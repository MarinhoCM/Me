# Compreensão de Listas em Python

A compreensão de listas, ou list comprehension, é uma poderosa e concisa construção da linguagem Python que nos permite criar listas de forma elegante e eficiente. Com a compreensão de listas, podemos criar listas baseadas em outras listas, aplicando transformações e filtrando elementos de maneira direta.

## Sintaxe Básica

A estrutura básica de uma compreensão de listas em Python segue o seguinte formato:

```python
nova_lista = [expressao for elemento in lista_original if condicao]
```
- ``expressao``: é a expressão que define o valor de cada elemento na nova lista.
- ``elemento``: é uma variável temporária que representa cada elemento da lista original.
- ``lista_original``: é a lista de onde os elementos serão obtidos.
- ``condicao (opcional)``: é uma condição que determina se o elemento deve ser incluído na nova lista ou não.
