import sqlite3

#conectexao com o db
conn = sqlite3.connect('neabi.db')

#cria um cursor para interagir com o banco de dados
cursor = conn.cursor()

#Cria uma tabela tipos de usuarios
cursor.execute('''
    create table tipos_usuarios (
               id INT auto_increment primary key, 
               nome varchar(30) not null, 
               descricao varchar(50) not null
               );
''')

#Cria uma tabela tipos de denuncia
cursor.execute('''
    create table tipos_denuncias (
               id int auto_increment primary key, 
               nome varchar(50) not null, 
               descricao text, 
               prioridade int not null
               );
''')

#Cria uma tabela de status da denuncia
cursor.execute('''
    create table status_denuncias (
               id int auto_increment primary key, 
               status varchar(50) not null
               );
''')

#Cria uma tabela de usuarios
cursor.execute('''
    create table usuarios (
               id int auto_increment primary key, 
               nome varchar(90) not null, 
               matricula varchar(14) unique, 
               telefone varchar(8), 
               senha_hash varchar(200), 
               tipo_usuario_id int, foreign key (tipo_usuario_id) references tipos_usuarios(id)
               );
''')

#Cria uma tabela de denuncia
cursor.execute('''
    create table denuncias (
               id int auto_increment primary key, 
               usuario_id int, 
               tipo_denuncia_id int, 
               status_denuncia_id int, 
               denuncia text not null, 
               data_denuncia date, 
               foreign key (usuario_id) references usuarios(id), 
               foreign key (tipo_denuncia_id) references tipos_denuncias(id), 
               foreign key (status_denuncia_id) references status_denuncias(id)
               );
''')

#Cria uma tabela permissao de vizualização
cursor.execute('''
    create table permissao_visualizacao(
               id int auto_increment primary key, 
               tipo_usuario_id int, 
               denuncia_id int, 
               foreign key (tipo_usuario_id) references tipos_usuarios(id), 
               foreign key (denuncia_id) references denuncias(id)
               );
''')


# Salva as mudanças e fecha a conexão
conn.commit()
conn.close()
