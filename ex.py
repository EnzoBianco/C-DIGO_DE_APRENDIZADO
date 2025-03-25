import locate
import os
import emoji
import colorama

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

os.system("cls")

if num2 == 0:
    print("Não é possível realizar a divisão por zero.")
else:
    print(f"A divisão de {num1} por {num2} é igual a {num1 / num2}.")
    
os.system("pause")
    
os.system("cls")
 
# ------------------------------------------------------------------------------------------------------------------

num_inteiro = int(input("Digite um número inteiro: "))

os.system("cls")

if num_inteiro % 2 == 0:
    print(f"O número {num_inteiro} é par.")
else:
    print(f"O número {num_inteiro} é ímpar.")
    
os.system("pause")
    
os.system("cls")
    
# -------------------------------------------------------------------------------------------------------------------

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))
quarto_numero = int(input("Digite o quarto número: "))

os.system("cls")

if primeiro_numero == segundo_numero and primeiro_numero != terceiro_numero and primeiro_numero != quarto_numero:
    print("O primeiro e segundo números digitados são iguais.")
elif primeiro_numero == terceiro_numero and primeiro_numero != segundo_numero and primeiro_numero != quarto_numero:
    print("O primeiro e terceiro números digitados são iguais.")
elif primeiro_numero == quarto_numero and primeiro_numero != segundo_numero and primeiro_numero != terceiro_numero:
    print("O primeiro e quarto números digitados são iguais.")
elif segundo_numero == terceiro_numero and segundo_numero != primeiro_numero and segundo_numero != quarto_numero:
    print("O segundo e terceiro números digitados são iguais.")
elif segundo_numero == quarto_numero and segundo_numero != primeiro_numero and segundo_numero != terceiro_numero:
    print("O segundo e quarto números digitados são iguais.")
else:
    print("O terceiro e quarto números digitados são iguais.")
    
os.system("pause")
    
os.system("cls")



# ---------------------------------------------------------------------------------------------------------------------

first = int(input("Digite o primeiro número: "))
second = int(input("Digite o segundo número: "))
third = int(input("Digite o terceiro número: "))

os.system("cls")

if second == first + 1 and third == second + 1:
    print(f"Os números digitados, {first}, {second} e {third}, são consecutivos em ordem crescente.")
elif second == first - 1 and third == second - 1:
    print(f"Os números digitados, {first}, {second} e {third}, são consecutivos em ordem decrescente.")
else:
    print("Os números digitados não são consecutivos em ordem crescente ou decrescente.")
    
os.system("pause")
    
os.system("cls")

# ---------------------------------------------------------------------------------------------------------------------

idade = int(input("Digite a sua idade: "))

os.system("cls")

if idade <= 16:
    print(f"Você, por ter {idade} anos, tem direito a desconto em nossa loja!")
elif idade >= 60:
     print(f"Você, por ter {idade} anos, tem direito a desconto em nossa loja!")
else:
    print(f"Infelizmente, por ter {idade} anos, você não tem desconto em nossa loja!")
     
os.system("pause")
    
os.system("cls")

# ---------------------------------------------------------------------------------------------------------------------

print("Seja Bem-Vindo à nossa colônia de férias!")

print("Aperte Enter para continuar e ver nossas opções...")

input()

os.system("cls")

print("Temos dois tipos de apartamento para você e sua família!")

print("Apartamento 1 - Mais simplicidade, porém com muito conforto!")
print("Apartamento 2 - Mais luxo para você e sua família, com a melhor expêriencia!") 
        
        
escolha = input("Digite o número do apartamento que deseja (1 ou 2): ")

if escolha == "1":
    print("Você escolheu o Apartamento 1 - Mais simplicidade, porém com muito conforto!")
    print("Digite, por favor, a quantidade de pessoas, contando com você, que estarão na colônia de férias: ")
    quantidade = int(input())
    print("Ótima escolha!")
    if quantidade == 1:
        print("Pelos seis dias, o total a ser pago é de R$120,00.")
    elif quantidade == 2:
        print("Pelos seis dias, o total a ser pago é de R$168,00.")
    elif quantidade == 3:
        print("Pelos seis dias, o total a ser pago é de R$210,00.")
    elif quantidade == 4:
        print("Pelos seis dias, o total a ser pago é de R$252,00.")
    elif quantidade == 5:
        print("Pelos seis dias, o total a ser pago é de R$240,00.")
    elif quantidade == 6:
        print("Pelos seis dias, o total a ser pago é de R$318,00.")
    else:
        print("Número de pessoas inválido.")   
        
elif escolha == "2":
    print("Você escolheu o Apartamento 2 - Mais luxuoso para você e sua família, com a melhor experiência!")
    print("Digite, por favor, a quantidade de pessoas, contando com você, que estarão na colônia de férias: ")
    quantidade = int(input())
    print("Ótima escolha!")
    if quantidade == 1:
        print("Pelos seis dias, o total a ser pago é de R$150,00.")
    elif quantidade == 2:
        print("Pelos seis dias, o total a ser pago é de R$204,00.")
    elif quantidade == 3:
        print("Pelos seis dias, o total a ser pago é de R$252,00.")
    elif quantidade == 4:
        print("Pelos seis dias, o total a ser pago é de R$300,00.")
    elif quantidade == 5:
        print("Pelos seis dias, o total a ser pago é de R$342,00.")
    elif quantidade == 6:
        print("Pelos seis dias, o total a ser pago é de R$378,00.")
    else:
        print("Número de pessoas inválido.")