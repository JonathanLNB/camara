function validar() {
    const Usuarios=['alan','jona','chipo'];
    const Contraseñas=['12345','54321','abcde'];
    user=document.getElementById('first_name').value;
    console.log(user);
    pwd=document.getElementById('password').value;
    console.log(pwd);
   if(Usuarios.includes(user) && Contraseñas.includes(pwd))
       location.href='./camara.html';
    else
        alert("Usuario o contraseña incorrectos");
}