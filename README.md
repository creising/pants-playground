# Introduction

This repo is a POC for using [Pants V2](https://www.pantsbuild.org/) for the
build system for a Monorepo whose primary language is Python.

The motivation here is to find a build system that can easily wrap common
libraries used while developing Python apps such as pytest, black, mypy and
others. What we want to avoid is having to deal with a hodgepodge of scripts and
tools and would much rather have a consistent interface that will support
development, testing, and deployment.

Pants also has pretty good support for Docker containers which might make
deployment easier as well.

# POC setup

This example project consists of two independent Python applications that share
a common library.

Note that each directory has its own BUILD file for defining behavior specific
to the directory it is in. Pants will pick these up automatically.

## Python source code

- `src/python/api` contains a RESTful API that will interact with the
  "processor" app using ZeroMQ
- `src/python/processor` responds to ZeroMQ messages and publishes random facts
  when a message is received
- `src/python/utils` is the amazing logging library shared between the two

## Docker

`src/docker` is where we define the containers used to deploy the API and
processing applications. Note that the docker files reference the artifacts from
other Build targets. Pants will recognize these dependencies and run the
necessary targets. FOr example, in the API container, we copy the artifact
`src.python.api/binary-linux.pex`.

# Install

See: https://www.pantsbuild.org/docs/installation

# Quick start

## [Goals](https://www.pantsbuild.org/docs/goals)

Pants uses the concept of "goals" (think of build targets). An operation is
categorized into a goal. For example, this project has black, flake8, and isort
enabled. If the `lint` goal is run all of these libraries will be invoked since
they are all considered a linter.

You can scope the goal. Here are some examples:

- `pants lint ::` will run the all linters over the entire project (the `::` is
  a wild card)
- `pants lint src/python/processor` will only run it over the processor module
- `pants lint src/python::` will run the linting over all python projects

Sometimes these commands can get a little verbose. You can create aliases in the
`pants.toml` (the pants config file) under the `[cli.alias]` section. For
example, this project has the alias `green = "fmt lint check"` which allows us
to run `pants green` to run the formatter, followed by the linter, and static
type checker.
