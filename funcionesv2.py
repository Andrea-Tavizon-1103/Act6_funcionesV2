print("Mas sobre funciones")
# Aqui se escriben las funciones

def suma_ab(a,b):
    s=a+b
    return s

def resta_ab(a,b):
    r=a-b
    return r

def mul_ab(a,b):
    m=a*b
    return m

def div_ab(a,b):
    d=a/b
    return d
#llamadas a funciones
#SUMA
print("Calculando suma")
n1=int(input("ingresa el primer numero: "))
n2=int(input("ingresa el segundo numero: "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es=  {suma}")

#RESTA
print("Calculando resta")
m1=int(input("Ingresa tu primer numero: "))
m2=int(input("Ingresa tu segundo numero: "))
res=resta_ab(m1,m2)
print(f"La resta de {m1} - {m2} es= {res}")

#MULTIPLICACION
print("Calculando multiplicacion")
o1=int(input("ingresa el primer numero: "))
o2=int(input("ingresa el segundo numero: "))
multi=mul_ab(o1,o2)
print(f"La multiplicacion de {o1} x {o2} es=  {multi}")

#DIVISION
print("Calculando division")
d1=int(input("ingresa el primer numero: "))
d2=int(input("ingresa el segundo numero: "))
div=div_ab(d1,d2)
print(f"La division de {d1} / {d2} es=  {div}")