def visualizacion(CB,resultado,resultadoValidacion,conteoValidacion,resultadoCPBloque,n,resultadoBloqueMO,resultadoPorBloque,Grafica1,Grafica2,Grafica3,Grafica4):
    '''
    Description:

    Args:
        CB ():
        resultado ():
        resultadoValidacion ():
        conteoValidacion ():
        resultadoCPBloque ():
        n ():
        resultadoBloqueMO ():
        resultadoPorBloque ():
        Grafica1 ():
        Grafica2 ():
        Grafica3 ():
        Grafica4 ():
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
    '''

    # Import the libraries
    import matplotlib.pyplot as plt
    import seaborn as sns
    # import numpy as np
    import pandas as pd
    # import collections

    # GRAFICA MOSTRANDO PEDIDOS POR BLOQUE

    #Titulo de Grafica
    plt.title('Cant Pedidos vs Bloque')

    #Genero el DataFrame para cargar la grafica
    data2 = pd.DataFrame(resultadoPorBloque , index = range(1))

    # Create an lmplot
    grid = sns.barplot(data=data2,  palette="muted")

    #Setear titulos de ejes
    plt.ylabel('Cantidad Pedidos')
    plt.xlabel('Bloque')

    #Guardo Grafica en archivo
    plt.savefig(Grafica1)

    # Show plot
    plt.show()

    # GRAFICA MOSTRANDO PEDIDOS QUE CUMPLEN Y NO CUMPLEN

    #Titulo de Grafica
    titulo = 'Cumplimiento Pedidos - Tot:' + str(conteoValidacion["Total"]) + ' (' + str(round(conteoValidacion["%Cumplimiento"],2)) + '%)'
    plt.title(titulo)

    # Se quita el porcentaje de cumplimiento del dict ya que el eje Y es 'Cant Pedidos' no '%' & Total de Pedidos
    conteoValidacion.popitem()
    conteoValidacion.popitem()

    #Genero el DataFrame para cargar la grafica
    data3 = pd.DataFrame(conteoValidacion , index = range(1))

    # Create an lmplot
    grid = sns.barplot( data=data3,  palette="muted")

    #Setear titulos de ejes
    plt.ylabel('Cantidad Pedidos')
    #plt.xlabel('')

    #Guardo Grafica en archivo
    plt.savefig(Grafica2)

    # Show plot
    plt.show()

    # GRAFICA MOSTRANDO CANT DE COD POSTALES POR BLOQUE

    #Titulo de Grafica
    plt.title('Codigo Postal vs Bloque')

    #Genero el DataFrame para cargar la grafica
    data3 = pd.DataFrame(resultadoCPBloque , index = range(1))

    # Create an lmplot
    grid = sns.barplot( data=data3,  palette="muted")

    #Setear titulos de ejes
    plt.ylabel('Cantidad CP')
    plt.xlabel('Bloque')

    #Guardo Grafica en archivo
    plt.savefig(Grafica3)

    # Show plot
    plt.show()

    # GRAFICA MOSTRANDO CANT MO POR BLOQUE

    #Titulo de Grafica
    plt.title('Demanda Personal vs Bloque')

    #Genero el DataFrame para cargar la grafica
    data3 = pd.DataFrame(resultadoBloqueMO , index = range(1))

    # Create an lmplot
    grid = sns.barplot( data=data3,  palette="muted")

    #Setear titulos de ejes
    plt.ylabel('Personal')
    plt.xlabel('Bloque')

    #Guardo Grafica en archivo
    plt.savefig(Grafica4)

    # Show plot
    plt.show()


    # GRAFICA MOSTRANDO PEDIDOS POR BLOQUE ESPECIFICANDO SI CUMPLEN O NO CUMPLEN

    # GRAFICA TORTA CON %CUMPLIMIENTO
