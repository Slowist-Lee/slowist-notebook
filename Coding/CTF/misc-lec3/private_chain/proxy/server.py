from typing import Union
from enum import IntEnum

import http.server
import http.client

import json
import gzip
import logging

logger = logging.getLogger(name="regeth")
logger.setLevel(level=logging.INFO)

hdr = logging.FileHandler(filename="/var/log/regeth/access.log")
hdr.setLevel(level=logging.INFO)
hdr.setFormatter(fmt=logging.Formatter("%(levelname)s [%(asctime)s] %(message)s"))

logger.addHandler(hdr)


class JSONRPCErrorCode(IntEnum):
    
    """Ethereum JSON-RPC error codes

    If an Ethereum RPC method encounters an error, the error member included on the response object MUST be
    an object containing a code member and descriptive message member.

    All the following error codes are observed from EIP-1474.
    """

    def __new__(cls, value, message):
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.message = message
        return obj
    
    # basic errors
    PARSE_ERROR = -32700, "Parse error"
    INVALID_REQUEST = -32600, "Invalid request"
    METHOD_NOT_FOUND = -32601, "Method not found"
    INVALID_PARAMS = -32602, "Invalid params"
    INTERNAL_ERROR = -32603, "Internal error"

    # eip 1474 non-standard
    INVALID_INPUT = -32000, "Invalid input"
    RESOURCE_NOT_FOUND = -32001, "Resource not found"
    RESOURCE_UNAVAILABLE = -32002, "Resource unavailable"
    TRANSACTION_REJECTED = -32003, "Transaction rejected"
    METHOD_NOT_SUPPORTED = -32004, "Method not supported"
    LIMIT_EXCEEDED = -32005, "Limit exceeded"
    JSONRPC_VERSION_NOT_SUPPORTED = -32006, "JSON-RPC version not supported"
    
    # user defined errors
    SANDBOXED_METHOD = -32300, "Sandboxed method"


Server = http.server.HTTPServer
Handler = http.server.BaseHTTPRequestHandler
Connection = http.client.HTTPConnection

class GethRequestHandler(Handler):
    
    """Geth RPC request handler with only POST commands.

    This handler essentially receives requests from clients and transfers them to a local Geth node through
    an HTTP connection. This approach allows us to easily implement restricted access to Geth by applying a
    Web Application Firewall (WAF) to the RPC methods.

    """
    
    # local geth rpc port, default is 18545
    grpc_port = 18545    
    
    white_list = [
        # rpc
        "rpc_modules",
        # web3
        "web3_clientVersion",
        "web3_sha3",
        # net
        "net_version",
        # eth
        "eth_coinbase",
        "eth_chainId",
        "eth_mining",
        "eth_hashrate",
        "eth_gasPrice",
        "eth_feeHistory",
        "eth_blockNumber",
        "eth_getBalance",
        "eth_getStorageAt",
        "eth_getTransactionCount",
        "eth_getBlockTransactionCountByHash",
        "eth_getBlockTransactionCountByNumber",
        "eth_getCode",
        "eth_sendRawTransaction",
        "eth_call",
        "eth_estimateGas",
        "eth_getTransactionByHash",
        "eth_getTransactionReceipt",
    ]
    
    grey_list = [
        "eth_getBlockByHash",
        "eth_getBlockByNumber",
    ]

    def proxy_response(self, status: http.HTTPStatus, content: Union[str, bytes]):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        if isinstance(content, str):
            content = content.encode("utf-8")
        self.wfile.write(content)
    
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        # default content encoding
        encoding = "utf-8"
        if "gzip" in self.headers.get("Accept-Encoding", ''):
            self.encoding = "gzip"
        payload = self.rfile.read(length)
        try:
            payload_json = json.loads(payload)
        except Exception:
            # Why 500? Ref: https://www.jsonrpc.org/historical/json-rpc-over-http.html#id17
            self.proxy_response(
                http.HTTPStatus.INTERNAL_SERVER_ERROR,
                jsonrpc_error_object(JSONRPCErrorCode.PARSE_ERROR, None)
            )
            return
        
        try:
            conn = Connection("localhost", self.grpc_port)
            conn.request(
                method="POST",
                url=self.path,
                body=payload,
                headers=self.headers,
            )
        except Exception:
            logger.warn(f"Local geth node http://localhost:{self.grpc_port} not ready yet")
            return

        response = conn.getresponse()
        res_content = response.read()
        if self.encoding == "gzip":
            res_content = gzip.decompress(res_content)
        try:
            res_content_json = json.loads(res_content)
        except Exception:
            self.proxy_response(
                http.HTTPStatus.INTERNAL_SERVER_ERROR,
                jsonrpc_error_object(JSONRPCErrorCode.INTERNAL_ERROR, None)
            )
        else:
            if "error" in res_content_json.keys():
                self.proxy_response(response.status, res_content)
                return
            
            # --- no filter ---

            # rpc_method = payload_json["method"]
            # if  rpc_method not in self.white_list + self.grey_list:
            #     self.proxy_response(
            #         http.HTTPStatus.METHOD_NOT_ALLOWED,
            #         jsonrpc_error_object(JSONRPCErrorCode.SANDBOXED_METHOD, res_content_json["id"])
            #     )
            #     return
            
            # if rpc_method in self.grey_list:
            #     # This is intended to enable MetaMask or other crypto wallets, since
            #     # the methods in grey_list are used in the interaction process. However,
            #     # the content of `transactions` should be erased to keep the game fair.
            #     res_content_json["result"]["transactions"] = []
            #     res_content = json.dumps(res_content_json)
                
            self.proxy_response(response.status, res_content)
        finally:
            conn.close()
            client_ip, _ = self.client_address
            logger.info(f"Connection from {client_ip} requests {json.dumps(payload_json)}")


def jsonrpc_error_object(err_code: JSONRPCErrorCode, id: Union[int, None]) -> str:
    return json.dumps({
        "jsonrpc": "2.0",
        "id": id,
        "error": {
            "code": err_code.value,
            "message": err_code.message,
        },
    })
    
    
HOST = "0.0.0.0"
PORT = 8545

if __name__ == "__main__":
    proxy = Server((HOST, PORT), GethRequestHandler)
    logger.info(f"Starting geth proxy server on http://{HOST}:{PORT}")
    proxy.serve_forever()
    