
docker_image(
  name="processor-container"
)

run_shell_command(
    name="run-container",
    command='docker rm --force processor-container && pants run --docker-run-args="--network=pants-dev-network --name processor-container" src/docker/processor:processor-container',
)