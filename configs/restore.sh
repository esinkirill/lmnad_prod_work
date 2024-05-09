#!/bin/bash

read -p "Введите дату резервной копии (в формате dd_mm_yyyy): " backup_date

if [ -z "$backup_date" ]; then
    echo "Дата резервной копии не указана."
    exit 1
fi

docker cp backup_${backup_date}.sql lmnad_mysql:/tmp

docker exec -i lmnad_mysql bash -c "mysql -u root -p78910 lmnad_db < /tmp/backup_${backup_date}.sql"

docker cp backup.lmnad_uploads_${backup_date}.tar.gz lmnad_web:/tmp

docker exec -i lmnad_web bash -c "cd /tmp && tar -xvf backup.lmnad_uploads_${backup_date}.tar.gz"

docker exec -i lmnad_web bash -c "cp -r /tmp/var/www/site/lmnad/project/media/uploads/ /lmnad/project/media/"

docker exec lmnad_web bash -c "rm -rf /tmp/var /tmp/backup.lmnad_uploads_${backup_date}.tar.gz"
docker exec lmnad_mysql bash -c "rm -rf /tmp/backup_${backup_date}.sql"
