
#Lista com os dias da semana em forma escrita
dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

#Dicionário que contém os meses do ano e seu número de dias
meses = {'Janeiro' : 31, 
         'Fevereiro' : 28, 
         'Março' : 31,
         'Abril' : 30, 
         'Maio' : 31, 
         'Junho' : 30,
         'Julho' : 31, 
         'Agosto' : 31, 
         'Setembro' : 30,
         'Outubro' : 31, 
         'Novembro' : 30, 
         'Dezembro' : 31}

#Lista que armazena os dias do ano em forma escrita
dias_ano_escrito = [0]

#input
ano = 365 # pergunta o ano
 
 #Gerador de dias em forma escrita (também funciona com ano bissexto)
for _ in range(ano): 
    
    dias_ano_escrito.append(dias_da_semana[6])
    if len(dias_ano_escrito) >= ano:
    	break
    else:
        dias_ano_escrito.append(dias_da_semana[0])
    
    if len(dias_ano_escrito) >= ano:
    	break
    else:
        dias_ano_escrito.append(dias_da_semana[1])
    
    if len(dias_ano_escrito) >= ano:
    	break
    else:
        dias_ano_escrito.append(dias_da_semana[2])
    
    if len(dias_ano_escrito) >= ano:
    	break
    else:
        dias_ano_escrito.append(dias_da_semana[3])
    
    if len(dias_ano_escrito) >= ano:
    	break
    else:
        dias_ano_escrito.append(dias_da_semana[4])
    
    if len(dias_ano_escrito) >= ano:
    	break
    else:
        dias_ano_escrito.append(dias_da_semana[5])
   
    if len(dias_ano_escrito) >= ano:
    	break

#Lista com os do ano em forma numérica
dias_num = [0]

#Gerador de dias 1 a 365 numérico
for _ in range(1):
        
    dias_num.extend(range(1, meses['Janeiro']+1))
    dias_num.extend(range(1, meses['Fevereiro']+1))
    dias_num.extend(range(1, meses['Março']+1))
    dias_num.extend(range(1, meses['Abril']+1))
    dias_num.extend(range(1, meses['Maio']+1))
    dias_num.extend(range(1, meses['Junho']+1))
    dias_num.extend(range(1, meses['Julho']+1))
    dias_num.extend(range(1, meses['Agosto']+1)) 
    dias_num.extend(range(1, meses['Setembro']+1))
    dias_num.extend(range(1, meses['Outubro']+1))
    dias_num.extend(range(1, meses['Novembro']+1))
    dias_num.extend(range(1, meses['Dezembro']+1))

#Dicionário com a "Escala" e os parâmetros para o código /// valor do contador e do acumulador
escalas = {"46" : [3, 3], "48" : [7, 5]}

#input
escala = escalas["46"][1]

#Cores para o terminal
cor1 = '\033[96m'
cor2 = '\033[93m'
cor3 = '\033[97m'

#--------------------------------------------------------------------------------
#Variáveis

folga_1 = folga_2 = 0 #Variáveis para indicar os dias de folga
contador_de_folgas = 0 #Conta de 1 a 365 somando as folgas no loop
contador_de_dias = 0 #Conta de 1 a 365 no loop
contador_de_loop = 0 #Conta de 1 a 5/6 dentro do loop e reseta
condicao = True #determina se começa na semana de 5 ou 6
primeiroloop = True #indica se inicia na semana de 5 ou 6 dias (True para 5 e False par 6)

#--------------------------------------------------------------------------------

while contador_de_dias <= 365:
             
    contador_de_dias += 1
    
    contador_de_loop += 1
    
    contador_de_folgas = contador_de_dias + 2
    
    if primeiroloop == True:
        contador_de_dias = 0
        contador_de_loop = 5 #pra iniciar na semana de 5 ou 6
        contador_de_dias = escala #numero de dias até a folga (se iniciar com folga soma as folga junto com a semana)
        contador_de_folgas = contador_de_dias
        primeiroloop = False
      
    if contador_de_loop == 6 and condicao == False and (contador_de_folgas <= ano):
        folga_1 = contador_de_dias + 1
        folga_2 = contador_de_dias + 2
        print (cor1, dias_num[folga_1], dias_ano_escrito[folga_1], dias_num[folga_2], dias_ano_escrito[folga_2], "seis")
        contador_de_loop = 0
        folga_1 = 0
        folga_2 = 0
        condicao = True
        contador_de_dias += 2
        print(cor3, '-'*20)
    
    contador_de_folgas = contador_de_dias + 2 
            
    if contador_de_loop == 5 and condicao == True and (contador_de_folgas <= ano):
        folga_1 = 0
        folga_2 = 0
        folga_1 = contador_de_dias + 1
        folga_2 = contador_de_dias + 2
        print (cor2, dias_num[folga_1], dias_ano_escrito[folga_1], dias_num[folga_2], dias_ano_escrito[folga_2], "cinco")
        contador_de_loop = 0
        folga_1 = 1
        folga_2 = 2
        condicao = False
        contador_de_dias += 2
    
    
 
 
 

    