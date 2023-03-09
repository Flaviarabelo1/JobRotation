print ("Informe uma palavra")
palavra= input()
tamanho = len(palavra)
result=""
for i in range(tamanho-1, -1, -1):
    result += palavra[i]
print(result)
