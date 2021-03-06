# ParcialHerramientasComputacionales

### Problema
 La mercatería se encuentra de aniversario y ha decidido otorgar descuentos pero sólo a algunos productos seleccionados y dependiendo también si es estudiante o profesor, pues tienen descuentos diferentes. Se desea saber entonces por cada compra cuánto debe pagar el usuario en caja. Para ello:
 
- Pida por teclado la siguiente información para el cliente: cédula y rol: profesor o estudiante.
- Registrar el producto a comprar: código producto, cantidad de unidades y precio del producto.
- Los descuentos están dados de la siguiente forma: los estudiantes tienen un 40% de descuento mientras que los profesores tienen un 20% de descuento.

Al final el procedimiento por cada cliente debería imprimir el valor a pagar por sus productos de la forma: "El Rol con cédula Numero, debe pagar Valor por el producto Código".

### Modelo computacional

Lo resuelve el siguiente algoritmo que hace las veces  de una *caja registradora* inteligente que calcula descuentos especiales de acuerdo al rol de los clientes de la mercatería y que al final da como resultado la factura de compra: 

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
  Este código se encuentra dentro del repositorio con el nombre de ***Mercatería***, éste fue desarrollado en el lenguaje de programación Python y se puede ingresar dando click [aqui](https://github.com/Deaf2234/ParcialHerramientasComputacionales/blob/master/Mercater%C3%ADa.py)

### Entrada
El algoritmo anteriormente mencionado recibe como entrada datos de caracteres para preguntar el rol de cada cliente y también recibe datos de números para la cédula del cliente, la cantidad de productos que va a comprar, el precio por producto y el código del producto.

### Salida
El algoritmo emite los siguientes datos como resultado de los datos primeramente ingresados: *rol, cédula, valor a pagar y el código del producto.*

### Solución
Para darle solución al problema se calculó primeramente el *valor total* de acuerdo a los datos ingresados como *cantidad* y *precio* por producto; luego de esto se procedió a crear dos condiciones planteadas de la siguiente manera:

 1. Si el *rol* ingresado es igual a "profesor" entonces al valor total de su compra se le aplicará un descuento del 20% como lo indican las condiciones del problema, para calcular dicho descuento se multiplica el valor total ya obtenido por 20 y luego se realiza una división entera por 100; Por último se imprime por pantalla la **Salida** mencionada en la sección anterior.

 2. Si el *rol* ingresado es igual a "estudiantes" entonces al valor total de su compra se le aplicará un descuento del 40% como lo indican las condiciones del problema, para calcular dicho descuento se multiplica el valor total ya obtenido por 40 y luego se realiza una división entera por 100; Por último se imprime por pantalla la **Salida** mencionada en la sección anterior.

### Errores
Dentro del repositorio se encuentra un archivo específico hablando detalladamente de los errores presentados y los que se puedan presentar; además de eso se presenta las estrategias utilizadas para resolver los problemas presentada y como sugerencia para darle solución a los posibles errores que se puedan presentar.

Para acceder al archivo de **Errores y estrategias** da click [aqui.](https://github.com/Deaf2234/ParcialHerramientasComputacionales/blob/master/Errores%20y%20estrategias.pdf)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NjEyNzQ5NDAsLTIxMjY0NDQxMjUsLT
ExMTQyODEzODNdfQ==
-->