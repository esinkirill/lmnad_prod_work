#!/bin/bash

mysqldump=/usr/bin/mysqldump
mysql_user=root
mysql_password=78910

basedir=/root/backup
backup_dir=files

# Clear current backups
cd $basedir/$backup_dir
rm -f backup*

now=$(date +"%d_%m_%Y")

# Make mysql backup
$mysqldump --user=$mysql_user --password=$mysql_password --triggers --routines --databases lmnad_db | gzip > backup_$now.sql.gz

# Make files backup
tar cvzf backup.lmnad_uploads_$now.tar.gz /lmnad/project/media/

