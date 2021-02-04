#!/bin/sh

maxcounter=45
counter=1

HOST="db"
MYSQL_USER="root"
MYSQL_PASSWORD="root"

while ! mysql --protocol TCP -h"$HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "show databases;" > /dev/null 2>&1; do
	echo "sleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep"
    sleep 1
    counter=`expr $counter + 1`
    if [ $counter -gt $maxcounter ]; then
        >&2 echo "We habe been waiting for MySQL too long already; failing."
        return
    fi;
done
