## Packaging and Shipping Code


Save your environment with printenv to a file, create a venv, activate it, printenv to another file and diff before.txt after.txt. What changed in the environment? Why does the shell prefer the venv? (Hint: look at $PATH before and after activation.) Run which deactivate and reason about what the deactivate bash function is doing.


- When activating the virtual environment, the beginning of the $PATH variable points directly to it, loading the selected Python version immediately.

```
Before:
PATH=/home/matteo/.local/bin:/

After:
PATH=/home/matteo/Documents/project/venv/bin:/home/matteo/.local/bin:/
```

- deactivate restores the $PATH variable to the value used before running source venv/bin/activate.

```
if [ -n "${_OLD_VIRTUAL_PATH:-}" ]; then
    PATH="${_OLD_VIRTUAL_PATH:-}";
    export PATH;
    unset _OLD_VIRTUAL_PATH;
fi;

if [ -n "${_OLD_VIRTUAL_PYTHONHOME:-}" ]; then
    PYTHONHOME="${_OLD_VIRTUAL_PYTHONHOME:-}";
    export PYTHONHOME;
    unset _OLD_VIRTUAL_PYTHONHOME;
fi;
```


Create a Python package with a pyproject.toml and install it in a virtual environment. Create a lockfile and inspect it.

- In hello.py:

```
def cli():
    print("Hello, world!")


if __name__ == "__main__":
    cli()
```

- In pyproject.toml:
```
[project]
name = "hello"
version = "0.1.0"
description = "A hello world library"
dependencies = []

[project.scripts]
hello = "hello:cli"

[build-system]
requires = ["setuptools>=61.0"]
```

- Then:

``` 
activate the virtual env:
source venv/bin/activate

build the program and install it:
uv build
uv pip install ./hello-0.1.0-py3-none-any.whl

→ now we can type hello in our terminal to use the program anywhere

We can run uv lock to create the lockfile:

requires-python = ">=3.12" (no other dependencies in this case)
``` 


Install Docker and use it to build the Missing Semester class website locally using docker compose.