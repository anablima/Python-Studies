'''
Antes de qualquer coisa, vamos pensar no problema que vamos resolver!

Quero criar um programa que leia um arquivo .html com anotações de livros, 
armazene esses dados em uma arquvio .csv e apresente as anotações em formato tabular.

Let's go Baby!

Arquivo de teste:
/mnt/c/Users/014061631/Documents/Scrum - a arte de fazer o dobro de trabalho na metade do tempo - Notebook.html
'''

# Importando as bibliotecas
import pandas as pd
import os 

# Futuros ajustes no bloco de código abaixo
'''
    1. Inserir tratamento do arquivo recebido caso não seja inserido a extensão.
    2. Inserir msg de erro caso o caminho do arquivo contenha algum erro e não
    seja possível localizar o arquivo no computador.
'''

# Solicitando o local com o nome do arquivo
print('Insira o local e nome do arquivo .html: ')    
caminho = str(input("> "))

# Lendo e armazendo os dados em formato tabular
arq = str("'", caminho, "'")
tratahtml = pd.read_html(arq)
tratahtml

'''
div class usadas pra criar a tabela

sectionHeading -> Capítulo
noteHeading -> Posição da anotação
noteText -> Texto anotado


'''