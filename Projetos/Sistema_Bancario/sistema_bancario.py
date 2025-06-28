#PROJETO SISTEMA BANCARIO SIMPLES

#Variaveis
saldo_atual     = 0
qtd_depositos   = 0
lista_depositos = []
total_depositos = 0
qtd_saques      = 0
lista_saques    = []
total_saques    = 0

#Tela Inicial

while True:
    print('''          
          MENU PRINCIPAL____________
                                     
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
        print("Opção Invalida! Digite um numero de 1 a 4")
        continue

    #Operação_Bancaria (Deposito)    

    if opcao == 1:
        
        deposito = float(input("Digite o valor a ser depositado: R$ "))
        
        if deposito < 0:
            print("Valor Invalido! Digite apenas valores superiores a R$ 0,00")
        else:
            print(f"Valor de R$ {deposito:.2f} depositado com sucesso")
            saldo_atual     += deposito
            qtd_depositos   += 1
            total_depositos += deposito
            lista_depositos.append(deposito)
    
    #Operação_Bancaria (Saque)  
            
    elif opcao == 2:
        
        if qtd_saques >= 3:
            print("Operação Invalida! Limite de saques diarios atingido")
        
        else: 
            valor_saque = float(input("Digite o Valor de Saque desejado: R$ "))
             
            if valor_saque < 0:
                print("Valor Invalido! Saques permitidos para valores acima de R$ 0,00")
            elif valor_saque > 500:
                print("Valor Invalido! Limite de R$ 500,00 por saque")    
            elif valor_saque > saldo_atual:
                print("Operação Invalida! Saldo indisponivel")
            else:
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
                saldo_atual   = saldo_atual - valor_saque
                qtd_saques   += 1
                total_saques += valor_saque
                lista_saques.append(valor_saque)
    
    #Operação_Bancaria (Ver Extrato Bancario)  
    
    elif opcao == 3:
        
        if qtd_depositos == 0 and qtd_saques == 0:
            print("Não foram realizadas movimentações")
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
                LISTA DE DEPOSITOS________________''')
            for d in lista_depositos:
                print(f"                 +R$ {d:.2f}")
            print('''
                LISTA DE SAQUES___________________''')
            for s in lista_saques:
                print(f"                 -R$ {s:.2f}")
            
    #Sair do programa
    
    elif opcao == 4:
        print("Obrigado por utilizar nosso sistema bancario, até logo!")
        break
    
    else:
        print("Opção invalida!")
