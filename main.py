from aluno import *

alunos = []

joao = Aluno()
joao.matricula = '0001'
joao.nome = 'João'

pedro = Aluno()
pedro.matricula = '0002'
pedro.nome = 'Pedro'

alunos.append(joao)
alunos.append(pedro)

#------------------------------------------------------------------

def listar_alunos():
    print('Listagem de Alunos:')
    for a in alunos:
        print(a)
    print()

#----------------------------------------------------------------

def cadastrar_aluno():
    print('Cadastro de um novo aluno:')
    matricula = input('Matrícula: ')
    nome = input('Nome: ')

    novo = Aluno()
    novo.matricula = matricula
    novo.nome = nome

    alunos.append(novo)

#------------------------------------------------------------------

def excluir_aluno():
    print('Exclusão de Aluno:')
    matricula = input('Digite a matrícula do aluno:')

    for aluno in alunos:
        if aluno.matricula == matricula:
            alunos.remove(aluno)
            print('Aluno removido com sucesso')
            print()
            return

    print('Aluno não encontrado')
    print()

#------------------------------------------------------------------

while True:
    print('Menu Principal')
    print('1 - Listar alunos')
    print('2 - Cadastrar aluno')
    print('3 - Excluir aluno')
    print('0 - Sair')
    opcao = input('Opção: ')
    print()

    if opcao == '0':
        exit(0)
    elif opcao == '1':
        listar_alunos()
    elif opcao == '2':
        cadastrar_aluno()
    elif opcao == '3':
       excluir_aluno()
