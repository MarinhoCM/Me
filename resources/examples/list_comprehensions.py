# Exemplo 1: Gerando uma lista de números pares
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]

# Exemplo 2: Transformando uma lista de strings em letras maiúsculas
names = ['john', 'mary', 'peter', 'ana']
uppercase_names = [name.upper() for name in names]
print(uppercase_names)  # Output: ['JOHN', 'MARY', 'PETER', 'ANA']

# Exemplo 3: Filtrando números ímpares e elevando ao cubo
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes_odd = [x**3 for x in numbers if x % 2 != 0]
print(cubes_odd)  # Output: [1, 27, 125, 343, 729]

# Exemplo 4: Gerando uma lista de tuplas (número, número ao quadrado)
squares = [(x, x**2) for x in range(1, 6)]
print(squares)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Exemplo 5: Filtrando elementos de uma lista de listas
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_elements = [
    element for row in matrix for element in row if element % 2 == 0
]
print(even_elements)  # Output: [2, 4, 6, 8]
