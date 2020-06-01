while True:
    cedula = int(input("Digite la cédula: "))
    rol = input("¿Profesor o Estudiante?: ")
    producto = int(input("Código del producto: "))
    cantidad = int(input("¿Cantidad de unidades?: "))
    precio = int(input("Precio: "))
    valor_total = cantidad * precio
    if rol == 'profesor':
        desc_profe = (valor_total * 20)//100
        valor_total = valor_total - desc_profe
        print(f"El {rol} con Cédula {cedula} debe pagar ${valor_total} por el producto {producto}")

    if rol == 'estudiante':
        desc_estudiante = (valor_total * 40)// 100
        valor_total = valor_total - desc_estudiante
        print(f"El {rol} con Cédula {cedula} debe pagar ${valor_total} por el producto {producto}")
        
    print("-----------------------------------------------------------------------------")
