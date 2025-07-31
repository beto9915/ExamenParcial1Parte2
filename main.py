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
            opcion=int(input("Seleccione una opcion: "))
            try:
                match int(opcion):
                    case 1:
                        a=int(input("Ingrese primer numero: "))
                        b=int(input("Ingrese segundo numero: "))
                        mcd=Program.mcd(a,b)
                        print(f"El mcd es: {mcd}")
                        print("\npresione ENTER para continuar...")
                        input()

                    case 2:
                        palabra=input("Ingrese la palabra: ")
                        veces=int(input("Ingrese cuantas veces: "))
                        print(f"{Program.n_veces(palabra, veces)}")
                        print("\npresione ENTER para continuar...")
                        input()
                    case 3:
                        cadena=input("Ingrese cadena de texto: ")
                        letra=input("Ingrese la letra: ")
                        cantidad=Program.letra_en_cadena(cadena, letra)
                        print(f"La cantidad de veces que aparece {letra} en {cadena} es: {cantidad}")
                        print("\npresione ENTER para continuar...")
                        input()
                    case 4:
                        numero=int(input("Ingrese numero: "))
                        binario=Program.decimal_a_binario(numero)
                        print(binario)
                        print("\npresione ENTER para continuar...")
                        input()
                    case 5:
                        numero=(int(input("Ingrese numero: ")))
                        cantidad=Program.digitos_en_numero(numero)
                        print(f"La cantidad de digitos en {numero} es: {cantidad}")
                        print("\npresione ENTER para continuar...")
                        input()
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
        if veces == 0:
            return ""
        else:
            print(palabra, end="")
            return Program.n_veces(palabra, veces - 1)

    @staticmethod
    def letra_en_cadena(cadena, letra):
        if cadena == "":
            return 0
        elif cadena[0] == letra:
            return 1 + Program.letra_en_cadena(cadena[1:], letra)
        else:
            return Program.letra_en_cadena(cadena[1:], letra)
    @staticmethod
    def decimal_a_binario(n):
        if n == 0:
            return 0
        else:
            return n % 2 + 10 * Program.decimal_a_binario(n // 2)

    @staticmethod
    def digitos_en_numero(numero):
        if numero==0:
            return 0
        else:
            return 1+Program.digitos_en_numero(numero // 10)
Program.main()