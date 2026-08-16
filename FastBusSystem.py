#PROJETO DE ENG. SW.
#GRUPO: Felipe Marinho Rocha, Alexandre Alves, Wesley dos Reis, Danilo Gomes
from time import sleep
def menu():
    print(f'''{'='*25}
{'FAST BUS SYSTEM':^25}
{'='*25}''')
def listagem():
    print()
    print(f'Nº  {'Nome do passageiro':<20}{'Meio de pagamento':<18} Valor total da passagem')
    print()
    for c in range(len(lista)):
        print(f'{c}   {str(lista[c][0]):<20}{str(lista[c][1]):<18} R${lista[c][2]:.2f}')
        sleep(0.7)
    print()
    print()
opção='-1'
lista=[]
lista1=[]
r='\033[31m'
g='\033[32m'
e='\033[m'
while opção!='0':
    menu()
    print(f'''[ 1 ] Registrar novo pagamento
[ 2 ] Registro geral
[ 3 ] Remover registros
[ 4 ] Atualizar registros
[ 5 ] Buscar registros
[ 0 ] Sair
{'='*25}''')
    opção=input('Digite sua opção: ').strip()
    if opção=='0':
        print(f'\nEncerrando FAST BUS SYSTEM...\n')
        sleep(3)
        print(f'{r}FAST BUS SYSTEM encerrado com sucesso{e}\n')
    elif opção=='1':
        opção1='-1'
        print()
        lista1.append(input('Nome do passageiro: '))
        while opção1 not in ['0','1','2']:
            menu()
            print('''[ 0 ] Pix
[ 1 ] Cartão de débito
[ 2 ] Cartão de crédito
''')
            opção1=input('Digite qual foi o meio de pagamento de acordo com a numeração exibida: ').strip()
            if opção1 in ['0','1','2']:
                meio='Pix','Cartão de débito','Cartão de crédito'
                lista1.append(meio[int(opção1)])
                valor=float(input('Valor da passagem: R$'))
                passe='0'
                while passe not in ['S','SIM','NAO','N']:
                    passe=input('Possui passe estudantil[S/N]: ').strip().upper()
                    if passe in ['S','SIM']:
                        valor=valor/2
                        lista1.append(valor)
                        lista1.append('Sim')
                    elif passe in ['N','NAO']:
                        lista1.append(valor)
                        lista1.append('Não')
                    else:
                        print(f'\n{r}Entrada inválida, tente novamente{e}\n')
                        sleep(3)
                lista.append(lista1[:])
                lista1.clear()
                print('\nSalvando registro...')
                sleep(1)
                print(f'\n{g}Registro salvo com sucesso{e}\n')
            else:
                print(f'\n{r}Entrada inválida, tente novamente{e}\n')
                sleep(1)
    elif opção=='2':
        if lista==[]:
            print(f'\n{r}Não há nenhum registro ainda{e}\n')
            sleep(3)
        else:
            opção4=0
            while opção4>-1:
                listagem()
                opção4=int(input('Digite um Nº correspondente á tabela para visualizar o registro individual de um passageiro [digite um Nº negativo para sair da operação]: '))
                if opção4>=len(lista):
                    print(f'\n{r}Entrada inválida, tente novamente{e}\n')
                    sleep(3)
                elif 0<=opção4<len(lista):
                    dic={}
                    dic['Nome do passageiro']=lista[opção4][0]
                    dic['Meio de pagamento']=lista[opção4][1]
                    dic['Possui passe estudantil']=lista[opção4][3]
                    if lista[opção4][3]=='Sim':
                        dic['Valor inteiro da passagem']=(f'R${lista[opção4][2]*2:.2f}')
                        dic['Valor abatido na passagem']=(f'50% = R${lista[opção4][2]:.2f}')
                        dic['Valor total da passagem']=(f'R${lista[opção4][2]:.2f}')
                    else:
                        dic['Valor inteiro da passagem']=(f'R${lista[opção4][2]:.2f}')
                        dic['Valor abatido na passagem']=(f'0% = R$0.00')
                        dic['Valor total da passagem']=(f'R${lista[opção4][2]:.2f}')
                    print()
                    for k,v in dic.items():
                        print(f'{k}: {v}')
                        sleep(0.7)
                    print()
                    dic.clear()
                    sleep(3)
                else:
                    print(f'\n{r}Encerrando operação de visualização de registro...{e}\n')    
            sleep(3)
    elif opção=='3':
        if lista==[]:
            print(f'\n{r}Não há nenhum registro para ser removido ainda{e}\n')
            sleep(3)
        else:
            opção2=0
            while opção2>-1:
                listagem()
                opção2=int(input('Digite um Nº correspondente à tabela para remover determinado registro [digite um Nº negativo para sair da operação]: '))
                if opção2>=len(lista):
                    print(f'\n{r}Entrada inválida, tente novamente{e}\n')
                    sleep(3)
                elif 0<=opção2<len(lista):
                    lista.pop(opção2)
                    print(f'\n{g}Operação de remoção do registro de Nº{opção2} bem sucedida{e}\n')
                    sleep(1.5)
                    if lista==[]:
                        print(f'{r}Todos os registros foram removidos{e}\n')
                        opção2=-1
                        sleep(1.5)
                else:
                    print(f'\n{r}Encerrando operação de remoção...{e}\n')
                    sleep(3)
    elif opção=='4':
            opção3=0
            while opção3>-1:
                listagem()
                opção3=int(input('Digite um Nº correspondente à tabela para atualizar um registro [digite um Nº negativo para sair da operação]: '))
                if opção3>=len(lista):
                    print(f'\n{r}Entrada inválida, tente novamente{e}\n')
                    sleep(3)
                elif 0<=opção3<len(lista):
                    opção5=0
                    while opção5>-1:
                        print()
                        print(f'''[ 0 ] Nome: {lista[opção3][0]}
[ 1 ] Meio de pagamento: {lista[opção3][1]}
[ 2 ] Valor total da passagem: {lista[opção3][2]}
[ 3 ] Passe estudantil: {lista[opção3][3]}
''')
                        opção5=int(input('Digite sua opção de atualização dados de acordo com a numeração da tabela [Digite um valor negativo para encerrar a operação de atualização de dados]: '))
                        if opção5==0:                        
                            print()
                            lista[opção3][0]=input('Novo nome do passageiro: ')
                        elif opção5==1:
                            opção1='-1'
                            while opção1 not in ['0','1','2']:
                                menu()
                                print('''[ 0 ] Pix
[ 1 ] Cartão de débito
[ 2 ] Cartão de crédito
''')
                                opção1=input('Digite o novo meio de pagamento de acordo com a numeração exibida: ').strip()
                                if opção1 in ['0','1','2']:
                                    meio='Pix','Cartão de débito','Cartão de crédito'
                                    lista[opção3][1]=(meio[int(opção1)])
                                else:
                                    print(f'{r}Entrada inválida, tente novamente{e}')
                        elif opção5==2:
                            valor=float(input('Novo valor da passagem: R$'))
                            if lista[opção3][3]=='Sim':
                                valor/=2
                            lista[opção3][2]=valor
                        elif opção5==3:
                            if lista[opção3][3]=='Sim':
                                valor=lista[opção3][2]*2
                            passe='0'
                            while passe not in ['S','SIM','NAO','N']:
                                passe=input('possui passe estudantil[S/N]: ').strip().upper()
                                if passe in ['S','SIM']:
                                    valor=valor/2
                                    lista[opção3][2]=valor
                                    lista[opção3][3]='Sim'
                                elif passe in ['N','NAO']:
                                    lista[opção3][2]=valor
                                    lista[opção3][3]='Não'
                                else:
                                    print(f'\n{r}Entrada inválida, tente novamente{e}\n')
                                    sleep(3)
                        else:
                            print(f'\n{r}Encerrando operação de atualização...{e}\n')
                            sleep(3)
    elif opção=='5':
        opçãobusca=0
        while opçãobusca>-1:
            print()
            menu()
            print('''[ 0 ] Nome
[ 1 ] Meio de pagamento
[ 2 ] Passe estudantil
''')
            opçãobusca=int(input('Digite sua opção de busca de dados de acordo com a numeração da tabela [Digite um valor negativo para encerrar a operação de busca de dados]: '))
            if opçãobusca==0:
                buscanome=input('Digite o nome que deseja buscar: ')
                cont=0
                for c in range(len(lista)):
                    if buscanome in lista[c]:
                        cont+=1
                if cont==0:
                    print(f'\n{r}Nenhum resultado com o nome "{buscanome}" encontrado{e}\n')
                    sleep(3)
                else:
                    print(f'Nº  {'Nome do passageiro':<20}{'Meio de pagamento':<18} Valor total da passagem')
                    print()
                    for c in range(len(lista)):
                        if buscanome in lista[c]:
                            print(f'{c}   {str(lista[c][0]):<20}{str(lista[c][1]):<18} R${lista[c][2]:.2f}')
                            sleep(0.7)
                    sleep(3)
            elif opçãobusca==1:
                cont=0
                opção1='-1'
                while opção1 not in ['0','1','2']:
                    print('''[ 0 ] Pix
[ 1 ] Cartão de débito
[ 2 ] Cartão de crédito
''')
                    opção1=input('Digite qual será o meio de pagamento para a busca de acordo com a numeração exibida: ').strip()
                    if opção1=='0':
                        for c in range(len(lista)):
                            if 'Pix' in lista[c]:
                                cont+=1
                        if cont==0:
                            print(f'\n{r}Nenhum resultado com meio de pagamento "Pix" encontrado{e}\n')
                            sleep(3)
                        else:
                            print(f'Nº  {'Nome do passageiro':<20}{'Meio de pagamento':<18} Valor total da passagem')
                            print()
                            for c in range(len(lista)):
                                if 'Pix' in lista[c]:
                                    print(f'{c}   {str(lista[c][0]):<20}{str(lista[c][1]):<18} R${lista[c][2]:.2f}')
                                    sleep(0.7)
                            sleep(3)
                    elif opção1=='1':
                        for c in range(len(lista)):
                            if 'Cartão de débito' in lista[c]:
                                cont+=1
                        if cont==0:
                            print(f'\n{r}Nenhum resultado com meio de pagamento "Cartão de débito" encontrado{e}\n')
                            sleep(3)
                        else:
                            print(f'Nº  {'Nome do passageiro':<20}{'Meio de pagamento':<18} Valor total da passagem')
                            print()
                            for c in range(len(lista)):
                                if 'Cartão de débito' in lista[c]:
                                    print(f'{c}   {str(lista[c][0]):<20}{str(lista[c][1]):<18} R${lista[c][2]:.2f}')
                                    sleep(0.7)
                            sleep(3)
                    elif opção1=='2':
                        for c in range(len(lista)):
                            if 'Cartão de crédito' in lista[c]:
                                cont+=1
                        if cont==0:
                            print(f'\n{r}Nenhum resultado com meio de pagamento "Cartão de crédito" encontrado{e}\n')
                        else:
                            print(f'Nº  {'Nome do passageiro':<20}{'Meio de pagamento':<18} Valor total da passagem')
                            print()
                            for c in range(len(lista)):
                                if 'Cartão de crédito' in lista[c]:
                                    print(f'{c}   {str(lista[c][0]):<20}{str(lista[c][1]):<18} R${lista[c][2]:.2f}')
                                    sleep(0.7)
                            sleep(3)
                    else:
                        print(f'\n{r}Entrada inválida, tente novamente{e}\n')
                        sleep(3)
            elif opçãobusca==2:
                passebusca='2'
                while passebusca not in ['0','1']:
                    print(f'''[ 0 ] Com passe estudantil
[ 1 ] Sem passe estudantil
''')
                    passebusca=input(f'Digite qual será a situação do passe estudantil para a busca de acordo com a numeração exibida: ')
                    if passebusca=='0':
                        cont=0
                        for c in range(len(lista)):
                            if 'Sim' in lista[c]:
                                cont+=1
                        if cont==0:
                            print(f'\n{r}Nenhum resultado com passe estudantil encontrado{e}\n')
                            sleep(3)
                        else:
                            print(f'Nº  {'Nome do passageiro':<20}{'Meio de pagamento':<18} Valor total da passagem')
                            print()
                            for c in range(len(lista)):
                                if 'Sim' in lista[c]:
                                    print(f'{c}   {str(lista[c][0]):<20}{str(lista[c][1]):<18} R${lista[c][2]:.2f}')
                                    sleep(0.7)
                            sleep(3)
                    elif passebusca=='1':
                        cont=0
                        for c in range(len(lista)):
                            if 'Não' in lista[c]:
                                cont+=1
                        if cont==0:
                            print(f'\n{r}Nenhum resultado sem passe estudantil encontrado{e}\n')
                            sleep(3)
                        else:
                            print(f'Nº  {'Nome do passageiro':<20}{'Meio de pagamento':<18} Valor total da passagem')
                            print()
                            for c in range(len(lista)):
                                if 'Não' in lista[c]:
                                    print(f'{c}   {str(lista[c][0]):<20}{str(lista[c][1]):<18} R${lista[c][2]:.2f}')
                                    sleep(0.7)
                            sleep(3)
                    else:
                        print(f'\n{r}Entrada inválida, tente novamente{e}\n')
            elif opçãobusca<0:
                print(f'\n{r}Encerrando operação de busca...{e}\n')
            else:
                print(f'\n{r}Entrada inválida, tente novamente{e}')
    else:
        print(f'\n{r}Entrada inválida, tente novamente{e}\n')
        sleep(3)
#IMPLEMENTAÇÃO DE CÓDIGO by: Felipe Marinho Rocha
