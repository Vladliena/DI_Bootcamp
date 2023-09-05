const { myArr } = require('./product.js')

const findName = (name) => myArr.find((el) => el.name == name)

console.log(findName('tea'))
console.log(findName('milk'))
console.log(findName('cookies'))

