docker network create traefik
docker-compose -f docker-compose.traefik.yml up -d
docker-compose up --build