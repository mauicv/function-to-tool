import ast
import os
from docstring_parser import parse
from src.func_node import FunctionNode


def collect_fn(directory):
    all_fn = []

    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext == '.py':
                with open(os.path.join(root, filename)) as fd:
                    file_contents = fd.read()
                    module = ast.parse(file_contents)
                    function_definitions = [
                        node for node in module.body
                        if isinstance(node, ast.FunctionDef)]

                    for func in function_definitions:
                        doc_string = ast.get_docstring(func)
                        fm_valid, parsed_data = parse_docstring(doc_string)
                        if fm_valid:
                            all_fn.append(FunctionNode(
                                name=func.name,
                                func_path=os.path.join(root, filename),
                                desc=parsed_data.short_description
                            ))
    return all_fn


def parse_docstring(doc_string):
    parsed_data = parse(doc_string)
    if verify_use_fmap(parsed_data):
        return True, parsed_data
    else:
        return False, None


def verify_use_fmap(parsed_data):
    for attr in ['short_description', 'long_description']:
        attr_data = getattr(parsed_data, attr, False)
        if attr_data and 'to-tool' in attr_data:
            return True
    return False
