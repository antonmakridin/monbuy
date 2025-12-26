const mybutton = document.querySelector('button')
const give = document.querySelector('#give')
const thx = document.querySelector('#thx')
const server = document.querySelector('#server')

console.log(mybutton)

mybutton.onclick = function (){
    const mydiv = document.querySelector('#content')
    mydiv.textContent = 'Дай денег'
}

give.onclick = function (){
    const mydiv = document.querySelector('#content')
    mydiv.textContent = 'Дай денег'
}

thx.onclick = function (){
    const mydiv = document.querySelector('#content')
    mydiv.textContent = 'Спасибо, ваш голос услышан'
}

server.onclick = function (){
    fetch('http://127.0.0.1:8000/get_data')
    .then(res => res.json())
    .then(console.log)
}


