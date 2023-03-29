import os
import csv

def agendaexiste():
    caminho_agenda = os.path.abspath("contatos.csv")
    return os.path.exists(caminho_agenda):

def checarContato(dic, nome_lista):
    try:
        c = 0
        c_lista = []
        contatos_lista = list(dic.keys())
        if len(nome_lista) == 1:
            for nome in contatos_lista:
                if nome == nome_lista:
                    c += 1
                    c_lista.append(nome)
            if c > 1:
                return c_lista
            elif c == 1:
                return dic[nome_lista[0]]
            elif c == 0:
                return 0
        else:
            nome_lista = " ".join(nome_lista)
            for nome in contatos_lista:
                if nome == nome_lista:
                    c += 1
                    c_lista.append(nome)
            if c == 1:
                return dic[nome_lista]
            elif c > 1:
                return c_lista
            elif c == 0:
                nome_lista = nome_lista.split(" ")
                checarContato(dic, nome_lista[:-1])

    except KeyError:
        return 0


def buscarContato(dic):
    try:
        while True:
            nome = input("NOME: ").upper().strip()
            if nome == "":
                raise ValueError("ENTRE UM NOME NÃO NULO.")
            n_l = nome.split(" ")
            tel = checarContato(dic, n_l)
            if tel != 0:
                if isinstance(tel, list):
                    print("\nCONTATOS ENCONTRADOS:")
                    for contato in tel:
                        print(f"{contato} - {dic[contato]}")
                else:
                    print("\nCONTATO ENCONTRADO:")
                    print(f"{nome} - {tel}")
            else:
                print("\nNENHUM CONTATO ENCONTRADO.")
            op = int(input("BUSCAR MAIS ALGUM CONTATO? 1- SIM/ 2- NÃO."))
            if op != 1 and op != 2:
                raise ValueError("OPÇÃO INVÁLIDA.")
            elif op == 2:
                break
    except KeyError:
        print("NENHUM CONTATO ENCONTRADO.")
    except ValueError as e:
        print(f"ERRO: {e}")

def adicionarContato(dic):
    try:
        while True:
            nome = input("NOME: ").upper().strip()
            telefone = input("TELEFONE: ").strip()
            if nome == "" or telefone == ""
                raise ValueError("ENTRE UM NOME/TELEFONE NÃO NULO.")
            with open("contatos.csv", "a") as agenda:
                agenda.write(f"{nome},{telefone}\n")
            dic[nome] = telefone
    except ValueError as e:
        print(f"ERRO: {e}")
    else:
        print("CONTATO ADICIONADO.")

def mostrarLista(dic):
    lista_contatos = list(dic.keys())
    for contato in lista_contatos:
        if contato == EMPTY:
            continue
        print(f"{contato} - {dic[contato]}")

while True:
    try:
        if not agendaexiste():
            with open("contatos.csv", "w") as agenda:
                agenda.write("NOME,TELEFONE\n")
                agenda.write("EMPTY,0\n")

        dic_contatos = {}
        with open("contatos.csv", "r") as agenda:
            reader = csv.DictReader(agenda)
            for row in reader:
                if row['NOME'] == "EMPTY" and row['TELEFONE'] == "0":
                    dic_contatos = {"VAZIO": "0"}
                else:
                    dic_contatos[row['NOME']] = row['TELEFONE']

        print("""MENU
            1 - BUSCAR CONTATO
            2 - ADICIONAR CONTATO
            3 - ALTERAR/REMOVER CONTATO
            4 - VER LISTA DE CONTATOS
            5 - SAIR
            """)
        op = int(input("ENTRE UMA OPÇÃO: "))
        if op < 1 or op > 5:
            raise ValueError("ESCOLHA UMA OPÇÃO VÁLIDA (1 a 5).")
        if op == 5:
            break
        elif op == 1:
            buscarContato(dic_contatos)
        elif op == 2:
            adicionarContato(dic_contatos)
        elif op == 3:
            alterarContato()
        elif op == 4:
            mostrarLista(dic_contatos)

except KeyError:
    print("CONTATO NÃO EXISTE")
