"""Módulo de testes"""
from typer import (
    Argument, Exit, Option, run
)

__version__ = 'v0.0.1'

def version(args: str):
    if args:
        print(__version__)
        raise Exit(code=0)
    
run(version)