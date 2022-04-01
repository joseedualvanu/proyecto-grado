def guardarcsv(resultado,archivo_resultado):
    '''
    Description:
        Se guarda el resultado de un archivo csv
    Args:
        resultado ():
        archivo_resultado ():
    Returns:
        --
    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
    '''

    file = open(archivo_resultado,"w")

    file.write("NroOrden,Elecc")
    file.write("\n")

    for i in resultado:
            #Escribe el indice
            file.write(str(i))
            file.write(",")
            #Escribe el valor
            file.write(str(resultado[i]))
            #Escribe un salto de renglon
            file.write("\n")

    #Cierra el archivo
    file.close()
    print("-------------------------------------")
    print("Se guardo resultado exitosamente.")
    print("-------------------------------------")
