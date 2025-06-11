def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    if b != 0:
        return a / b
    else:
        return "Nu se poate împărți la 0!"

print("Calculator simplu")
a = float(input("Primul număr: "))
b = float(input("Al doilea număr: "))
op = input("Operație (+, -, *, /): ")

if op == "+":
    print("Rezultat:", adunare(a, b))
elif op == "-":
    print("Rezultat:", scadere(a, b))
elif op == "*":
    print("Rezultat:", inmultire(a, b))
elif op == "/":
    print("Rezultat:", impartire(a, b))
else:
    print("Operație invalidă!")