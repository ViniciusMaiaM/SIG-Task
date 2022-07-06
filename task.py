import calendar
import os
import datetime
import pickle  # biblioteca pra gravar o dicionario inteiro no arquivo

os.system('cls')  # clear so funcionar no linux, pra windows o comando é cls

#dicionario com os usuarios, vamos usar os integrantes do grupo como padrão

us = {

    "Lucas" : ["1234"],
    "Vinicius" : ["4321"]

}

arq = open('users.dat', 'wb')  # criando arquivo de usuários
pickle.dump(us, arq) # usar a função dump para passar tudo de um dicionario para o arquivo de uma vez só
arq.close()


# assim o programa funcionara pra qualquer ano, então é bom trabalhar sempre com datas variaveis
anomenu = datetime.datetime.now().year

print(f"O calendário do ano {anomenu} é:")
print(calendar.calendar(anomenu))

print('========================= ')
print('        SIG-Task          ')
print('========================= ')
print('  1 - Seleção de usuário  ')
print('  2 - Cadastrar usuário   ')
print('  3 - Atualizar usuário   ')
print('  4 - Deletar             ')
print('  0 - Sair                ')
esc1 = input('Escolha sua opção: ')

while esc1 != "0":

    if esc1 == "1":
        print("=== Seleção de usuário ===\n")
        try:
            arq = open("users.dat", "rb")
            us = pickle.load(arq)
            arq.close()
        except: 
            arq = open("users.dat", "wb")
            arq.close()

        for users in us:
            print(users)

        print("=== Em Desenvolvimento ===")

    elif esc1 == "2":

        print("=== Cadastro de usuário ===")
        nome = input('Insira seu nome: ')
        senha = input('Insira sua senha:')

        if us.get(nome):

            print('Usuário já existe', nome)
        else:

            us[nome] = senha
            arq = open('users.dat', 'wb')
            pickle.dump(us, arq) 
            arq.close()

        print("=== Em Desenvolvimento ===")
    elif esc1 == "3":

        print("===  Atualizar usuário   =")
        nome = input('Insira o nome usuário a se mudar:')
        if nome in us.keys():

            nome2 = input('Insira o novo nome: ')
            senha = input('Insira a nova senha: ')
            us[nome2] = senha
            del us[nome]
        else:

            print('Nome não encontrado!')

        print("=== Em Desenvolvimento ===")

    elif esc1 == "4":

        print("===   Função Deletar   ===")
        nome = input('Insira o usuário que será deletado:')
        if nome in us.keys():
            del us[nome]
        else:
            print("Usuário não encontrado")
    else:
        print("===   Opção Invalida   ===")
    input("Tecle ENTER para continuar")

    os.system('cls')  # cls no lugar de clear no windows

    print('========================= ')
    print('        SIG-Task          ')
    print('========================= ')
    print('  1 - Seleção de usuário  ')
    print('  2 - Cadastrar usuário   ')
    print('  3 - Atualizar usuário   ')
    print('  4 - Deletar             ')
    print('  0 - Sair                ')
    esc1 = input('Insira: ')
print("Fim")
print(us)
