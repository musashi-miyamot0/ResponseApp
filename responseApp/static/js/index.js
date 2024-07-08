const logoutButton = document.querySelector('.logout')
const modelLogout = document.querySelector('.modalWindow')
const No = document.querySelector('.no')
const menu = document.querySelector('.menu')
const menuBtn = document.querySelector('.menuBtn')

logoutButton.addEventListener('click',()=>{
    modelLogout.style.display = 'grid'

})

No.addEventListener('click',()=>{
    modelLogout.style.display = 'none'
})

menuBtn.addEventListener('click',()=>{
    menu.classList.toggle('hidden')
    

})



