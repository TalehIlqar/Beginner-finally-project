var plasticCard = document.getElementsByClassName('plasticCard')
var sameclass = document.querySelectorAll(".sameclass")
sameclass.forEach(element => {
    element.addEventListener('click', function () {
        for (let i = 0; i < plasticCard.length; i++) {
            if (plasticCard[i].classList.contains(`${this.innerText}`)) {
                plasticCard[i].classList.remove('d-none')     
                plasticCard[i].classList.add('d-flex')

            } else {
                plasticCard[i].classList.add('d-none')                
                plasticCard[i].classList.remove('d-flex')

            }
        }
        if (`${this.clicked == true}`) {
            for (let i = 0; i < sameclass.length; i++) {
                sameclass[i].classList.add('bg-white')
                sameclass[i].classList.remove('bg-secondary')
                sameclass[i].classList.add('text-dark')
                sameclass[i].classList.remove('text-light')
            }
 
            this.classList.remove('bg-white')
            this.classList.add('bg-secondary')
            this.classList.remove('text-dark')
            this.classList.add('text-light')
        }
    })
})

