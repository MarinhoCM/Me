"""Módulo responsável por armazenar a funções relacionadas a arquivos"""

import os


def verify_files(path: str) -> bool:
    """Função responsável por verificar a
    existência de arquivos e diretórios"""
    if os.path.exists(path):
        return True
    else:
        return False


def create_file(path: str, file_content=None) -> None:
    """Função responsável por criar os arquivos"""
    with open(path, "w", encoding='UTF8') as arquive:
        if file_content:
            arquive.write(file_content)
