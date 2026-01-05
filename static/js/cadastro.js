const form = document.querySelector('form');

form.addEventListener('submit', function (e) {
    e.preventDefault();

    //pegando valores do meu formulario
    const user = document.getElementById('user').value;
    const password = document.getElementById('password').value;

    //fetch utilizado para mandar os dados para a rota correta do meu flask
    fetch('/api/usuarios', { //minha rota no flask
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `user=${encodeURIComponent(user)}&password=${encodeURIComponent(password)}`
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert(data.mensagem || data.erro);
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});
