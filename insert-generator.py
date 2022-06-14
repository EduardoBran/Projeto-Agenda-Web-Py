# from datetime import datetime
# import time
# import random
#
# ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in range(16, 200):  # Presume que você só usou os ids 1 ao 13 pois começa do 3
#     id = i
#     nome = ''.join(random.choices(ALPHABET, k=6))  # Gera nomes de tamanho 6
#     sobrenome = ''.join(random.choices(ALPHABET, k=6))  # Gera sobrenomes de tamanho 6
#     num_registro = str(i).zfill(3)
#     tres_ultimos_digitos = num_registro
#     telefone = f'31999999{tres_ultimos_digitos}'
#     email = f'{nome}@gmail.com'
#     data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     categoria_id = random.randint(1, 3)  # Estou presumindo a existência de 3 categorias
#
#     print(f"INSERT INTO contatos_contato"
#           f" (id, nome, sobrenome, telefone, email, data_criacao, descricao, categoria_id)"
#           f" VALUES ('{id}', '{nome}', '{sobrenome}', '{telefone}', '{email}',"
#           f" '{data_criacao}', 'descricao{num_registro}', '{categoria_id}');")
#
#     # time.sleep(0.5)


"""
É só executar esse script e jogar a saída para um arquivo:

Ir ao terminal e digitar:
python insert-generator.py > inserts.sql

Abrir o DB Browser e mudar da aba "Estrutura do banco de dados" para a aba "Executar SQL" e daí
carregar esse arquivo inserts.sql e clicar no botão de play para rodar todas as queries.

Abrir o SqliteStudio, abrir o banco de dados usado, abrir a aba OPEN SQL & Editor (alt + E),
clicar em load sql for file , abrir o arquivo, SELECIONAR TODOS e apertar play.
"""




from random import *
import sqlite3
from datetime import datetime

connection = sqlite3.connect('generator.db')
cursor = connection.cursor()

nomes = 'Miguel Arthur Heitor Bernardo Davi Gabriel Pedro Samuel Lorenzo Benjamin Matheus Lucas Gabriela Julia Maria Larissa Leticia Guilherme Murilo Lucca Gustavo João Miguel Noah Felipe Anthony Enzo João Pedro Pietro Bryan Daniel Pedro Henrique Enzo Gabriel Leonardo Vicente Valentim Eduardo Antônio  Emanuel Davi Lucca João João Lucas'
nomes = nomes.split()
sobrenomes = 'Abbott Abernathy Adair Adams Adkins Aguirre Alexander Allen Allison Almeida Alvarado Alvarez Andersen Anderson Anderson Andrews Archer Armstrong Arnold Arsenault Ashby Ashworth Atkinson Austin Ayers Fagan Fallon Fanning Farley Farrell Faulkner Ferguson Fernandez Figueroa Finch Finn Finnegan Fischer Fisher Fitch Fitzgerald Fitzpatrick Fitzsimmons Flanagan Fletcher Flood Flores Floyd Flynn Forbes Ford Forsyth Foster Fournier Fowler Fox Franklin Fraser Frazier Freeman Frost Fry Fuller'
sobrenomes = sobrenomes.split()
for i in range(1, 30):
    id = i
    nome = choice(nomes)
    sobrenome = choice(sobrenomes)
    email = nome+'@gmail.com'
    data_criacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    descricao = 'Gerado a partir de um script.'
    categoria_id = randint(1, 3) #Supondo que você tem 3 categorias, caso não, só alterar o segundo valor.
    telefone = str(randint(888888888, 999999999))


    print(f"INSERT INTO contatos_contato"
          f" (id, nome, sobrenome, email, data_criacao, descricao, categoria_id, telefone)"
          f" VALUES ('{id}', '{nome}', '{sobrenome}', '{email}', '{data_criacao}', '{descricao}', '{categoria_id}', '{telefone}');")

connection.commit()

cursor.close()
connection.close()

