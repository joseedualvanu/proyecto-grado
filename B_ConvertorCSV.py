def convertorcsv(CB,Dividendo,archivo_pedidos_1,archivo_distancias):
    '''
    Description:
        Se busca generar la matriz pedido vs bloques elegidos (BE), la matriz pedido vs tipo (TP), la lista con los datos iniciales y distancias

    Args:
        CB (int): cantidad de bloques del día
        Dividendo (int): peso de los bloques elegidos
        archivo_pedidos_1 (str): Ubicación y nombre del archivo con los pedidos y bloques
        archivo_distancias (str): Ubicación y nombre del archivo con los CP y distancias

    Returns:
        BE (list): lista de pedidos y bloques elegidos
        TP (list): lista de pedidos y sus tipos
        Lista_Datos_Iniciales (list): lista con la informacion de los pedidos
        Lista_Distancias (list): lista con las distancias de los CP
    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
    '''
    import numpy as np
    # Abrir archivo .csv como lectura de los pedidos
    File_Pedido_BE = open(archivo_pedidos_1,"r")

    # Inicializar lista vacia a trabajar
    Lista_Datos_Iniciales = list();

    # Recorrida para obtener preferencias en una lista
    for i in File_Pedido_BE:
        # Se sacan los espacios
        i = i.rstrip()
        # Se separan los valores en una lista Linea
        Linea = i.split(",")
        # Se agrega Linea a la coleccion de listas con las que se va a trabajar
        Lista_Datos_Iniciales.append(Linea)

    # Inicializar matriz de ceros
    # (al tener una columna con Nro orden se agrega una columna mas a la matriz)
    BE = np.zeros([len(Lista_Datos_Iniciales),CB + 1])
    # Se crea matriz para obtener id_pedido y tipo de pedido
    TP = np.zeros([len(Lista_Datos_Iniciales),2])

    # Saltear primera fila de cabezales
    First_Line = True

    # Recorremos la coleccion Lista Datos Iniciales
    for pedido in Lista_Datos_Iniciales:
        # Salteo primera linea
        if First_Line:
            First_Line = False
            continue

        # Indice del pedido a recorrer
        Index_Pedido = Lista_Datos_Iniciales.index(pedido)
        # Se carga el IdPedido en la columna 0 de la matriz BE
        BE[Index_Pedido][0] = str(pedido[0])

        #-------------------------------------------
        # PEDIDOS DE TIPO DELIVERY
        if pedido[1] == "1":
            # Cantidad de columnas del pedido actual
            Long_BE = len(pedido)
            #print(pedido)
            # Cantidad de BE en pedido se le quita 2
            # Por la columna 0 = 'IdPedido' y por el tipo de pedido
            Cant_BE = Long_BE - 2
            # Valor a asignar en matriz, depende de la Cant_BE

            #ORIGINAL
            Valor_BE = round(Dividendo / Cant_BE, 2)

            #PRUEBA 1
            # Valor_BE = round((Dividendo - Cant_BE + 1) ,2)

            #PRUEBA 2
            # Valor_BE = round((Dividendo - Cant_BE * 2 + 6) ,2)

            # Recorremos los valores del pedido
            # Arranca en 2 porque no se usa id_pedido ni tipo pedido
            for column in range(2,Long_BE):
                # Valor de preferencia de bloque
                Bloque_Preferencia = int(pedido[column])
                # Ingreso de valor a matriz BE
                BE[Index_Pedido][Bloque_Preferencia] = Valor_BE
        #-------------------------------------------
        # PEDIDOS DE TIPO PICK UP
        if pedido[1] == "2":
            # Cantidad de BE del pedido, se le quita 2
            # Por la columna 0 = 'IdPedido' y por el tipo de pedido
            #print(pedido)
            Cant_BE = int(pedido[2])
            # Valor a asignar en matriz, depende de la Cant_BE
            #ORIGINAL
            Valor_BE = round(Dividendo / Cant_BE, 2)

            #PRUEBA 1
            # Valor_BE = round((Dividendo - Cant_BE + 1) ,2)

            #PRUEBA 2
            # Valor_BE = round((Dividendo - Cant_BE * 2 + 6) ,2)

            # Recorremos los valores del pedido
            # Arranca en 2 porque no se usa id_pedido ni tipo pedido
            for column in range(1,int(pedido[2])+1):
                BE[Index_Pedido][column] = Valor_BE
        #-------------------------------------------
        # Se carga el IdPedido en la columna 0 matriz desde BE
        TP[Index_Pedido][0] = str(pedido[0])
        # Se carga el tipo de pedido en la columna 1 matriz desde BE
        TP[Index_Pedido][1] = str(pedido[1])

    #Encabezados del numero de bloque
    for j in range(1,len(BE[0])):
        BE[0][j] = str(j)

    # Abrir archivo .csv como lectura de las distancias
    File_Distancias = open(archivo_distancias,"r")

    # Inicializar lista vacia a trabajar
    Lista_Distancias = list();

    First_Line = True

    # Recorrida para obtener preferencias en una lista
    for i in File_Distancias:
        # A la primer linea la dejo igual, la segunda la convierto en int
        if First_Line:
            First_Line = False
            # Se sacan los espacios
            i = i.rstrip()
            # Se separan los valores en una lista Linea
            Linea = i.split(",")
            # Se agrega Linea a la coleccion de listas con las que se va a trabajar
            Lista_Distancias.append(Linea)
            continue
        # A la segunda linea hay que convertirla en int
        # Se sacan los espacios
        i = i.rstrip()
        # Se separan los valores en una lista Linea
        Linea = i.split(",")
        # Convierto la lista de string a lista de enteros
        Linea = list(map(float,Linea))
        # Se agrega Linea a la coleccion de listas con las que se va a trabajar
        Lista_Distancias.append(Linea)

    print("-------------------------------------")
    print("Se cargaron los archivos con el input.")
    print("-------------------------------------")
    return BE,TP,Lista_Datos_Iniciales,Lista_Distancias
