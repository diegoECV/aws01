CREATE DATABASE sistema_ventas;

USE sistema_ventas;

-- 1. Tabla de Usuarios para el Login
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Insertamos un usuario de prueba (Usuario: admin, Clave: 123456)
INSERT INTO usuarios (username, password) VALUES ('admin', '123456');

-- 2. Tabla de Clientes para el CRUD
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni_ruc VARCHAR(15) NOT NULL,
    nombres VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100),
    direccion TEXT,
    estado TINYINT DEFAULT 1 -- Por defecto se crean como "Activos"
);