CREATE DATABASE IF NOT EXISTS bds_usuarios;
USE bds_usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(255) NOT NULL,
    pwrd VARCHAR(255) NOT NULL,
    tipo_usuario VARCHAR(20) NOT NULL DEFAULT 'user'
);


--update utilizado para trocar o tipo de usuario para admin ou user

--USE bds_usuarios;
--UPDATE usuarios
--SET tipo_usuario = 'user'  --altera aqui (user, admin)
--WHERE id_usuario = 2;
