#!/bin/bash
# wait-for-db.sh

set -e

#host="$1"
#shift
cmd="$@"

# we sleep to wait for mysql to start up lol
sleep 5

>&2 echo "DB is up - executing command"
exec $cmd
