# Test tasks

## Execution (with docker)

1. Clone the project
2. Docker-compose

   Check-up the ports in `docker-compose.yml` (if you want to use Flask)
   Up the docker-compose by `docker-compose up -d`

## Run tests and tasks (inside container)

Run tests: `pytest --cov=.`

Run flask: `cd /home/src/task_2a && flask run -h 0.0.0.0`
