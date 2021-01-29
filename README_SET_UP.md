# Set Up

- [Environmental Variables](#environmental-variables)
- [Clone the Repository](#clone-the-repository)
- [Virtual Environment](#virtual-environment)
- [Requirements](#requirements)

## Environmental Variables

- [What](#what)
- [How](#how)

### What

TBD

### How

- this will vary, depending on your system
    - e.g. add them temporarily `export ENV_VAR_NAME=whatever_it_is`
    - e.g. add them permanently to `.bash_profile`

## Clone the Repository

- [clone](https://git-scm.com/docs/git-clone) this repository

## Virtual Environment

- [Assumptions](#assumptions)
- [Creation](#creation)
- [Activation](#activation)

### Assumptions

- [Python 3.9 (or greater)](https://www.python.org/) is installed
- [virtualenv](https://pypi.org/project/virtualenv/) is installed

### Creation

- `python3 -m venv gr_venv`
- see [here](https://docs.python.org/3/library/venv.html) for more detailed instructions, if necessary

### Activation

- `source gr_venv/bin/activate`

### Confirmation

- `which python` should display a path to a subfolder of this project
    - e.g. `/Users/youridentifier/projects/guardian_reader/gr_venv/bin/python`
- `python --version` should indicate some version of Python 3.9
    - e.g. `Python 3.9.1`

## Requirements

- `pip install -r requirements.txt`