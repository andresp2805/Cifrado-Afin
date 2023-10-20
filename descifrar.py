import model as md

def ejecutar_decifrado():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    palabra = str(input("Ingrese el texto a descifrar: "))
    palabra_descifrada = md.decifrado(a, b, palabra)
    print("\n" + "Su texto cifrado es: \n" + "\n" + str(palabra_descifrada))
    
def iniciar_aplicacion()->None:
    print("BIENVENIDO AL PROGRAMA DE DESCIFRADO AFIN \n") 
    ejecutar_decifrado()
iniciar_aplicacion()