# Define a self-contained, relocatable binary that contains a complete Python environment
# (i.e., code and dependencies but not the interpreter itself). See https://pex.readthedocs.io
python_sources()

pex_binary(
  name="binary-local",
  entry_point="src.python.server.main:main",
  layout = "packed",
  execution_mode = "venv",
)

pex_binary(
  name="binary-linux",
  entry_point="src.python.server.main:main",  layout = "packed",
  execution_mode = "venv",
  complete_platforms = ["src/python:platforms"]
)
