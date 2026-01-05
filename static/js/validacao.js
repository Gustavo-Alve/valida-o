const form = document.querySelector('form');

form.addEventListener('submit', function (e) {
    e.preventDefault();

    const user = document.getElementById('user').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `user=${encodeURIComponent(user)}&password=${encodeURIComponent(password)}`
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === 'ok') {
            if (data.tipo === 'admin') {
                window.location.href = '/admin';
            } else {
                window.location.href = '/user';
            }
        } else {
            alert("Usuário ou senha incorretos");
        }
    })
    .catch(err => {
        console.error(err);
        alert("Erro no servidor");
    });
});
