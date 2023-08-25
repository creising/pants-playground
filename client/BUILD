python_sources()

#python_requirements(
#    name="reqs",
#)

python_tests(
    name="tests",
    skip_mypy=True
)

pex_binary(
  name="binary",
  entry_point="client.main",
)

docker_image(name="container")