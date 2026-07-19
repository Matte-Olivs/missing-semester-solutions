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