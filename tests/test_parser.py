"""Test the parser"""

from typing import Any

import pytest

from melly.parser import parse


@pytest.mark.parametrize(
    "input_,output",
    [
        ("py! 1+1", 2),
        ("py! 1/0", "exception=ZeroDivisionError('division by zero')"),
    ],
)
def test_parser(input_: str, output: Any) -> None:
    assert parse(input_) == output
