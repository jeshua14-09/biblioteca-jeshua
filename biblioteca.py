Libro_de_python = []
Libro_de_php = []
class libros:
    def Menulibros(self):
        print("-------------------------------------------------------")
        print("1 = VER LIBRO 1 (LIBRO DE PYTHON) ")
        print("2 = VER LIBRO 2 (LIBRO DE PHP) ")
        print("-------------------------------------------------------")
        desicion = int(input("INGRESE QUE LIBRO DESEA VER: "))
        if desicion == 1:
            self.libroNumero1()
        if desicion == 2:
            self.libroNumero2()
    def libroNumero1(self):
        print("-------------------------------------------------------")
        Menu=[
            ["Titulo : Phyton a fondo"],
            ["1A. Edicion"],
            ["Autor: Autor: Oscar Ramirez Jimenez"],
            ["Editorial: Marcombo"],
            ["Categoría(s):Programación De Bases De Datos"],
            ["Idioma:Español"],
            ["ISBN: 9788426732279."],
            ["Incluye Código fuente, 2022 "],
            ["648 Paginas"] 
        ]
        print("-------------------------------------------------------")
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
    def libroNumero2(self):
        print("-------------------------------------------------------")
        Menu=[
            ["Titulo : introduccion a php"],
            ["1A. Edicion"],
            ["Autor:  Miguel A. Arias"],
            ["5.98 x 0.23 x 9.02 pulgadas"],
            ["Idioma:Español"],
            ["ISBN: 9781492279372"],
            ["29 Agosto 2013"],
            ["110 páginas"] 
        ]
        print("-------------------------------------------------------")
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
        
class usuario:
    def __init__(self, nombre = 0, apellido= 0, cedula= 0):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_apellido(self, apellido):
        self._apellido = apellido
    def get_apellido(self):
        return self._apellido
    def set_cedula(self, cedula):
        self._cedula = cedula
    def get_cedula(self):
        return self._cedula
        
class Main(usuario,libros):
    def __init__(self):
        super(Main,self).__init__()
        print("-------------------------------------------------------")
        print("BIENVENIDO A LA BIBLIOTECA DE LA REPUBLICA ")
        print("1 = VER LIBROS CON SU REFERENCIA ")
        print("2 = PRESTAR LIBRO ")
        print("3 = SALIR ")
        print("-------------------------------------------------------")
        opcion = int(input("INGRESE LA OPCION DESEADA "))
        if opcion == 1:
            super(Main,self).Menulibros()
        if opcion == 2:
            Biblioteca = usuario()
            Biblioteca.set_nombre(input("INGRESE SU NOMBRE:  "))
            Biblioteca.set_apellido(input("INGRESE SU APELLIDO: "))
            Biblioteca.set_cedula(input("INGRESE LA CEDULA: "))
            print("1 = LIBRO 1 ")
            print("2 = LIBRO 2 ")
            opcion = int(input(("ESCOGE EL LIBRO QUE DESEA PEDIR PRESTADO ")))
            if opcion == 1:
                if 1 in Libro_de_python:
                    print("-------------------------------------------------------")
                    print("LIBRO NO DISPONIBLE O CUPADO")
                    self.__init__()
                    print("-------------------------------------------------------")
                else:
                    print("-------------------------------------------------------")
                    print("LIBRO PRESTADO ")
                    print("PRESTADO A LA PERSONA : ", (Biblioteca.get_nombre()), (Biblioteca.get_apellido()))
                    print(" CON CEDULA:", (Biblioteca.get_cedula()))
                    print("-------------------------------------------------------")
                    Libro_de_python.append(1)
                    self.__init__()
            if opcion == 2:
                if 1 in Libro_de_php:
                    print("-------------------------------------------------------")
                    print("LIBRO NO DISPONIBLE O OCUPADO ")
                    self.__init__()
                    print("-------------------------------------------------------")
                else:
                    print("LIBRO PRESTADO ")
                    print("PRESTADO A LA PERSONA: ", (Biblioteca.get_nombre()), (Biblioteca.get_apellido()))
                    print(" CON CEDULA :", (Biblioteca.get_cedula()))
                    Libro_de_php.append(2)
                    self.__init__()
        if opcion == 3:
            print(" ")
            exit()
Biblioteca = Main()