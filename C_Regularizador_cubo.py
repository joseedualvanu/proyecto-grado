def regularizador_cubo(BE,Peso1,Peso2,archivo_pedidos_2,Lista_Distancias):
    '''
    Description: modulo que genera el cubo CPBCP_ijk necesario para el modelo de optimizacion

    Args:
        BE (list): lista de pedidos y bloques elegidos
        Peso1 (float): Puntaje que se reparte a los bloques anteriores a los elegidos
        Peso2 (float): Puntaje que se reparte a los bloques posteriores a los elegidos
        archivo_pedidos_2 (csv): Archivo con el resultado de pedidos y codigos postales
        Lista_Distancias (list): lista con las distancias de los CP

    Returns:
        CPBCP (3Darray): array con los puntajes asociado para la terna pedido, bloque y codigo postal
        Cant_Pedidos (integer): cantidad de filas de la lista BE
        Cant_Bloques (integer): cantidad de columnas de la lista BE
        Cant_Codigos_Postales (integer): cantidad de códigos postales únicos
        Lista_Pedidos_CodPostales_Aux (list): lista con todos los códigos postales (puede existir repetidos)
        Lista_Pedidos_CodPostales_Unicos (list): lista con los códigos postales unicos
        Lista_Pedidos_k (list): lista con el indice del código postal correspondiente a cada pedido
        D (list): lista únicamente con las distancias de los CP de los pedidos de la ejecucion
        APuntaje (list): lista con las operaciones que luego se suma a BE, se utiliza para verificar solamente
        MPCP (3Darray): matriz de pedidos vs codigos postales

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
    '''
    import numpy as np
    # Numero de filas de B
    Cant_Pedidos = BE.shape[0]
    #print(filas)
    # Numero de columnas de BE
    Cant_Bloques = BE.shape[1]
    #print(columnas)
    # Matriz con las operaciones que luego se suma a BE
    APuntaje = np.zeros([Cant_Pedidos,Cant_Bloques])
    """
    Matriz BE_Normalizada - Matriz de Bloques Elegidos
    Primero se realizan operaciones en una matriz A, matriz auxiliar
    para luego obtener BE_Normalizada
    """
    #---- Columnas anteriores a las columnas de bloques elegidos ----
    # Recorro en filas
    for i in range(1,Cant_Pedidos):
        # Recorro primeras columnas para saber cuantas estan vacias
        CantVacias = 0
        j = 1
        while (BE[i][j] == 0):
                CantVacias = CantVacias + 1
                j = j + 1
        # Recorro primeras columnas vacias para agregar la ponderación
        for j in range(1,CantVacias+1):
            #Multiplico por j para darle mas importancia a las cercanas
            APuntaje[i][j] = round(Peso1*j/CantVacias,2)

    #---- Columnas posteriores a bloques elegidos ----
    # Recorro en filas
    ultimacolumn = 0
    for i in range(1,Cant_Pedidos):
        # Recorro las columnas buscando la ultima columna con entrada
        for j in range(1,Cant_Bloques):
            if BE[i][j] > 0:
                APuntaje[i][j] = (Cant_Bloques - j) / Cant_Bloques
                ultimacolumn = j
        #print(ultimacolumn)
        largo = Cant_Bloques - ultimacolumn - 1
        # Recorro primeras columnas para agregar la ponderación
        for j in range(ultimacolumn+1,Cant_Bloques):
                #columnas - j para darle mas importancia a las cercanas
                APuntaje[i][j] = round(Peso2*(Cant_Bloques - j)/largo,2)

    # Pasos para normalizar matriz A
    # Creo una matriz auxiliar para sacar la primer fila y columna con valores cero
    A_aux = APuntaje[1:,1:]
    row_sums = A_aux.sum(axis=1)
    A_aux = A_aux / row_sums[:, np.newaxis]
    #print(A)
    APuntaje[1:,1:] = A_aux
    BE_Normalizada = BE + APuntaje
    #BE = 10* BE / row_sums[:, np.newaxis]
    #print(R)

    #normed_matrix = normalize(BE, axis=1, norm='l1')

    print("Se regularizó la matriz BE.")
    print("-------------------------------------")

    """
    Matriz MPCP - Matriz de Pedidos vs Codigos Postales
    """
    # Lectura del archivo
    File_Pedido_PCP = open(archivo_pedidos_2,"r")

    # Inicializar lista vacia para guardar el archivo Pedido_PCP
    Lista_Pedidos_CodPostales = list();

    # Recorrida para obtener archivo en una lista
    for i in File_Pedido_PCP:
        # Se sacan los espacios
        i = i.rstrip()
        # Se separan los valores en una lista Linea
        Linea = i.split(",")
        # Se agrega Linea a la lista
        Lista_Pedidos_CodPostales.append(Linea)

    #Lista de Pedidos
    Lista_Pedidos_Aux = list()
    First_Line = True

    for pedido in Lista_Pedidos_CodPostales:
        if First_Line:
            First_Line = False
            # Primer fila con encabezado
            Lista_Pedidos_Aux.append(str(0))
            continue
        Lista_Pedidos_Aux.append(pedido[0])

    Lista_Pedidos_CodPostales_Aux = list()
    First_Line = True

    #Lista de Codigos Postales
    for pedido in Lista_Pedidos_CodPostales:
        if First_Line:
            First_Line = False
            # Primer fila con encabezado
            Lista_Pedidos_CodPostales_Aux.append(str(0))
            continue
        Lista_Pedidos_CodPostales_Aux.append(pedido[1])

    Lista_Pedidos_k = list()
    First_Line = True

    # Obtengo valores unicos de la lista de codigos postales
    Lista_Pedidos_CodPostales_Unicos = set(Lista_Pedidos_CodPostales_Aux)
    # Ordeno la lista en modo ascendente
    Lista_Pedidos_CodPostales_Unicos = sorted(Lista_Pedidos_CodPostales_Unicos)
    # Cantidad de numeros de codigos postales
    Cant_Codigos_Postales = len(Lista_Pedidos_CodPostales_Unicos)

    #Lista de Indices k (SE PUEDE JUNTAR LOS 3 FOR...)
    for pedido in Lista_Pedidos_CodPostales_Aux:
        if First_Line:
            First_Line = False
            Lista_Pedidos_k.append(str(0))
            continue

        #Obtengo el indice k
        k = Lista_Pedidos_CodPostales_Unicos.index(pedido)

        Lista_Pedidos_k.append(k)

    # Matriz de zeros para colocar codigos postales unicos vs pedidos
    MPCP = np.zeros((Cant_Pedidos,Cant_Codigos_Postales))

    # Agrego encabezado de codigos postales
    MPCP[0][:] = Lista_Pedidos_CodPostales_Unicos

    # Genero la Matriz de Pedidos vs Codigos Postales
    for i in range(1,len(Lista_Pedidos_Aux)):
        # Agrego encabezado de pedidos
        MPCP[i][0] = Lista_Pedidos_Aux[i]

        indice = Lista_Pedidos_CodPostales_Unicos.index(Lista_Pedidos_CodPostales_Aux[i])
        #print(indice)

        MPCP[i][indice] = 1

    # --------------------------------------------------------
    # --------------------------------------------------------
    # CUBO CPBCP: pedido vs bloque elegido vs codigos postales
    CPBCP = np.zeros((Cant_Pedidos,Cant_Bloques,Cant_Codigos_Postales))

    for i in range(1, Cant_Pedidos):

        # Obtengo el indice k que es el numero de la columna que tiene un 1 en la matriz MPCP
        k = np.where(MPCP[i][:] == 1)

        CPBCP[i][0][:] = MPCP[i][0]

        for j in range(1, Cant_Bloques):
            CPBCP[i][j][k] = BE_Normalizada[i][j]

    # --------------------------------------------------------
    # --------------------------------------------------------
    # CUBO CPBCP: pedido vs bloque elegido vs codigos postales
    D = list()
    First_Line = True

    # Agrego cabezal vacio
    D.append(0)

    # Genero una lista D UNICAMENTE con las distancias de los CP de los pedidos de la ejecucion
    for CodPos in Lista_Pedidos_CodPostales_Unicos:
        if First_Line:
            First_Line = False
            continue
        # Tomo
        D_Aux = Lista_Distancias[0][:]

        index = D_Aux.index(CodPos)

        D.append(Lista_Distancias[1][index])

    return CPBCP,Cant_Pedidos,Cant_Bloques,Cant_Codigos_Postales,Lista_Pedidos_CodPostales_Aux,Lista_Pedidos_CodPostales_Unicos, Lista_Pedidos_k,D,APuntaje,MPCP
