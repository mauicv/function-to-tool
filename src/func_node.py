from importlib import import_module
from inspect import signature, Parameter
import os
import click


class FunctionNode:
    def __init__(self, name, func_path, desc):
        self.name = name
        self.desc = desc
        self.import_path = os.path \
            .splitext(func_path)[0] \
            .replace('/', '.')
        self.func = getattr(import_module(self.import_path), name)

    def _get_params(self):
        v = signature(self.func)
        return [
            (
                '--{}'.format(param_name),
                full_val.default if full_val.default
                is not Parameter.empty else None
            )
            for param_name, full_val in v.parameters.items()
        ]

    def __call__(self, group):
        params = self._get_params()
        decorator = group.command()
        self.func = decorator(self.func)
        for param in params:
            self.func = click \
                .option(param[0], default=param[1])(self.func)
        self.func.__name__ = self.name
        return self.func
