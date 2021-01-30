# Set Up

- [Environmental Variables](#environmental-variables)
- [Clone the Repository](#clone-the-repository)
- [Virtual Environment](#virtual-environment)
- [Requirements](#requirements)

## Environmental Variables

- [What](#what)
- [How](#how)

### What

- `USER_NAME_PASSWORD`
    - you can create as many of these as required
    - they need to follow this format:
        - all capital letters
        - ending with `PASSWORD`
        - all words separated by an underscore `_`
        - the words before `PASSWORD` should be the desired username
        - e.g. `export TIM_HORTON_PASSWORD=someHashedPassword`
        - `generate_password_hash` can be used to create a hashed password
- `GUARDIAN_JWT_KEY`
    - a random secret key used when signing JWT tokens
    - e.g. `openssl rand -hex 32`
- `GUARDIAN_API_KEY`
    - create a key [here](https://open-platform.theguardian.com/access/)

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
