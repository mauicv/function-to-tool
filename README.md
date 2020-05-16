# Function To Tool  


A python tool that converts functions into commandline tools with no effort. All you do is add a doc string and it will be parsed into a commandline tool.

___

## Example

In `some_python_function` in `some_python_file.py` in your project source folder, `example_project`:

```py
def some_python_function(value):
    """to-tool"""
    print(value)
    return value
```

Then at the beggining of your `main.py`:

```py
from src import register_fn
register_fn('example_project')
```

And now you can do:

```sh
python main.py some-python-function --value="hello world"
```
___

__NOTE__: This was done as a quick project and isn't maintained properly. For a library that does the exact same thing far better see: [clippy](https://pypi.org/project/Clippy/).
