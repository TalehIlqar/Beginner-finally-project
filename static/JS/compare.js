var selectcont = document.getElementsByClassName('selectcont')
var opption = document.getElementsByClassName('opption')
var muqaiseKart = document.getElementsByClassName('muqaiseKart')
xClass = document.getElementsByClassName('xClass')

for (let i = 0; i < opption.length; i++) {

    opption[i].addEventListener('change', function(){
        console.log('salam');        
        muqaiseKart[i].parentElement.classList.add('d-flex')

        muqaiseKart[i].classList.remove('d-none')
        selectcont[i].classList.add('d-none')
        try{
            selectcont[i+1].classList.remove('d-none')
        }catch{

        }
    })
} 

for (let j = 0; j < xClass.length; j++) {
    xClass[j].addEventListener('click', function(){
        muqaiseKart[j].classList.add('d-none')
        selectcont[j].classList.remove('d-none')
    })    
}













// var selectionClass = document.querySelectorAll(".selectionClass")
// var muqaiseKart = document.querySelectorAll(".muqaiseKart")
// var muqaise = document.querySelectorAll(".opption")

// muqaise.forEach(element => {
//     element.addEventListener("change", function () {
//         var intext = this.value
//         for (let i = 0; i < muqaiseKart.length; i++) {
//             y = muqaiseKart[i].children[0].innerText
//         }
//         console.log(y);
//         if (intext == y) {
//             muqaiseKart[i].classList.remove('d-none')
//         }
//     })
// });




// var selectcont = document.getElementById("selectcont")
// var muqaise = document.getElementById('opption');
// var muqaiseKart = document.querySelectorAll(".muqaiseKart")
// muqaise.addEventListener('change', function () {
//     // var intext = muqaise.options[muqaise.selectedIndex].text
//     var intext = `${this.value}`
//     // console.log(intext);
//     for (let i = 0; i < muqaiseKart.length; i++) {
//         let x = muqaiseKart[i].children[0]
//         // console.log(x.innerText);
//         muqaiseKart[i].classList.add("d-none")
//         if (intext == x.innerText) {
//             muqaiseKart[i].classList.remove("d-none")
//         }

//     }
//     selectcont.classList.add('d-none')
//     selectcont1.classList.remove('d-none')
// })

// var selectcont1 = document.getElementById("selectcont1")
// var muqaise1 = document.getElementById('opption1');
// var muqaiseKart1 = document.querySelectorAll(".muqaiseKart1")
// muqaise1.addEventListener('change', function () {
//     // var intext = muqaise.options[muqaise.selectedIndex].text
//     var intext1 = `${this.value}`
//     // console.log(intext);
//     for (let i = 0; i < muqaiseKart1.length; i++) {
//         let x = muqaiseKart1[i].children[0]
//         // console.log(x.innerText);
//         muqaiseKart1[i].classList.add("d-none")
//         if (intext1 == x.innerText) {
//             muqaiseKart1[i].classList.remove("d-none")
            
//         }

//     }
//     selectcont1.classList.add('d-none')
//     selectcont3.classList.remove('d-none')
// })



// var selectcont3 = document.getElementById("selectcont3")
// var muqaise3 = document.getElementById('opption3');
// var muqaiseKart3 = document.querySelectorAll(".muqaiseKart3")
// muqaise3.addEventListener('change', function () {
//     // var intext = muqaise.options[muqaise.selectedIndex].text
//     var intext3 = `${this.value}`
//     // console.log(intext);
//     for (let i = 0; i < muqaiseKart3.length; i++) {
//         let x = muqaiseKart3[i].children[0]
//         // console.log(x.innerText);
//         muqaiseKart3[i].classList.add("d-none")
//         if (intext3 == x.innerText) {
//             muqaiseKart3[i].classList.remove("d-none")
            
//         }

//     }
//     selectcont3.classList.add('d-none')
// })




// var xClass = document.getElementsByClassName('xClass')
// for (let i = 0; i < xClass.length; i++) {
//     xClass[i].addEventListener('click', function () {
//         xClass[i].parentElement.parentElement.parentElement.style.display = 'none'
//         selectcont3.classList.remove('d-none')

//     })
// }