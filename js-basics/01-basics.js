//การประกาศตัวแปรใน JavaScript สามารถทำได้โดยใช้คำสั่ง var, let หรือ const es6

//แบบเก่า
var firstName = "John";
console.log(firstName);

//แบบใหม่
let fullName = "Jany Doe";
fullName = "Jany Smith"; //สามารถเปลี่ยนค่าได้
console.log(fullName);

const age = 40;//ไม่สามารถเปลี่ยนค่าได้
console.log(age);

//traditional function
function greet(name) {
    return "Hello, " + name ;
}
console.log(greet("John"));

//arrow function
// const greetArrow = (name) => {
//     return "Hello, " + name ;
// }
// console.log(greetArrow("John"));

// const greetArrow = (name) => "Hello, " + name ; //ถ้า return แค่ค่าเดียวสามารถเขียนแบบนี้ได้
// console.log(greetArrow("John"));
//const greetArrow =()=> "Hello Word " ; //ไม่มีการรับparamator

//Template literals
const message_traditional = "My name is " + fullName + " and I am " + age + " years old.";
const message = `My name is ${fullName} and I am ${age} years old.`;
console.log(message_traditional);
console.log(message);
