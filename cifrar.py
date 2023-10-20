import model as md

def ejecutar_cifrar_afin():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    palabra = str(input("Ingrese el texto a cifrar: "))
    palabra_cifrada = md.cifrar_afin(a, b, palabra)
    print("\n" + "Su texto cifrado es: \n" + "\n" + str(palabra_cifrada))
    
def iniciar_aplicacion()->None:
    print("BIENVENIDO AL PROGRAMA DE CIFRADO AFIN \n") 
    ejecutar_cifrar_afin()
iniciar_aplicacion()