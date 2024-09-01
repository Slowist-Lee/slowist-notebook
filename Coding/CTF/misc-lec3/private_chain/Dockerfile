FROM python:3.12-alpine

COPY genesis.json.template /genesis.json.template
COPY entrypoint.sh /entrypoint.sh
COPY proxy/server.py /server.py

# NOTE: Geth v1.11.5 enables the Shanghai upgrade on Wednesday, April 12, 2023 10:27:35 PM UTC
COPY --from=ethereum/client-go:v1.13.4 /usr/local/bin/geth /usr/local/bin/

RUN chmod +x /entrypoint.sh

EXPOSE 8545

ENTRYPOINT ["/entrypoint.sh"]
