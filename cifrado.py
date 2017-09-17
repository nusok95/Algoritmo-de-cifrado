class Cifrar(object):
    """docstring for Cifrar"""

    def __init__(self):
        super(Cifrar, self).__init__()
        self.size = 0

    def dividir_string(self, string):
        self.size = len(string)
        if(self.size % 2 == 1):
            string += " "
            self.size += 1
        self.first_size = self.size / 2
        self.second_size = self.first_size
        self.first_string = string[0: int(self.first_size)]
        self.second_string = string[int(self.second_size): int(self.size)]
        # print(self.first_string)
        # print(self.second_string)

    def invertir_string(self):
        self.first_string = self.first_string[::-1]
        self.second_string = self.second_string[::-1]

    def intercalar(self):
        cadena = "".join(
            i + j for i, j in zip(self.first_string, self.second_string))
        return cadena

    def to_ascii(self, string):
        x = [ord(c) for c in string]
        # print(x)
        cadena = ""
        for i in x:
            if i / 10 < 10:
                i = i * 10
            cadena = cadena + str(i)
        # print(cadena)
        hexa = hex(int(cadena))
        # print(hexa)
        # print(int(hexa, 16))

        return hexa

    def cifrar(self, cadena):
        if len(cadena) < 2:
            return self.cifrar_char(cadena)
        self.dividir_string(cadena)
        self.invertir_string()
        cadena = self.intercalar()
        # print(cadena)
        return self.to_ascii(cadena)

    def cifrar_char(self, char):
        char = self.to_ascii(char)
        return char


class Descifrar(object):
    """docstring for Descifrar"""

    def __init__(self):
        super(Descifrar, self).__init__()

    def hex_to_dec(self, hexa):
        dec = (int(hexa, 16))
        return dec

    def dec_to_ascii(self, dec):
        lista = []
        dec = str(dec)
        aux = ''
        contador = 0
        for numero in dec:
            aux += numero
            if len(aux) > 2:
                lista.append(aux)
                contador += 1
                aux = ''
        return lista

    def ascii_to_string(self, lista_ascii):
        palabra = ""
        for valor in lista_ascii:
            valor = int(valor)
            if(valor > 255):
                valor = int(valor / 10)
            palabra += chr(valor)
        return palabra

    def desintecalar(self, palabra):
        first_string = ''
        second_string = ''
        flag = 1
        for letra in palabra:
            if flag == 1:
                first_string += letra
                flag = 0
            else:
                second_string += letra
                flag = 1
        return(first_string[::-1] + second_string[::-1])

    def descifrar(self, cifrado):
        decimal = self.hex_to_dec(cifrado)
        ascii = self.dec_to_ascii(decimal)
        palabra = self.ascii_to_string(ascii)
        return self.desintecalar(palabra)


if __name__ == '__main__':
    cifrar = Cifrar()
    descifrar = Descifrar()
    while True:
        print("\n1.-Cifrar \n2.-Descifrar \n3.-Salir\n")
        x = input("->")
        if x == '1':
            string = input("Digite el texto: ")
            cifrado = cifrar.cifrar(string)
            print("Texto cifrado: ", cifrado)
        elif x == '2':
            string = input("Digite el texto: ")
            descifrado = descifrar.descifrar(string)
            print("Texto descifrado: ", descifrado)
        elif x == '3':
            print('0x3db10b0c0e17d494f11fb2e28c7ab8')
            break
