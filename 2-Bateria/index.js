function sonar_animar(boton){
    let nombre = getComputedStyle(boton).backgroundImage;
    nombre = nombre.split('/').slice(-1)[0].split('.')[0];

    console.log(nombre);

    let audio = new Audio(`./sonidos/${nombre}.mp3`);
    audio.play();

    boton.classList.add('presionado')
    setTimeout(()=>{
        boton.classList.remove('presionado')
    }, 150)
}

let botones = document.querySelectorAll('button')

botones.forEach(element => {
    element.addEventListener('click', function() {
        sonar_animar(this);
    })
});

document.addEventListener('keyup', tecla =>{
    key = tecla.key

    botones.forEach(boton => {
        if(key == boton.innerHTML){
            sonar_animar(boton)
        }
    })

})
