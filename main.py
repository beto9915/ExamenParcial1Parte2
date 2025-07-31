class Program:
    @staticmethod
    def main():
        opcion=0
        while opcion!=6:
            print("===MENU===")
            print("1. Calcular MCD")
            print("2. Cadena repetida N veces")
            print("3. Contar letras en una cadena")
            print("4. Convertir decimal a binario")
            print("5. Contar digitos de un numero")
            print("6. Salir")
            try:
                match int(opcion):
                    case 1:
                        a=int(input("Ingrese primer numero: "))
                        b=int(input("Ingrese segundo numero: "))
                        mcd=Program.mcd(a,b)
                        print(f"El mcd es: {mcd}")

                    case 2:
                        palabra=input("Ingrese la palabra: ")
                        veces=int(input("Ingrese cuantas veces: "))
                        print(f"{Program.n_veces(palabra, veces)}")
                    case 3:
                        cadena=input("Ingrese cadena de texto: ")
                        letra=input("Ingrese la letra: ")
                        cantidad=Program.letra_en_cadena(cadena, letra)
                        print(f"La cantidad de veces que aparece {letra} en {cadena} es: {cantidad}")
                    case 4:


            except:
                print(f"Error")

    @staticmethod
    def mcd(a, b):
        if b == 0:
            return a
        else:
            return Program.mcd(b, a % b)
    @staticmethod
    def n_veces(palabra, veces):
        if veces==0:
            return 0
        else:
            return palabra & Program.n_veces(palabra, veces)
    @staticmethod
    def letra_en_cadena(cadena, letra):
        if cadena == "":
            return 0
        elif cadena[0] == letra:
            return 1 + Program.letra_en_cadena(cadena[1:], letra)
        else:
            return Program.letra_en_cadena(cadena[1:], letra)
    @staticmethod
