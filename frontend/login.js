let from = document.getElementById('login-form')

from.addEventListener('submit', (e) =>{
    e.preventDefault()
    
    let fromData = {
        'username':from.username.value,
        'password':from.password.value
    }

    fetch('http://127.0.0.1:8000/api/users/token/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body: JSON.stringify(fromData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('DATA:',data.access)
        if(data.access){
            localStorage.setItem('token',data.access)
            window.location = 'file:///C:/Users/Rahul%20Jangir/Dropbox/Django%20by%20Dennis/frontend/projects-list.html'
        }else{
            alert('Username OR password did not work')
        }
    })
})