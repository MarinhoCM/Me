// Exemplo de uso das funções de array

// concat()
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const newArray = array1.concat(array2);
console.log(newArray); // Output: [1, 2, 3, 4, 5, 6]

// filter()
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // Output: [2, 4]

// find()
const fruits = ['apple', 'banana', 'orange', 'mango'];
const result = fruits.find(fruit => fruit.length > 5);
console.log(result); // Output: 'banana'

// findIndex()
const scores = [80, 90, 70, 85];
const index = scores.findIndex(score => score > 80);
console.log(index); // Output: 1

// forEach()
const names = ['Alice', 'Bob', 'Charlie'];
names.forEach(name => console.log(`Hello, ${name}!`));
// Output:
// Hello, Alice!
// Hello, Bob!
// Hello, Charlie!

// pop()
const stack = [1, 2, 3];
const poppedElement = stack.pop();
console.log(stack); // Output: [1, 2]
console.log(poppedElement); // Output: 3

// shift()
const queue = [1, 2, 3];
const shiftedElement = queue.shift();
console.log(queue); // Output: [2, 3]
console.log(shiftedElement); // Output: 1

// push()
const numbersArray = [1, 2, 3];
numbersArray.push(4);
console.log(numbersArray); // Output: [1, 2, 3, 4]

// unshift()
const numbersArray2 = [2, 3, 4];
numbersArray2.unshift(1);
console.log(numbersArray2); // Output: [1, 2, 3, 4]

// reduce()
const values = [1, 2, 3, 4, 5];
const sum = values.reduce(
    (accumulator, currentValue) => accumulator + currentValue
);
console.log(sum); // Output: 15

// reverse()
const letters = ['a', 'b', 'c'];
const reversedLetters = letters.reverse();
console.log(reversedLetters); // Output: ['c', 'b', 'a']

// slice()
const originalArray = [1, 2, 3, 4, 5];
const slicedArray = originalArray.slice(1, 3);
console.log(slicedArray); // Output: [2, 3]

// sort()
const fruitsArray = ['banana', 'apple', 'orange'];
fruitsArray.sort();
console.log(fruitsArray); // Output: ['apple', 'banana', 'orange']

// splice()
const months = ['January', 'February', 'April', 'May'];
months.splice(2, 0, 'March');
console.log(months); // Output: ['January', 'February', 'March', 'April', 'May']
