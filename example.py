import sqlite3 #importando o banco de dados nativo 

#criando uma conexao 
conexao = sqlite3.connect("alunos.db")

#criando as tabelas
conexao.execute('''CREATE TABLE IF NOT EXISTS planilha
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOT NULL);''')

#OPERAÇÃO CRUD
def criar_aluno(nome,idade):
    conexao.execute("INSERT INTO planilha (nome,idade) VALUES (?,?);", (nome,idade))        #evitar SQL injections
    conexao.commit()
    print("Aluno inserido com sucesso")

def listar_alunos():
    alunos = conexao.execute("SELECT * FROM planilha;")
    for aluno in alunos:
        print(aluno)

def atualizar_aluno(id, novo_nome, nova_idade):
    conexao.execute("UPDATE planilha SET nome = ?, idade = ? WHERE id = ?;", (novo_nome, nova_idade,id))
    conexao.commit()
    print("Aluno atualizado com sucesso.")

def remover_aluno(id):
    conexao.execute("DELETE FROM planilha WHERE id = ?;", (id,))
    conexao.commit()
    print("Aluno removido com sucesso")

listar_alunos()
criar_aluno("Eduardo", 19)
criar_aluno("Richard", 20)
criar_aluno("Yan", 20)
listar_alunos()
remover_aluno(1)
listar_alunos()
atualizar_aluno(2, "Gabriel",20)
listar_alunos()