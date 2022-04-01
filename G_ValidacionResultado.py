def validacion(Lista_Datos_Iniciales,resultado):
    '''
    Description:

    Args:
        Lista_Datos_Iniciales ():
        resultado ():
    Returns:
        resultadoValidacion ():
        conteoValidacion ():
    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
    '''

   #import numpy as np

    #Saltear primera fila de cabezales
    First_Line = True

    #Inicializo nuevo diccionario
    resultadoValidacion = dict()
    #Inicializo nuevo diccionario y contadores
    conteoValidacion = dict()
    ContCumplen = 0
    ContNoCumplen = 0

    #Recorremos la coleccion Lista Datos Iniciales
    for pedido in Lista_Datos_Iniciales:
        #Salteo primera linea
        if First_Line:
            First_Line = False
            continue
        #Obtener el numero de orden a validar
        NumeroOrden = int(pedido[0])

        #Obtenemos el Bloque asignado por modelo para ese Numero de Orden
        BloqueAsignado = resultado.get(int(NumeroOrden))

        #Flag cumplio pedido
        CumplioPedido = False
        #Saltear primera y segunda Columnas de 'pedido'
        First_Line = True
        Second_Line = True

        for i in pedido:
            #Salteo primeras dos columnas (Numero de orden y Tipo de pedido)
            #Salteo primera linea
            if First_Line:
                First_Line = False
                continue

            #Salteo segunda linea
            if Second_Line:
                Second_Line = False
                continue

            #Es el Bloque Elegido por el cliente
            BloqueElegido = int(i)

            #Me quedo con el tipo de pedido
            TipoPedido = pedido[1]

            #Se diferencia por tipo de pedido, en caso que sea pickup el bloque correcto es el elegido o cualquier bloque anterior.

            #Delivery
            if TipoPedido == '1':
                if BloqueAsignado == BloqueElegido:
                    CumplioPedido = True
                    break
            #Pickup
            if TipoPedido == '2':
                if BloqueAsignado <= BloqueElegido:
                    CumplioPedido = True
                    break

        if CumplioPedido:
            ContCumplen += 1
        else:
            ContNoCumplen +=1

        #Agrego si cumplio o no a dict 'resultadoValidacion'
        resultadoValidacion[NumeroOrden] = CumplioPedido

        #Asigno total como la suma de pedidos que cumplen y los que no
        Total = ContCumplen + ContNoCumplen

        conteoValidacion['Cumplen'] = ContCumplen
        conteoValidacion['No Cumplen'] = ContNoCumplen
        conteoValidacion['Total'] = Total
        conteoValidacion['%Cumplimiento'] = ContCumplen / Total * 100

    print("VALIDACIÓN")
    #print("Se imprime resultado validación.")
    #print(resultadoValidacion)
    print("Se imprime el conteo de validación.")
    print(conteoValidacion)
    print("-------------------------------------")

    return resultadoValidacion, conteoValidacion
