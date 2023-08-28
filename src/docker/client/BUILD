docker_image(
  name="client-container",
  # Currently not supported: https://github.com/pantsbuild/pants/issues/18386
  # restartable=True
)

run_shell_command(
    name="run-container",
    command='docker rm --force client-container && pants run --docker-run-args="-p 8080:8080 --network=pants-dev-network --name client-container" src/docker/client:client-container',
)