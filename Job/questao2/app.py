while (True):
    print ("Informe um número")
    numero= int(input ())
    fibonacci1=0
    fibonacci2=1
    flag = 0
    while(fibonacci2 <= numero):
        if(numero == fibonacci1 or numero == fibonacci2):
            print("Dentro da sequencia de fibonacci")
            flag = 1
        tmp = fibonacci2    
        fibonacci2 = fibonacci1+fibonacci2
        fibonacci1 = tmp
    if(flag == 0):
        print("Fora da sequencia de fibonacci")


