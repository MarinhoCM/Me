# Funções de Array em JavaScript

Este repositório contém exemplos e explicações sobre algumas das principais funções de array em JavaScript.

## concat()

A função `concat()` junta dois arrays, colocando o array passado como argumento imediatamente após o primeiro array. Essa operação é conhecida como concatenação em português. A função não altera o array original, portanto, é necessário salvar o resultado em um novo array.

## filter()

A função `filter()` retorna uma lista contendo todos os elementos que passaram em um determinado teste, que é uma função definida por nós. Ela não altera o array original e requer que o resultado seja armazenado em um novo array.

## find()

A função `find()` funciona de forma semelhante ao `filter()`, mas retorna apenas o primeiro valor que satisfaz o teste. Esse valor pode ser uma string ou um número.

## findIndex()

A função `findIndex()` é semelhante à função `find()`, mas retorna o índice do elemento em vez do próprio elemento. Isso possibilita o uso do índice em outras partes do código.

## lastIndexOf()

A função `lastIndexOf()` é similar à `findIndex()`, porém começa a busca a partir do último elemento do array, em vez do primeiro.

## forEach()

A função `forEach()` executa uma função em cada elemento do array, de forma individual. Ela não altera o array original e não retorna um valor, deixando essa responsabilidade para a função fornecida.

## pop()

A função `pop()` remove o último elemento do array. Ela altera o array original, removendo o elemento.

## shift()

A função `shift()` remove o primeiro elemento do array. Ela altera o array original, removendo o elemento e ajustando os índices dos elementos restantes. O índice 1 passa a ser 0, o índice 2 passa a ser 1 e assim por diante.

## push()

A função `push()` adiciona o elemento passado como parâmetro ao array, na última posição. Ela altera o array original com o novo valor.

## unshift()

A função `unshift()` é semelhante ao `push()`, mas adiciona o elemento na primeira posição do array, ajustando os índices de todos os outros elementos. Ela altera o array original com o novo valor.

## reduce()

A função `reduce()` aplica uma função definida pelo usuário a cada um dos elementos do array, acumulando o resultado em uma variável que pode ser acessada dentro da função. Ela retorna um único valor no final, reduzindo o array a um único valor.

## reduceRight()

A função `reduceRight()` funciona de forma semelhante ao `reduce()`, mas começa a partir do final do array e percorre até o início.

## reverse()

A função `reverse()` inverte a ordem dos elementos do array. O primeiro elemento se torna o último, o segundo se torna o penúltimo e assim por diante.

## slice()

A função `slice()` copia uma parte do array para outro array.

## sort()

A função `sort()` organiza o array de acordo com a classificação Unicode. No entanto, não funciona corretamente para ordenar números, exigindo a definição de uma função auxiliar para classificar corretamente.

## splice()

A função `splice()`
