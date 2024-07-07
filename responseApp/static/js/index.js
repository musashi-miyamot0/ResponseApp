const logoutButton = document.querySelector('.logout')
const modelLogout = document.querySelector('.modalWindow')
const No = document.querySelector('.no')

logoutButton.addEventListener('click',()=>{
    modelLogout.style.display = 'grid'

})

No.addEventListener('click',()=>{
    modelLogout.style.display = 'none'
})




