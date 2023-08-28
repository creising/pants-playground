
docker_image(
  name="server-container"
)

run_shell_command(
    name="run-container",
    command='docker rm --force server-container && pants run --docker-run-args="--network=pants-dev-network --name server-container" src/docker/server:server-container',
)