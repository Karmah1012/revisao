n2novo = "s"
while n2novo == "s":
 n  = int(input("Digite um número: "))
 if n%2 == 0 and n > 0:
    print("Este número é positivo e par")
 elif n%2 == 0 and n < 0:
    print("Este número é par e negativo")
 elif n%2 == 1 and n > 0:
    print("Este número é ímpar e positivo")
 elif n%2 == 1 and n < 0 :
    print("Este número é ímpar e negativo")
 n2novo = input("Gostaria de perguntar outro número?")

