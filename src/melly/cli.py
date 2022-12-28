"""CLI building"""

from .parser import parse


def cli():
    """Run the CLI"""
    try:
        while True:
            line = input("|> ")
            print(parse(line))
    except (EOFError, KeyboardInterrupt):
        print("\nShutting down...")
