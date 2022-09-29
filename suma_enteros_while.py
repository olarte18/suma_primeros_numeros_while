## suma de n numeros enteros-operador while




print("----------------------------")
print("---SUMA N NUMEROS ENTEROS---")
print("----------------------------")

#input
n=int(input("digite un numero entero: "))

#procesing

i=1
sum=0
while i<=n:
    sum+=i
    i=i+1
#output
print("la suma es: "+str(sum))

