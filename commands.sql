#01 Inicializar o BDR mariaDB (antigo MySQL)
# mysql -u root

#02 Verificar se o mariaDB está funcionando
show databases;

#03 Criar um banco de dados com o nome que desejar
create database sgdb;

#04 Usar o banco criado
use sgdb;

#05 Criar tabela
create table product(
code int not null,
name varchar(50) not null,
description varchar(150) not null,
price float not null,
primary key(code));

#06 Verificar a estrutura da tabela criada
desc product;