"""Parsing the input text"""

from collections.abc import Callable
from typing import Any
from uuid import uuid4

FUNCTIONS: dict[str, Callable] = {"uuid": uuid4}


def _parse_python(text: str) -> Any:
    """Attempt to parse and execute input as Python"""
    try:
        output = eval(compile(text, "<string>", "eval"))  # pylint: disable=eval-used
    except Exception as exception:  # pylint: disable=broad-except
        output = f"{exception=}"
    return output


def parse(line: str) -> Any:
    """Attempt to parse and execute input"""
    if function := FUNCTIONS.get(line):
        output = function()
    elif line.startswith("py!"):
        line = line.removeprefix("py! ")
        output = _parse_python(line)
    else:
        output = "failed to parse line"
    return output
