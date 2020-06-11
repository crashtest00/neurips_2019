This project is to track notable documents from NeurIPS 2019 in a Django database.

How to run:
- Install Docker and Docker Compose
https://docs.docker.com/engine/install/ubuntu/
https://docs.docker.com/compose/install/
- Create project directory
- Copy dockerfile, requirements.txt, and docker-compose.yaml into project directory
- Start Docker daemon (sudo dockerd)
- Run docker-compose up

- For each deploy, `docker system prune` should reset docker to a zero state without nuking the DB. Test this...obvs...
