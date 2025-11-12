// Equivalent of Python: evens = [x for x in numbers if x % 2 == 0]
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const evens = numbers.filter(x => x % 2 === 0);

console.log(evens); // [2, 4, 6, 8, 10]
