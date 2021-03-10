DIR="/home/pi/terrarium"
docker network create traefik
docker-compose -f $DIR/docker-compose.traefik.yml up -d
docker-compose -f $DIR/docker-compose.yml up --build -d
