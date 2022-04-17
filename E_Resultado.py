def resultado(X,A,Cant_Pedidos,Cant_Bloques,Cant_Codigos_Postales,CPBCP,Lista_Pedidos_CodPostales_Aux,MO):
    '''
    Description:
        Procesar el output del modelo.
        Se realiza un conteo y se clasifica.
    Args:
        X (pulp dict 3D binary): variable de asignacion del pedido i al bloque j y codigo postal k X_ijk
        A (pulp dict 2D binary): variable de asignacion de bloque j al codigo postal k A_jk
        Cant_Pedidos (int): cantidad de pedidos total
        Cant_Bloques (int): cantidad de bloques como opcion
        Cant_Codigos_Postales (int): cantidad de codigos postales de los pedidos
        CPBCP (3Darray): array con los puntajes asociado para la terna pedido, bloque y codigo postal
        Lista_Pedidos_CodPostales_Aux (list): lista con todos los códigos postales (puede existir repetidos)
        MO (integer): Capacidad de armado de pedidos por bloque por persona
    Returns:
        resultado (dict): pedido (key) vs bloque elegido
        resultadoPorBloque (dict): bloque (key) vs cantidad de pedidos en el bloque
        resultadoCPBloque (dict): bloque (key) vs cantidad de codigos postales en el bloque
        resultadoBloqueMO (dict): bloque (key) vs cantidad de personas necesarias para el bloque
        contTotal (int): cantidad de codigos postales recorridos en el dia
    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
    '''

    iR = range(1,Cant_Pedidos)
    jR = range(1,Cant_Bloques)
    kR = range(1,Cant_Codigos_Postales)

    #Se crea un dictionario para guardar los resultados pedido - bloque
    resultado = dict()
    resultadoCPBloque = dict()
    resultadoBloqueMO = dict()
    #Se crea un dictionario para guardar los resultados por Bloque
    resultadoPorBloque = dict()

    for i in iR:
        for j in jR:
            for k in kR:
                if X[i][j][k].varValue > 0:
                    #print('Pedido ' + str(i) + ' va al bloque ' + str(j) + ' y codigo postal ' + str(k) + ' - CP dato ' + Lista_Pedidos_CodPostales_Aux[i] )
                    Id_Pedido = int(CPBCP[i][0][0])
                    resultado[Id_Pedido] = j

    #Recorrida para generar cantidad de pedidos por bloque
    for j in jR:
        #Inicializo contador
        contBloque = 0
        for i in iR:
            for k in kR:
                if X[i][j][k].varValue > 0:
                    contBloque += 1
        resultadoPorBloque[j] = contBloque

    #Contador de todos los CP visitados en el dia
    contTotal = 0

    for j in jR:
        # Inicializo contador de CP
        cont = 0
        for k in kR:
            if A[j][k].varValue > 0:
               #print('El bloque ' + str(j) + ' tiene de CP a ' + str(k))
                cont += 1

        resultadoCPBloque[j] = cont
        contTotal += cont

    # Obtener un dict de MO requerida por bloque
    for j in jR:
        cantPedidos = resultadoPorBloque[j]
        resultadoBloqueMO[j] = cantPedidos / MO

    return resultado,resultadoPorBloque,resultadoCPBloque,resultadoBloqueMO,contTotal
