import mysql.connector

conexao = mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='',
                                  database='conteiner')

cursor = conexao.cursor()