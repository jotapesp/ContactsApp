import os
import csv

## essa linha não deve existir

def agendaexiste():
    caminho_agenda = os.path.abspath("contatos.csv")
    return os.path.exists(caminho_agenda)

def checarContato(dic, nome_lista):
    try:
        qn = 0
        maior = 0
        #nome_maior_i = 0
        c_lista = []
        contatos_lista = list(dic.keys())
        nome_s = " ".join(nome_lista)
        for contato in contatos_lista:
            if contato == nome_s:
                return dic[contato]
            else:
                contato_lista = contato.split(" ")
                for i in range(len(nome_lista)):
                    qn = 0
                    for j in range(len(contato_lista)):
                        if nome_lista[i] == contato_lista[j]:
                            qn += 1
                    if qn > maior:
                        #nome_maior_i = j
                        if len(c_lista) > 0:
                            c_lista = []
                            c = 0
                        maior = qn
                        c_lista.append(contato)
                    if qn == maior and maior != 0:
                        if contato not in c_lista:
                            c_lista.append(contato)
        if len(c_lista) == 1:
            return dic[c_lista[0]]
        elif len(c_lista) > 1:
            return c_lista
        elif len(c_lista) == 0:
            return 0

        # if len(nome_lista) == 1:
        #     for i in range(len(contatos_lista)):
        #         contatos_na_lista = contatos_lista[i].split(" ")
        #         for j in range(len(contatos_na_lista)):
        #             if contatos_na_lista[j] == nome_lista[0]:
        #                 c += 1
        #                 c_lista.append(contatos_lista[i])
        #     if c > 1:
        #         print("retornar lista")
        #         return c_lista
        #     elif c == 1:
        #         return dic[c_lista[0]]
        #     elif c == 0:
        #         return 0
        # else:
        #     nome_lista = " ".join(nome_lista)
        #     for nome in contatos_lista:
        #         if nome == nome_lista:
        #             c += 1
        #             c_lista.append(nome)
        #     if c == 1:
        #         return dic[nome_lista]
        #     elif c > 1:
        #         return c_lista
        #     elif c == 0:
        #         nome_lista = nome_lista.split(" ")
        #         checarContato(dic, nome_lista[:-1])

    except KeyError:
        return 0


def buscarContato(dic):
    while True:
        try:
            nome = input("NOME: ").upper().strip()
            if nome == "":
                raise ValueError("ENTRE UM NOME NÃO NULO.")
            espaco = 0
            for i in range(len(nome)):
                if nome[i] == (" "):
                    espaco += 1
            if espaco > 0:
                n_l = nome.split(" ")
            else:
                n_l = [nome]
            tel = checarContato(dic, n_l)
            if tel != 0:
                if isinstance(tel, list):
                    print("\nCONTATOS ENCONTRADOS:")
                    print()
                    print("NOME".ljust(29, " "), end="-")
                    print("TELEFONE".rjust(15, " "))
                    print("-"*45)
                    for contato in tel:
                        if len(contato) > 28:
                            contato_curto = contato[:29]
                            print(f"{contato_curto}".ljust(29," "), end ="-")
                        else:
                            print(f"{contato}".ljust(29," "), end ="-")
                        print(f"{dic[contato]}".rjust(15, " "))
                        # print(f"{contato} - {dic[contato]}")
                    print()
                else:
                    print("\nCONTATO ENCONTRADO:")
                    print()
                    print("NOME".ljust(29, " "), end="-")
                    print("TELEFONE".rjust(15, " "))
                    print("-"*45)
                    nomes = list(dic.keys())
                    for nom in nomes:
                        if dic[nom] == tel:
                            nome = nom
                    if len(nome) > 28:
                        contato_curto = nome[:29]
                        print(f"{contato_curto}".ljust(29," "), end ="-")
                    else:
                        print(f"{nome}".ljust(29," "), end ="-")
                    print(f"{tel}".rjust(15, " "))
                    # print(f"{nome} - {tel}")
                    print()
            else:
                print("\nNENHUM CONTATO ENCONTRADO.")
            op = int(input("BUSCAR MAIS ALGUM CONTATO? 1- SIM/ 2- NÃO_"))
            if op != 1 and op != 2:
                raise ValueError("OPÇÃO INVÁLIDA.")
            elif op == 2:
                break
        except KeyError:
            print("NENHUM CONTATO ENCONTRADO.")
        except ValueError as e:
            print(f"ERRO: {e}")

def adicionarContato(dic):
    while True:
        try:
            nome = input("NOME: ").upper().strip()
            telefone = input("TELEFONE: ").strip()
            if nome == "" or telefone == "":
                raise ValueError("ENTRE UM NOME/TELEFONE NÃO NULO.")
            with open("contatos.csv", "a") as agenda:
                agenda.write(f"{nome},{telefone}\n")
            dic[nome] = telefone
            op = int(input("ADICIONAR MAIS ALGUM CONTATO? 1- SIM/ 2- NÃO_"))
            if op != 1 and op != 2:
                raise ValueError("OPÇÃO INVÁLIDA.")
            elif op == 2:
                break
        except ValueError as e:
            print(f"ERRO: {e}")

def mostrarLista(dic):
    lista_contatos = list(dic.keys())
    lista_contatos.sort()
    print()
    print("NOME".ljust(29, " "), end="-")
    print("TELEFONE".rjust(15, " "))
    print("-"*45)
    for contato in lista_contatos:
        if contato == "VAZIO":
            continue
        if len(contato) > 28:
            contato_curto = contato[:29]
            print(f"{contato_curto}".ljust(29," "), end ="-")
        else:
            print(f"{contato}".ljust(29," "), end ="-")
        print(f"{dic[contato]}".rjust(15, " "))

    print()

def alterarContato(dic):
    while True:
        try:
            nome = input("NOME DO CONTATO A ALTERAR: ").strip().upper()
            if nome == "":
                raise ValueError("ENTRE UM NOME NÃO NULO.")
            espaco = 0
            for i in range(len(nome)):
                if nome[i] == (" "):
                    espaco += 1
            if espaco > 0:
                n_l = nome.split(" ")
            else:
                n_l = [nome]
            tel = checarContato(dic, n_l)
            if tel != 0:
                if isinstance(tel, list):
                    print("\nCONTATOS ENCONTRADOS:")
                    print()
                    for i in range(len(tel)):
                        print(f"{i}-{tel[i]} - {dic[tel[i]]}")
                    print()
                    op1 = int(input(f"ENTRE A OPÇÃO EQUIVALENTE AO CONTATO A ALTERAR (0 a {len(tel) - 1}): "))
                    if op1 > len(tel) and op1 < 0:
                        raise ValueError("OPÇÃO INVÁLIDA.")
                    else:
                        print("""QUAL TIPO DE ALTERAÇÃO DESEJA REALIZAR?

                1 - ALTERAR NOME/TELEFONE
                2 - APAGAR CONTATO
                3 - VOLTAR
                """)
                        op2 = int(input("OPÇÃO: "))
                        if op2 < 1 and op > 3:
                            raise ValueError("OPÇÃO INVÁLIDA.")
                        elif op2 == 3:
                            break
                        elif op2 == 1:
                            novo_nome = input("NOVO NOME: ").strip().upper()
                            if novo_nome == "":
                                raise ValueError("ENTRE UM NOME NÃO NULO.")
                            novo_tel = input("NOVO TELEFONE: ").strip()
                            if novo_tel == "":
                                raise ValueError("ENTRE UM NÚMERO NÃO NULO.")
                            dic.pop(tel[op1])
                            dic[novo_nome] = novo_tel
                            with open("contatos.csv", "w") as agenda:
                                lista = list(dic.keys())
                                agenda.write("NOME,TELEFONE\n")
                                agenda.write("EMPTY,0\n")
                                for n in lista:
                                    if n != "VAZIO":
                                        agenda.write(f"{n},{dic[n]}\n")
                            break
                        elif op2 == 2:
                            dic.pop(tel[op1])
                            with open("contatos.csv", "w") as agenda:
                                lista = list(dic.keys())
                                agenda.write("NOME,TELEFONE\n")
                                agenda.write("EMPTY,0\n")
                                for n in lista:
                                    if n != "VAZIO":
                                        agenda.write(f"{n},{dic[n]}\n")
                            break
                else:
                    print("\nCONTATO ENCONTRADO:")
                    print("\nNOME               - TELEFONE     ")
                    print("-"*33)
                    nomes = list(dic.keys())
                    for nom in nomes:
                        if dic[nom] == tel:
                            nome = nom
                    print(f"{nome} - {tel}")
                    print()
            else:
                print("\nNENHUM CONTATO ENCONTRADO.")

        except Exception as e:
            print(f"ERRO: {e}")


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

        print("""\n           MENU
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
            alterarContato(dic_contatos)
        elif op == 4:
            mostrarLista(dic_contatos)

    except KeyError:
        print("CONTATO NÃO EXISTE")
