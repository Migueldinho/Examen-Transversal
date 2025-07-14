productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def validar_texto(mensaje_input):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip) == 0:
            continue
        else:
            return texto

def validar_numero_entero_positivo(msg_input:str):
    while True:
        try:
            numero = int(input(msg_input))
            if numero <= 0:
                print("Invalido")
                continue
            else:
                return numero
        except ValueError:
            print("Ingrese un numero valido")

def stock_marca():
    for i in productos:
        print(f"stock: {productos[i][0]}")
    

def actualizar_precio(modelo:str, precio:int):
    modelo(validar_texto("Ingrese el modelo : "))
    for i in productos:
        print(productos[i][0])
    if productos[i][0].lower() == modelo.lower():
        print("Encontrado, Cambie el precio ")    
        input("Nuevo precio del producto : ")

def menu(): 
    print("***MENU PRINCIPAL***")
    while True:
        print("1. Stock marca")
        print("2. Busqueda por precio")
        print("3. Actualizar precio")
        print("4. Salir") 
        try:
            opcion = int(input("Ingrese una opcion : "))
        except ValueError: 
            print("Ingrese una opcion : ") 
            continue


        if opcion == 1:
            modeloo = input("ingrese el modelo : ")
            if modeloo == "hp" or "lenovo":
                print(stock_marca(stock))

        elif opcion == 2:
            precio = (validar_numero_entero_positivo("Ingrese  el rango de precio que desea buscar "))   
            if precio > 249000 and precio < 425000:
                print("Lenovo , HP, Dell, ") 
            else:
                print("Asus") 

        elif opcion == 3:
            actualizar_precioo = input("Ingrese la marca que quiere actualizar : ")
            if actualizar_precioo == "hp" or "lenovo" or "asus" or "dell":
                print("ingrese el nuevo precio del producto : ")
            print(actualizar_precio)

        elif opcion == 4:
            break     
menu()