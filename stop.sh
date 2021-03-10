DIR="/home/pi/terrarium"
docker-compose -f $DIR/docker-compose.traefik.yml -f $DIR/docker-compose.yml down
