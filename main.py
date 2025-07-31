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
    @staticmethod
    def mcd(a, b):
        if b == 0:
            return a
        else:
            return Program.mcd(b, a % b)
    @staticmethod
    def n_veces():
