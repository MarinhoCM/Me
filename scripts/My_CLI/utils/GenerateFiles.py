"""Módulo resposável por gerar o diretorio e os arquivos
ao ser requisitado pela CLI"""

import os

from .Files import verify_files, create_file
from .messages import error_message


class GenerateFiles:
    def __init__(self) -> None:
        GenerateFiles.generate_directory()

    def generate_directory() -> object:
        """Função responsável por criar todo o diretorio
        utilizado nos testes com BDD"""
        try:
            directory_features = "features"
            if verify_files(directory_features):
                create_file(
                    f'{directory_features}/file.feature',
                    'Funcionalidade:\n\tDado\n\tQuando\n\tE\n\tEntão'
                )
                create_file(f'{directory_features}/environment.py')
                create_file(f'{directory_features}/.gitignore')
                create_file('requirements.txt')
                if verify_files(f'{directory_features}/steps'):
                    create_file(f'{directory_features}/steps/step.py')
                    create_file(f'{directory_features}/steps/common_steps.py')
                else:
                    return False
            else:
                os.mkdir(f"{directory_features}")
                os.mkdir(f"{directory_features}/steps/")
                GenerateFiles.generate_directory()
        except Exception as err:
            raise Exception(error_message(
                'Ocorreu um erro ao tentar gerar ' +
                f'o diretório {directory_features}\n' +
                err
            ))
        try:
            directory_support = "support"
            if verify_files(directory_support):
                create_file(f'{directory_support}/__init__.py')
                if verify_files(f'{directory_support}/configs'):
                    create_file(f'{directory_support}/configs/settings.py')
                else:
                    return False
            else:
                os.mkdir(f'{directory_support}')
                os.mkdir(f'{directory_support}/configs/')
                GenerateFiles.generate_directory()
        except Exception as err:
            raise Exception(error_message(
                'Ocorreu um erro ao tentar gerar ' +
                f'o diretório {directory_support}\n' +
                err
            ))
    
    def write_in_files(text: str) -> None:
        """Função responsável por escrever o conteúdo 
        inicial dos arquivos criados por ( generate_directory )"""
        ... 
