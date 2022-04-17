def modelo(CPBCP,Cant_Pedidos,Cant_Bloques,Cant_Codigos_Postales,TP,Lista_Pedidos_CodPostales_Aux,Lista_Pedidos_k, P ,D,Capacidad):
    '''
    Description:
        Ejecución del modelo de optimizacion matemática

    Args:
        CPBCP (3Darray): array con los puntajes asociado para la terna pedido, bloque y codigo postal
        Cant_Pedidos (integer): cantidad de filas de la lista BE
        Cant_Bloques (integer): cantidad de columnas de la lista BE
        Cant_Codigos_Postales (integer): cantidad de códigos postales únicos
        TP (list): lista de pedidos y sus tipos
        Lista_Pedidos_CodPostales_Aux (list): lista con todos los códigos postales (puede existir repetidos)
        Lista_Pedidos_k (list): lista con el i ndice del código postal correspondiente a cada pedido
        P (float): parámetro que relaciona beneficio del cubo contra la clusterizacion por distancias en la función objetivo
        D (list): lista únicamente con las distancias de los CP de los pedidos de la ejecucion
        Capacidad (integer): capacidad de pedido por bloque

    Returns:
        X (pulp dict 3D binary): variable de asignacion del pedido i al bloque j y codigo postal k X_ijk
        A (pulp dict 2D binary): variable de asignacion de bloque j al codigo postal k A_jk
        ValorObjetivo (pulp value): valor hallado por la función objetivo

    Error:
        --

    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
    '''
    # Cargar la librería PuLP
    # from pulp import *
    import pulp as pl
    # import numpy as np

    # Para elegir el solver
    # Si no quiero seleccionar solver
    # solver = ""
    # solver = pl.PULP_CBC_CMD(timeLimit=15)
    solver = pl.PULP_CBC_CMD()

    #solver.Parametros.timeLimit.set(1)
    # solver = pl.get_solver('GUROBI_CMD')
    # solver = pl.get_solver('CPLEX_PY') #Linux
    # solver = pl.get_solver('CPLEX_CMD')
    # solver = pl.get_solver('MOSEK')
    # solver = pl.PULP_CHOCO_CMD()

    # Distancia de un CP con los otros CP (km)
    # D = ([3, 4, 5, 2]);

    # Vector con Tipo de Entrega de Bloque (1- Delivery , 2- Pickup) _ for j in bloques
    #                 1  2  3  4  5  6  7
    # TEB = np.array([0, 2, 1, 1, 2, 1, 1, 1])

    # Problema de programación lineal
    prob = pl.LpProblem("test_de_optimizacion", pl.LpMaximize)

    iR = range(1,Cant_Pedidos)
    jR = range(1,Cant_Bloques)
    kR = range(1,Cant_Codigos_Postales)

    # Variables de decision
    # X_ijk: Variable de asignacion de pedido a bloque
    X = pl.LpVariable.dicts("(pedido,bloque,codigoPostal)", (iR,jR,kR) ,cat='Binary')

    # A_jk: Variable de asignacion de bloque a codigo postal
    A = pl.LpVariable.dicts("(bloque,codigoPostal)", (jR, kR), cat='Binary')

    # Restriccion 1 unicidad
    for i in iR:
        prob += pl.lpSum([ X[i][j][k] for j in jR for k in kR]) == 1
    # Restriccion 2 capacidad de bloque
    for j in jR:
        prob += pl.lpSum([ X[i][j][k] for i in iR for k in kR]) <= Capacidad
   # Restriccion de tipo de lote
    # for i in iR:
    #     for j in jR:
    #         prob +=  pl.lpSum([ X[i][j][k]*(TP[i][1] - TEB[j]) for k in kR]) == 0

    # Resticcion 3 activacion Matriz Ajk
    for j in jR:
        for k in kR:
          prob += pl.lpSum([X[i][j][k] for i in iR] ) <= A[j][k]*10000

    #Restriccon de Pedido a Codigo Postal
    for i in iR: # Para cada pedido
        # Necesito el indice del CP de cada pedido para ponerlo en k
        k = Lista_Pedidos_k[i]
       # for k in kR:
        prob += pl.lpSum([X[i][j][k] for j in jR] ) == 1 # Sumo en bloques

    # Funcion Objetivo
    prob += pl.lpSum([ (1 - P) * X[i][j][k]*CPBCP[i][j][k] - P/10000 *(A[j][k]*D[k] + (A[j][k] - 1)*D[k]) for i in iR for j in jR for k in kR ])

    # Resuelvo el problema
    prob.solve(solver)

    # Mostrar estado
    print("ESTADO DEL SOLVER")
    print("Status")
    print(pl.LpStatus[prob.status])
    print("Valor objetivo")
    print(pl.value(prob.objective))

    ValorObjetivo = pl.value(prob.objective)

    return X,A,ValorObjetivo
