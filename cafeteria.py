# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# <description>
# Written in MySQL Workbench 8.0.32

import grt
#import mforms
CREATE SCHEMA coffeshop;
USE coffeshop;
CREATE TABLE productos(
  codigo INT NOT NULL AUTOINCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  cantidad INT NOT NULL,
  precio INT NOT NULL,
  id_cliente INT NOT NULL,
  id_proveedor INT NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES clientes(id),
  FOREIGN KEY (id_proveedor) REFERENCES proveedores(id)
);

CREATE TABLE clientes(
  id INT NOT NULL AUTOINCREMENT PRIMARY KEY,
  nombre VARCHAR(100) not NULL,
  rut INT NOT NULL,
  id_empleado INT NOT FULL,
  codigo_producto INT NOT FULL,
  FOREIGN KEY (id_empleado) REFERENCES empleados(id),
  FOREIGN KEY (codigo_producto) REFERENCES productos(codigo)
);
CREATE TABLE empleados(
  id INT NOT NULL AUTOINCREMENT PRIMARY KEY,
  salario INT NOT NULL,
  nombre VARCHAR(100) not NULL,
  direccion VARCHAR(100) not NULL,
  rut INT NOT NULL,
  id_cliente INT NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
CREATE TABLE proveedores(
  id_proveedor INT NOT NULL AUTOINCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  direccion VARCHAR(100) NOT NULL,
  rut INT NOT NULL,
  codigo_producto INT NOT FULL,
  FOREIGN KEY (codigo_producto) REFERENCES productos(codigo)
); 

