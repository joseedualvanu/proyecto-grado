def generadorpedidos(archivo_pedidos_1,archivo_pedidos_2,CantPedidosInput,CP,CB):
    '''
    Description:
        Módulo auxiliar.
        Se generan aleatoriamente los archivos necesarios.
        Es el input necesario para ejecutar el programa.
        Pedido_BE y Pedido_PCP.

    Args:
        archivo_pedidos_1 (str): Ubicación y nombre del archivo con los pedidos y bloques
        archivo_pedidos_2 (str): Ubicación y nombre del archivo con los pedidos y codigos postal
        CantPedidosInput (int): Cantidad de pedidos a generar
        CB (int): Cantidad de bloques
        CP (list): Lista con los codigos postales

    Returns:
        archivo_pedidos_1 (csv): Archivo con el resultado de pedidos y bloques
        archivo_pedidos_2 (csv): Archivo con el resultado de pedidos y codigos postales
    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
    '''

    import random
    import csv

    # Listado de pedidos/tipo de pedido/bloques elegidos

    #CantPedidosInput = 200
    # CantPedidosInputMin = CantPedidosInput - 5
    # CantPedidosInputMax = CantPedidosInput + 5

    #CantPedidosInput = random.randint(CantPedidosInputMin,CantPedidosInputMax)
    print('CantidadPedidos')
    print(CantPedidosInput)

    CantPedidosRange = range(1,CantPedidosInput+1)

    ListaPedidos = list()
    Lista = list()
    # PARA MEJORAR
    Lista.append("NroOrden")
    Lista.append("TipoPedido")
    Lista.append("1Elecc")
    Lista.append("2Elecc")
    Lista.append("3Elecc")
    Lista.append("4Elecc")
    Lista.append("5Elecc")
    Lista.append("6Elecc")
    Lista.append("7Elecc")
    ListaPedidos.append(Lista)

    for i in CantPedidosRange:
        # Se crea la Lista para pedido i
        Lista = list()
        # Ingreso de Nro de Pedido
        Lista.append(100 + i)

        porcentajeDelivery = 60
        porcentajePickup = 100 - porcentajeDelivery

       # TipoPedido = random.randint(1,2)
       # Es delivery o pick up de forma aleatoria
        TipoPedidoList = random.choices([1,2] , weights=[porcentajeDelivery,porcentajePickup] , k= 1)
        TipoPedido = TipoPedidoList[0]

        #SOLO DELIVERY
        # TipoPedido = 1

    #   print('TipoPedido')
    #   print(TipoPedido)

       # Ingreso de Tipo de Pedido
        Lista.append(TipoPedido)

       # Ingreso de AA
        # Lista.append(4)

        # Caso de testear muchos pedidos en un bloque (4 en este caso)
        # if i < 70:
        #     Lista.append(5)

        # else:

        #     if i < 140:
        #         Lista.append(6)

        #     else:

        #         if i < 210:
        #             Lista.append(7)

        #         else:

        #Delivery
        if TipoPedido == 1:

            #Cantidad de bloques elegidos
            # Tope = CB
            # CantBloques = random.randint(1,Tope)
            # CantBloques = 4


            # Cantidad de bloques a elegir de 3
            # CantBloques = int(random.choices([1,2,3,4,5,6,7] , weights=[40,30,30,0,0,0,0] , k= 1)[0])
            # Cantidad de bloques a elegir de 7
            CantBloques = int(random.choices([1,2,3,4,5,6,7] , weights=[20,20,20,10,10,10,10] , k= 1)[0])

            # Distribucion de los pedidos

            # EQUILIBRADA (misma ponderacion para cualquier bloque)
            # BloqueSemilla = random.randint(1,CB)

            # NO EQUILIBRADA (ponderacion desigual para cada bloque)
            BloqueSemilla = int(random.choices([1,2,3,4,5,6,7] , weights=[20,5,5,5,15,20,30] , k= 1)[0])
            # BloqueSemilla = int(random.choices([1,2,3,4,5,6,7] , weights=[9,9,9,13,20,20,20] , k= 1)[0])

            PosicionSemilla = random.randint(1,CantBloques)

            BloqueInicial =  BloqueSemilla - PosicionSemilla + 1

            Cont = 1
            Bloque = BloqueInicial
            while Cont <= CantBloques:

                # Se agrega unicamente si es positivo
                if Bloque >= 1:
                    # Ingreso de Tipo de Pedido
                    Lista.append(Bloque)

                Bloque = Bloque + 1
                Cont = Cont + 1

                if Bloque > CB:
                        break
        else:
            BloqueInicial = random.randint(1,CB)
      #       print('BloqueInicial')
      #       print(BloqueInicial)
            Lista.append(BloqueInicial)

        # Se agrega pedido a ListaPedidos
        ListaPedidos.append(Lista)

    #print(ListaPedidos)

    # Escribimos el archivo de lista Pedidos
    with open(archivo_pedidos_1, "w", newline="") as f1:
        writer = csv.writer(f1)
        writer.writerows(ListaPedidos)
    #f1.close() no es necesario porque es un content manager (Jose)

    # Listado de pedidos / codigo postal
    # Se crea la Lista para pedido/CP i
    Lista_CP = list()

    # Resta definir a cuantos codigos postales se entrega hoy en dia
    # Asumimos 15
    # CantCodPostales = random.randint(10,10)
    CantCodPostales = 15

    #Tomamos estos 10 codigos postales
    # CP = [11100 , 11200 , 11300 , 11400, 11500 , 11600 , 11700 , 11800 , 11900 , 12000]

    CP_Aux = CP[0:CantCodPostales]

    Lista = list()
    Lista.append("NroOrden")
    Lista.append("Código Postal")
    Lista_CP.append(Lista)

    for i in CantPedidosRange:
        # Se crea la Lista para pedido i
        Lista = list()
        # Ingreso de Nro de Pedido
        Lista.append(100 + i)
        CP_Elegido = random.choice(CP_Aux)
        # CP_Elegido = int(random.choices(CP_Aux , weights=[14,14,14,10,10,5,5,5,5,5,5,5,1,1,1] , k= 1)[0])

        Lista.append(CP_Elegido)

        # Se agrega pedido a ListaPedidos
        Lista_CP.append(Lista)

   # print(Lista_CP)

    with open(archivo_pedidos_2, "w", newline="") as f2:
        writer = csv.writer(f2)
        writer.writerows(Lista_CP)
    #f2.close() no es necesario porque es un content manager (Jose)

    print("-------------------------------------")
    print("Se genero archivo de pedidos exitosamente.")
