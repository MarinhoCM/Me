"""Módulo que armazena as funções de menssagens"""
def error_message(message):
    """
    error_message():
        Função que recebe um texto e cria um erro para esse texto.
    Args:
        message: variável que recebe o texto da mensagem  
    """
    text = f'\033[31m{message}\033[0m'
    assert False, (str(text))

def sucess_message(message):
    """
    error_message():
        Função que recebe um texto e cria um erro para esse texto.
    Args:
        message: variável que recebe o texto da mensagem  
    """
    text = f'\033[32m{message}\033[0m'
    return text
    