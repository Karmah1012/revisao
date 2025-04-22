vla = int(input("Digite um valor para A: "))
vlb = int(input("Digite um valor para B: "))
vlc = int(input("Digite um valor para C: "))
soma = vla + vlb
print(f"A soma é: {soma}")
##############################################
if soma > vlc :
    print(f"A soma é maior que C e é: {soma}")
else:
    print(f"O valor de C que vale: {vlc} é maior que a soma de A + B, que vale: {soma}")