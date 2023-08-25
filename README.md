#docker run -v $PWD:/share --rm -t python:3.11.4-bullseye bash -c 'python -mvenv pex.venv && ./pex.venv/bin/pip install -U pex && ./pex.venv/bin/pex3 interpreter inspect --python /usr/local/bin/python3.11 --markers --tags --indent 2' > out.json

docker run --platform linux/x86_64

$ pants run --docker-run-args="-p 127.0.0.1:80:8080/tcp --name demo" src/example:image -- [image entrypoint args]

pants run --docker-run-args="--network host" src/docker/client:client-container

pants run --docker-run-args="-p 8080:8080" src/docker/client:client-container

pants run src/docker/server:server-container

# Running containers

- `docker network create -d bridge pants-bridge`
- `pants run --docker-run-args="-p 8080:8080 --network=pants-bridge --name client-container" src/docker/client:client-container`
- `pants run --docker-run-args="--network=pants-bridge --name server-container" src/docker/server:server-container`
