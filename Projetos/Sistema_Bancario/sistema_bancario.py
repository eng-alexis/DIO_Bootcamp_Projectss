#PROJETO SISTEMA BANCARIO SIMPLES

from datetime import datetime, time, date

#Variaveis
saldo_atual     = 0
transacoes_dia  = 0
hora_atual      = datetime.now()

qtd_depositos   = 0
total_depositos = 0
lista_depositos = []
data_hora_depos = []

qtd_saques      = 0
total_saques    = 0
lista_saques    = []
data_hora_saque = []


#Tela Inicial

while True:
    print('''          
          MENU PRINCIPAL
                                     
          Escolha uma Opção Abaixo: 
                                     
          1 - Depositar             
          2 - Sacar                  
          3 - Extrato                
          4 - Sair                   
          __________________________
    
                                       ''')
    try:
        opcao = int(input("Digite a opção desejada:"))
    except ValueError:
        print("\nOpção Invalida! \nDigite um numero de 1 a 4")
        continue
    
    #Atualização e verificação de qtde de transações diarias
       
    if hora_atual.hour == 9 and hora_atual.minute == 55:
         transacoes_dia = 0

    if  transacoes_dia == 10:
        print(f"\nLimite de transações diarias atingido!\nTente novamente amanha!")
        break
    else:
    
            #Operação_Bancaria (Deposito) 
    
            if opcao == 1:
                
                deposito = float(input("Digite o valor a ser depositado: R$ "))
                
                if deposito < 0:
                    print("\nValor Invalido! \nDigite apenas valores superiores a R$ 0,00")
                else:
                    transacoes_dia  += 1
                    saldo_atual     += deposito
                    qtd_depositos   += 1
                    total_depositos += deposito
                    data_hora_depos.append(datetime.now())
                    lista_depositos.append(deposito)
                    print(f"\nValor de R$ {deposito:.2f} depositado com sucesso")
                    print(f"Transações disponiveis: {10 - transacoes_dia}")
           
            
            #Operação_Bancaria (Saque)  
                    
            elif opcao == 2:
                
                if qtd_saques >= 3:
                    print("\nOperação Invalida! \nLimite de saques diarios atingido")
                
                else: 
                    valor_saque = float(input("Digite o Valor de Saque desejado: R$ "))
                    
                    if valor_saque < 0:
                        print("\nValor Invalido! \nSaques permitidos para valores acima de R$ 0,00")
                    elif valor_saque > 500:
                        print("\nValor Invalido! \nLimite de R$ 500,00 por saque")    
                    elif valor_saque > saldo_atual:
                        print("\nOperação Invalida! \nSaldo indisponivel")
                    else:
                        transacoes_dia  += 1
                        saldo_atual   = saldo_atual - valor_saque
                        qtd_saques   += 1
                        total_saques += valor_saque
                        lista_saques.append(valor_saque)
                        data_hora_saque.append(datetime.now())
                        print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")
                        print(f"Transações disponiveis: {10 - transacoes_dia}")
            
            #Operação_Bancaria (Ver Extrato Bancario)  
            
            elif opcao == 3:
                
                if qtd_depositos == 0 and qtd_saques == 0:
                    print("\nNão foram realizadas movimentações na conta")
                else:
                    print(f'''          
                        EXTRATO BANCARIO
                        
                        DEPOSITOS_________________________                           
                        Qtd.Depositos :       {qtd_depositos} 
                        Total Depositado : R$ {total_depositos:.2f}    
                        
                        SAQUES____________________________
                        Qtd.Saques :          {qtd_saques}
                        Total Sacado:      R$ {total_saques:.2f}
                        
                        SALDO_____________________________
                        Saldo Atual :      R$ {saldo_atual:.2f}                                                                
                        ''')
                
            #Lista de Depositos e Saques
                
                    print('''
                        LISTA DE DEPOSITOS________________
                        ''')
                    for valor_d, horario_d in zip(lista_depositos, data_hora_depos):
                        print(f'''                        Valor: +R$ {valor_d:.2f} | Data: {horario_d.strftime('%d/%m/%Y - %H:%M')}''')
                        
                    print('''1
                        LISTA DE SAQUES___________________
                        ''')
                    for valor_s, horario_s in zip(lista_saques, data_hora_saque):
                        print(f'''                        Valor: +R$ {valor_s:.2f} | Data: {horario_s.strftime('%d/%m/%Y - %H:%M')}''')
                    
            #Sair do programa
            
            elif opcao == 4:
                print("\nObrigado por utilizar nosso sistema bancario, até logo!")
                break
            
            else:
                print("\nOpção invalida!\nEscolha entre as seguinte opções: 1,2,3 e 4")
