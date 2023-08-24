# Define a self-contained, relocatable binary that contains a complete Python environment
# (i.e., code and dependencies but not the interpreter itself). See https://pex.readthedocs.io
python_sources()

python_requirements(
    name="reqs",
)

pex_binary(
  name="server-binary",
  entry_point="server.main:main",
  # Enable hot re-load
  # restartable=True
)

# Define a docker image that can be used to ship our Python env truly everywhere
docker_image(name="container")
