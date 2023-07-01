"""Módulo principal utilizado no projeto"""
from typer import (
    Exit, Option, run
)

from utils.GenerateFiles import GenerateFiles
from utils.messages import sucess_message
from utils.Files import verify_files

__version__ = 'v0.0.1'


def version(args: str) -> None:
    if args:
        print(__version__)
        raise Exit(code=0)


def generate_files(args: str) -> None:
    if args:
        GenerateFiles()
        if verify_files('features') and verify_files('Support'):
            print(sucess_message(
                'Diretório gerado com sucesso!'
            ))
        raise Exit(code=0)


def main(
    version_: bool = Option(False,
        '--version', '-v', '--Version', '-version',
        '--v',
        callback=version,
        is_eager=True,
        is_flag=True
    ), 
    init: bool=Option(
        False,
        '--init',
        callback=generate_files,
        help='Responsável por iniciar a CLI e construir os diretórios',
        is_eager=True,
        is_flag=True
    )
) -> None:
    ...
    

if __name__ == '__main__':
    run(main)
    