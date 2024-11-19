// console.log("line1")
// function hello() {
//     console.log("Helllo Javascript")
// }
// setTimeout(hello, 2000)
// console.log("Line 2")


// function sum(a, b) {
//     console.log(a+b)
// }

// function calculateSum(a, b, callbackSum){
//     callbackSum(a,b)
// }

// calculateSum(2,3,sum)



//Callback Hell - Nested Callbacks stacked below one another forming a pyramid structure
//This style of programming is difficult to understand and manage 
// function getData(dataId, nextData){
//     setTimeout(()=>{
//         console.log("data", dataId)
//         if(nextData){
//             nextData()
//         }
//     }, 1000)  
// }

// //Here I have to print first data1, after data2, after data3....
// getData(1, () => {
//     getData(2, () => {
//         getData(3, ()=> {
//             getData(4)
//         })
//     })
// })


//Promises
//Promises is for eventual completion of task. It is object in JS. It is solution to callback hell

// let promise = new Promise((resolve, reject) => {
//     console.log("I am a Promise")
//     resolve("success")
// })


// const getPromise = () => {
//     return new Promise((resolve, reject) => {
//         console.log("I am promise")
//         resolve("success")
//     })
// }

// let promise = getPromise()
// promise.then((res)=>{
//     console.log("Promise fulfilled", res)
// })
// promise.catch((err)=>{
//     console.log("rejected", err)
// })


//async-await
//async function always return promise
//await pauses the execution of its surrounding async function untill the promise is settled

// async function getData() {
//     await fetch(url)
// }


// Fetch API - It is an interface for fetching(sending/receiving) resources
// It uses request and response object.
// fetch method used to fetch resourse(data)
// let promise = fetch(url, [options])

// const url = 'https://api.restful-api.dev/objects'
// const fetchPara = document.querySelector('#facts')
// const btn = document.querySelector("#btn")

// //Fetching data using async-await from api

// const getFacts = async () => {
//     const response = await fetch(url)
//     const data = await response.json()
//     console.log(data[0])
//     fetchPara.innerText = data[1].name
// }

// //Fetching data using Promises from api

// // function getFacts(){
// //     fetch(url).then((response)=> {
// //         return response.json()
// //     }).then((data) => {
// //         console.log(data[1])
// //         fetchPara.innerText = data[1].name
// //     })
// // }


// btn.addEventListener("click", getFacts)


//Class and Objects
// class ToyotaCar {
//     constructor(brand, mileage) {
//         this.brand = brand
//         this.mileage = mileage
//     }
//     start = () => {
//         console.log("Start")
//     }

//     stop = () => {
//         console.log("Stop")
//     }

//     // setBrand(brand){
//     //     this.brand = brand
//     //     console.log("Brand is", brand)
//     // }
// }

// let fortuner = new ToyotaCar("fortuner", 60)
// console.log(fortuner)



// class User {
//     constructor(name, email){
//         this.name = name
//         this.email = email
//     }

//     viewData(){
//         console.log("You can view data")
//     }
// }

// user1 = new User("Rohit", "rohit@123")
// console.log(user1)


// class Admin extends User {
//     constructor(name, email){
//         super(name, email)
//     }
//     editData(){
//         console.log("Admin can edit data")
//     }
// }

// admin = new Admin("admin", "admin@123")
// console.log(admin.editData())