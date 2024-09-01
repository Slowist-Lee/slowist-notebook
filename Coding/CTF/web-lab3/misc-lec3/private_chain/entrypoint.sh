#!/bin/sh -eu

TIMESTAMP=$(date +%s)
RANDPASSWD=$(head /dev/urandom | tr -dc 'A-Za-z0-9!@#$&_+=' | head -c 16)

GETH_DATA_DIR=/data
GETH_CHAINDATA_DIR=$GETH_DATA_DIR/geth/chaindata
GETH_KEYSTORE_DIR=$GETH_DATA_DIR/keystore

CHAIN_ID="${CHAIN_ID:-$((RANDOM + 10000))}"
DIFFICULTY="${DIFFICULTY:-1}"

[ -f "$GETH_DATA_DIR/alloc-address" ] && ALLOC_ADDRESS_WITHOUT_0X=$(cat "$GETH_DATA_DIR/alloc-address")
[ ! -d "$GETH_DATA_DIR" ] && mkdir "$GETH_DATA_DIR"

if [ ! -d "$GETH_KEYSTORE_DIR" ]; then
    echo "[INFO] $GETH_KEYSTORE_DIR missing, running account import"
    echo -n "$ALLOC_ADDRESS_PRIVATE_KEY" >"$GETH_DATA_DIR/private-key"
    echo -n "${ALLOC_ADDRESS_PRIVATE_KEY_PASSWORD:-$RANDPASSWD}" >"$GETH_DATA_DIR/password"
    ALLOC_ADDRESS_WITHOUT_0X=$(geth account import \
        --datadir="$GETH_DATA_DIR" \
        --password="$GETH_DATA_DIR/password" \
        "$GETH_DATA_DIR/private-key" | grep -oE '[[:xdigit:]]{40}')
    echo -n "$ALLOC_ADDRESS_WITHOUT_0X" >"$GETH_DATA_DIR/alloc-address"
    echo "[INFO] geth account import complete"
fi

if [ ! -d "$GETH_CHAINDATA_DIR" ]; then
    echo "[INFO] $GETH_CHAINDATA_DIR missing, running init"
    sed -i "s/\"\${CHAIN_ID}\"/$CHAIN_ID/g" /genesis.json.template
    sed -i "s/\${TIMESTAMP}/$TIMESTAMP/g" /genesis.json.template
    sed -i "s/\${DIFFICULTY}/$DIFFICULTY/g" /genesis.json.template
    sed -i "s/\${ALLOC_ADDRESS_WITHOUT_0X}/$ALLOC_ADDRESS_WITHOUT_0X/g" /genesis.json.template
    mv /genesis.json.template /genesis.json
    geth init --datadir="$GETH_DATA_DIR" /genesis.json
    echo "[INFO] geth init complete"
fi

exec geth \
    --datadir="$GETH_DATA_DIR" \
    --password="$GETH_DATA_DIR/password" \
    --allow-insecure-unlock \
    --unlock="$ALLOC_ADDRESS_WITHOUT_0X" \
    --mine --miner.etherbase="$ALLOC_ADDRESS_WITHOUT_0X"\
    --networkid="$CHAIN_ID" --nodiscover \
    --http --http.addr=0.0.0.0 --http.port=18545 \
    --http.api=eth,net,web3,personal \
    --http.corsdomain='*' --http.vhosts='*' &

echo "[INFO] geth start running at $(date -u -d @"$TIMESTAMP" +'%Y-%m-%d %H:%M:%S UTC')"

mkdir -p /var/log/regeth && python3 server.py
