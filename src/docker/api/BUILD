docker_image(
  name="api-container",
)

run_shell_command(
  name="run-container",
  command='docker rm --force api-container && pants run --docker-run-args="-p 8080:8080 --network=pants-dev-network --name api-container -e PROC_URL=processor-container" src/docker/api:api-container',
)
