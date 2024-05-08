#!/bin/bash

mysql_user=root
mysql_password=78910

now=$(date +"%d_%m_%Y")

docker exec lmnad_web sh -c 'mkdir -p /root/backup && rm -f /root/backup/* && tar cvzf /root/backup/backup.lmnad_uploads_$1.tar.gz /lmnad/project/media/' sh "$now"

docker exec lmnad_mysql sh -c 'mkdir -p /root/backup && rm -f /root/backup/* && mysqldump --user=$1 --password=$2 --triggers --routines --databases lmnad_db | gzip > /root/backup/backup_$3.sql.gz' sh "$mysql_user" "$mysql_password" "$now"

docker cp lmnad_mysql:/root/backup/backup_$now.sql.gz /tmp/

docker cp /tmp/backup_$now.sql.gz lmnad_web:/root/backup
