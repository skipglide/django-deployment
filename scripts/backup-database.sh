#!/bin/bash
set -e
echo -e "\n >>> Backing up database on $SERVER"
TIME=$(date "+%s")
DBNAME="db.$TIME.sqlite3"

set -e
mkdir -p /root/backups/
cp /app/db.sqlite3 /root/backups/$DBNAME

mkdir -p ~/backups/
scp root@45.55.40.138:/root/backups/* ~/backups/ 