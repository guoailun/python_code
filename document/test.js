// function login(userName) {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             console.log('login')
//             resolve('1001');
//         }, 600);
//     });
// }

// function getData(userId) {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             if (userId === '1001') {
//                 console.log('getData')
//                 resolve('Success');
//             } else {
//                 reject('Fail');
//             }
//         }, 600);
//     });
// }

// // 不使用async/await ES7
// function doLogin(userName) {
//     login(userName)
//         .then(getData)
//         .then(result => {
//             console.log(result)
//         })
// }

// // 使用async/await ES8
// async function doLogin2(userName) {
//     const userId = await login(userName);
//     const result = await getData(userId);
//     console.log(userId, result)
// }

// doLogin()// Success
// doLogin2()// Success

// console.log('step1');

// function step2() {
//     console.log('step2 start');
//     setTimeout(() => {
//         console.log("step2=>setTimeout")
//     }, 1000)
//     console.log('step2 end');
// }



// step2();

// console.log('step3');

// setTimeout(() => {
//     console.log('step4')
// }, 2000)

// console.log('step5');

// function step6() {
//     console.log('step6 start')
//     return new Promise((resolve, reject) => {
//         console.log('step6 Promise');
//         resolve('success');
//     })
// }

// step6();
// console.log('step7')
// function step8() {
//     console.log('step8 start')
//     return new Promise((resolve, reject) => {
//         console.log('step8 Promise');
//         resolve('success');
//     })
// }

// console.log('step9')

// async function step10() {
//     console.log('step10 start')
//     let end = await step8();
//     console.log(end)
//     console.log('step10 end')
// }
// step10();
// console.log('end')


// console.log('0.0'.padStart(6, '10')) //10.0
// console.log('0.0'.padStart(20))//0.00
console.log('ab'.padStart(5, 'cdefgh'))
console.log('ab'.padEnd(5, 'cdefgh'))

