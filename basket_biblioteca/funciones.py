import json

# Carga de datos
def cargar_datos_json(ruta_archivo:str) -> list:
    """
    \nQué hace:
    - Carga los datos del archivo .json y los devuelve en una lista.
    \nParámetros:
    - ruta_archivo (str): la ruta del archivo .json.
    \nDevuelve:
    - list: los datos en formato list.
    """
    
    # Abre el archivo designado en ejercicio_parcial.py
    with open(ruta_archivo, encoding='utf-8') as file:
        # Guarda los datos de la lista "jugadores"
        data = json.load(file)
        data_dream_team = data['jugadores']

    return data_dream_team

# Menú
def menu_de_opciones():
    """
    \nQué hace:
    - Imprime el menú de opciones.
    """
    # Muestra todas las opciones disponibles
    mensaje = '\n\nMenú de opciones: '
    mensaje += '\n1) Lista de todos los jugadores con sus posiciones.'
    mensaje += '\n2) Todas las estadísticas de un jugador según su índice.'
    mensaje += '\n3) Todas los logros de un jugador según su nombre.'
    mensaje += '\n4) Mostrar el promedio de puntos por partido, ordenando los nombres de manera ascendente.'
    mensaje += '\n5) Mostrar si el jugador ingresado es miembro del Salón de la Fama del Baloncesto.'
    mensaje += '\n6) Mostrar el jugador con mayor cantidad de rebotes totales.'
    mensaje += '\n7) Mostrar el jugador con mayor porcentaje tiros de campo.'
    mensaje += '\n8) Mostrar el jugador con mayor cantidad de asistencias totales.'
    mensaje += '\n9) Mostrar los jugadores con un promedio de puntos por partido mayor a X valor.'
    mensaje += '\n10) Mostrar los jugadores con un promedio de rebotes por partido mayor a X valor.'
    mensaje += '\n11) Mostrar los jugadores con un promedio de asistencias por partido mayor a X valor.'
    mensaje += '\n12) Mostrar el jugador con mayor cantidad de robos totales.'
    mensaje += '\n13) Mostrar el jugador con mayor cantidad de bloqueos totales.'
    mensaje += '\n14) Mostrar los jugadores con un porcentaje de tiros libres mayor a X valor.'
    mensaje += '\n15) Mostrar promedio de puntos por partido del equipo sin contar al menor valor.'
    mensaje += '\n16) Mostrar el jugador con la mayor cantidad de logros.'
    mensaje += '\n17) Mostrar los jugadores con un porcentaje de tiros triples mayor a X valor.'
    mensaje += '\n18) Mostrar el jugador con mayor cantidad de temporadas jugadas.'
    mensaje += '\n19) TODAVÍA NO'
    mensaje += '\n20) Exportar posiciones de los jugadores sobre todas las estadísticas.'
    mensaje += '\n0) Cerrar el programa.\n'
    
    print(mensaje)

# Funciones de validación y reformateo
def validar_valor_numerico(numero:str) -> bool:
    """
    \nQué hace:
    - Recibe una string y verifica si es un número entero.
    \nParámetros:
    - numero (str): el número a verificar.
    \nDevuelve:
    - bool: True si lo es, False si no lo es.
    """
    if numero.isnumeric() == True:
        variable_a_retornar = True
    else:
        variable_a_retornar = False
    
    return variable_a_retornar

def quitar_guiones_del_nombre(texto:str) -> str:
    """
    \nQué hace:
    - Reemplaza los guiones bajos de un texto por espacios.
    \nParámetros:
    - texto (str): el texto a modificar.
    \nDevuelve:
    - str: el texto modificado.
    """
    lista_texto_separado = texto.split('_')
    texto_reescrito = ' '.join(lista_texto_separado)
    
    return texto_reescrito

def quicksort(lista_original:list,flag_orden:bool) -> list:
    """
    \nQué hace:
    - Ordena una lista de números de menor a mayor o de mayor a menor.
    \nParámetros:
    - lista (list): la lista a ordenar.
    - flag_ordenn (bool): de menor a mayor si es True, de mayor a menor
    si es False.
    \nDevuelve:
    - list: la lista ordenada.
    """
    # Se cream dos listas vacías
    lista_derecha = []
    lista_izquierda = []
    
    # Si recibe una lista de menos de 2 elementos, la returnea directo
    if len(lista_original) < 2:
        return lista_original
    
    else:
        pivot = lista_original[0]
        for indice in lista_original[1:]:
            if flag_orden == True:
                if indice > pivot:
                    lista_derecha.append(indice)
                else:
                    lista_izquierda.append(indice)
            else:
                if indice < pivot:
                    lista_derecha.append(indice)
                else:
                    lista_izquierda.append(indice)                
    
    # Se vuelve a combinar todo
    lista_final = quicksort(lista_izquierda,flag_orden)
    lista_final.append(pivot)
    lista_final.extend(quicksort(lista_derecha,flag_orden))
    return lista_final

# Mensajes recurrentes
def mensaje_valor_ingresado_valido(valor_ingresado:str):
    """
    \nQué hace:
    - Muestra un mensaje que aparecerá cuando un dato se ingrese correctamente.
    \nParámetros:
    - valor_ingresado (str): el valor ingresado
    """
    print('------------')
    print('Ingresó el valor "{0}".\n'.format(valor_ingresado))

def mensaje_opcion_finalizada():
    """
    \nQué hace:
    - Muestra un mensaje que aparecerá cuando una opción finalice totalmente.
    """
    input('\nPresione ENTER para volver al menú principal.')
    print('\n\n')    

def mensaje_valor_ingresado_invalido():
    """
    \nQué hace:
    - Muestra un mensaje que aparecerá al ingresar un dato inválido.
    """
    print('------------')
    print('ERROR: Ingresó un valor inválido.')
    input('Presione ENTER para volver al menú principal.')
    print('\n\n')

# PUNTO 1
def mostrar_nombre_y_posicion(lista:list):
    """
    \nQué hace:
    - Muestra el nombre y la posición de cada jugador en base a los datos de
    una lista.
    \nParámetros:
    - lista (list): la lista de datos.
    """
    for indice in lista:
        # Busca el nombre y la posición de cada jugador en la lista
        nombre_jugador = indice['nombre']
        posicion_jugador = indice['posicion']
        # La imprime con el formato especificado
        print('{0} - {1}'.format(nombre_jugador,posicion_jugador))
    
    mensaje_opcion_finalizada()

# PUNTO 2
def mostrar_estadisticas_de_jugador_especifico(lista:list):
    """
    \nQué hace:
    - Muestra las estadísticas de un jugador en base a su índice en la lista.
    Al final da la opción de exportar los datos a .csv gracias a la función
    "exportar_estadisticas_de_jugador_especifico".
    \nParámetros:
    - lista (list): la lista a analizar.
    """
    # Ya que hay 12 jugadores, pide que sea un valor de 0 a 11
    indice = input('Ingrese un número del 0 al 11 (inclusives): ')
    
    if validar_valor_numerico(indice) == True:
        # Pasa el número ingresado a entero
        indice_casteado = int(indice)
        if indice_casteado > -1 and indice_casteado < 12:
            mensaje_valor_ingresado_valido(indice)
            
            # Crea dos diccionarios, el primero tiene el nombre y la posición,
            # mientras que el otro tiene todas las estadísticas
            dict_jugador = lista[indice_casteado]
            dict_stats = dict_jugador['estadisticas']
            
            # Muestra todos los datos en pantalla
            mensaje = 'Nombre: {0}'.format(dict_jugador['nombre'])
            mensaje += '\nPosición: {0}'.format(dict_jugador['posicion'])
            mensaje += '\nEstadísticas:'
            mensaje += '\n- Temporadas: {0}'.format(dict_stats['temporadas'])
            mensaje += '\n- Puntos totales: {0}'.format(dict_stats['puntos_totales'])
            mensaje += '\n- Promedio de puntos por partido: {0}'.format(dict_stats['promedio_puntos_por_partido'])
            mensaje += '\n- Rebotes totales: {0}'.format(dict_stats['rebotes_totales'])
            mensaje += '\n- Promedio de rebotes por partido: {0}'.format(dict_stats['promedio_rebotes_por_partido'])
            mensaje += '\n- Asistencias totales: {0}'.format(dict_stats['asistencias_totales'])
            mensaje += '\n- Promedio de asistencias por partido: {0}'.format(dict_stats['promedio_asistencias_por_partido'])
            mensaje += '\n- Robos totales: {0}'.format(dict_stats['robos_totales'])
            mensaje += '\n- Bloqueos totales: {0}'.format(dict_stats['bloqueos_totales'])
            mensaje += '\n- Porcentaje de tiros de campo: {0}'.format(dict_stats['porcentaje_tiros_de_campo'])
            mensaje += '\n- Porcentaje de tiros libres: {0}'.format(dict_stats['porcentaje_tiros_libres'])
            mensaje += '\n- Porcentaje de tiros triples: {0}'.format(dict_stats['porcentaje_tiros_triples'])
            print(mensaje)
            
            # Usa los diccionarios creados para exportar las estadísticas
            exportar_estadisticas_de_jugador_especifico(dict_jugador,dict_stats)

            mensaje_opcion_finalizada()
        else:
            mensaje_valor_ingresado_invalido()
    else:
        mensaje_valor_ingresado_invalido()

# PUNTO 3
def exportar_estadisticas_de_jugador_especifico(jugador:dict,estadisticas:dict):
    """
    \nQué hace:
    - Exporta las estadísticas del jugador seleccionado en la opción 2 a un
    archivo .csv con su nombre
    \nParámetros:
    - jugador (dict): el nombre y la posición del jugador.
    - estadisticas (dict): las estadísticas del jugador.
    """
    # La ruta de exportación general de los .csv
    ruta_export = 'exports/'
    
    # Pregunta si se debe exportar o volver al menú
    print('\n¿Desea exportar los datos a un archivo.csv?')
    opcion = input('Ingrese "1" para exportar, o cualquier otra cosa para no hacerlo: ')
    
    if opcion == '1':
        # Todos los valores de estadísticas pasan a estar en una lista
        lista_estadisticas = list(estadisticas.values())
        
        # Se crea la primera fila del .csv
        primera_fila = 'Nombre,'
        primera_fila += 'Posición,'
        primera_fila += 'Temporadas,'
        primera_fila += 'Puntos totales,'
        primera_fila += 'Promedio de puntos por partido,'
        primera_fila += 'Rebotes totales,'
        primera_fila += 'Promedio de rebotes por partido,'
        primera_fila += 'Asistencias totales,'
        primera_fila += 'Promedio de asistencias por partido,'
        primera_fila += 'Robos totales,'
        primera_fila += 'Bloqueos totales,'
        primera_fila += 'Porcentaje de tiros de campo,'
        primera_fila += 'Porcentaje de tiros libres,'
        primera_fila += 'Porcentaje de tiros triples,'
        
        # Se crea la segunda fila del .csv
        segunda_fila = '{0},'.format(jugador['nombre'])
        segunda_fila += '{0},'.format(jugador['posicion'])
        
        # Añade todos los elementos de lista_estadisticas a la segunda fila
        for indice in lista_estadisticas:
            segunda_fila += '{0},'.format(indice)
        
        # Crea la ruta de exportación individual
        ruta_export += jugador['nombre']
        ruta_export += '.csv'
        
        # Abre (o crea) el archivo .csv seleccionado y escribe las dos filas
        with open(ruta_export, 'w+') as file:
            file.write('{0}\n'.format(primera_fila))
            file.write(segunda_fila)            
        
        print('\nLos datos fueron exportados al archivo')
    else:
        print('\nNo se exportaron los datos.')

# PUNTO 4
def mostrar_logros_de_jugador_especifico(lista:list):
    """
    \nQué hace:
    - Muestra los logros de un jugador en base a su nombre.
    \nParámetros:
    - lista (list): la lista a analizar.
    """
    nombre = input('Ingrese el nombre completo del jugador: ')
    mensaje_valor_ingresado_valido(nombre)
    
    # Se pasa el nombre a minúsculas
    nombre_minus = nombre.lower()
    
    # Se inicia un contador en 0 y una flag para ver si hay una coincidencia
    contador = 0
    flag_jugador_encontrado = False
    
    for indice in lista:
        # El nombre de la lista se pasa a minúsculas para compararlo
        nombre_lista = indice['nombre'].lower()
        if nombre_minus == nombre_lista:
            # Guarda el diccionario del jugador y la lista de logros
            dict_jugador = lista[contador]
            list_logros = dict_jugador['logros']
            # Cambia la flag a True
            flag_jugador_encontrado = True
        contador += 1
    
    # Si hubo una coincidencia, muestra todos los datos en pantalla
    if flag_jugador_encontrado == True:    
        mensaje = 'Nombre: {0}'.format(dict_jugador['nombre'])
        mensaje += '\nPosición: {0}'.format(dict_jugador['posicion'])
        mensaje += '\nLogros:'
        mensaje += '\n- '
        # Separa a todos los elementos de la lista con "\n- "
        mensaje += '\n- '.join(list_logros)
        print(mensaje)
    
    # De lo contrario, muestra otro mensaje
    else:
        print('No se encontró a un jugador con ese nombre.')

    mensaje_opcion_finalizada()

# PUNTO 5
def mostrar_promedio_puntos_por_partido_en_orden_alfabético_ascendente(lista:list):
    """
    \nQué hace:
    - Calcula y muestra el promedio de puntos por partido, ordenando los
    nombres de manera ascendente.
    \nParámetros:
    - lista (list): la lista a analizar.
    """
    # Se crean una lista y un diccionario vacíos
    lista_nombres_ordenada = []
    diccionario_nombres_con_puntos = {}
    
    # Se añaden los nombres a la lista y los puntos al diccionario
    for indice in lista:
        lista_nombres_ordenada.append(indice['nombre'])
        diccionario_nombres_con_puntos[indice['nombre']] = indice['estadisticas']['promedio_puntos_por_partido']
    
    # Se ordena la lista en forma ascendente
    lista_nombres_ordenada = sorted(lista_nombres_ordenada)

    # Se imprimen los puntos junto a los nombres ordenados
    for indice in lista_nombres_ordenada:
        puntos = diccionario_nombres_con_puntos[indice]
        print('{0} - {1}'.format(indice,puntos))

    mensaje_opcion_finalizada()

# PUNTO 6
def mostrar_si_es_del_salon_de_la_fama(lista:list):
    """
    \nQué hace:
    - 
    \nParámetros:
    - lista (list):
    """
    nombre = input('Ingrese el nombre completo del jugador: ')
    mensaje_valor_ingresado_valido(nombre)
    
    # Se pasa el nombre a minúsculas
    nombre_minus = nombre.lower()
    
    # Se crea una flag para ver si hay una coincidencia
    flag_jugador_encontrado = False
    
    for indice in lista:
        # El nombre de la lista se pasa a minúsculas para compararlo
        nombre_lista = indice['nombre'].lower()
        if nombre_minus == nombre_lista:
            # Se busca una string específica en la lista de logros
            if 'Miembro del Salon de la Fama del Baloncesto' in indice['logros']:
                print('Este jugador sí forma parte del Salon de la Fama del Baloncesto.')
            else:
                print('Este jugador no está en el Salon de la Fama del Baloncesto.')
            # Cambia la flag a True
            flag_jugador_encontrado = True
            
    # Si no se encontró al jugador, se muestra este mensaje
    if flag_jugador_encontrado == False:
        print('No se encontró a un jugador con ese nombre.')

    mensaje_opcion_finalizada()

# PUNTOS 7, 8, 9, 13, 14, 19
def mostrar_el_jugador_con_mayor_estadistica(lista:list,dato:str):
    """
    \nQué hace:
    - Muestra al jugador que tenga el mayor número de X estadística.
    \nParámetros:
    - lista (list): la lista a analizar.
    - dato (str): el dato a buscar. DEBE SER UNO DE LOS SIGUIENTES:
    "rebotes_totales", "porcentaje_tiros_de_campo", "asistencias_totales",
    "robos_totales", "bloqueos_totales", o "temporadas".
    """
    # Se obtiene el dato a buscar sin guiones bajos
    dato_reescrito = quitar_guiones_del_nombre(dato)
    
    # Se crea una flag para la primera vuelta del for
    flag_primera_vuelta = True
    
    for indice in lista:
        # Se sobreescribe el dato mayor si el nuevo dato es mayor
        # o es la primera vuelta
        if flag_primera_vuelta == True or indice['estadisticas'][dato] > dato_mayor:
            dato_mayor = indice['estadisticas'][dato]
            nombre_mayor = indice['nombre']
        # Cambia la flag a False
        flag_primera_vuelta = False
    
    # Muestra todos los datos en pantalla
    print('El jugador con mayor cantidad de {0} es {1}, con un total de {2}.'
          .format(dato_reescrito,nombre_mayor,dato_mayor))

    mensaje_opcion_finalizada()

# PUNTOS 10, 11, 12, 15, 18
def mostrar_jugadores_con_estadistica_sobre_valor_ingresado(lista:list,dato:str):
    """
    \nQué hace:
    - Muestra a todos los jugadores que tengan un valor superior al valor
    ingresado en una estadística específica.
    \nParámetros:
    - lista (list):
    - dato (str): el dato a buscar. DEBE SER UNO DE LOS SIGUIENTES:
    "promedio_puntos_por_partido", "promedio_rebotes_por_partido",
    "promedio_asistencias_por_partido","porcentaje_tiros_libres",
    o "porcentaje_tiros_triples".
    """
    valor = input('Ingrese el valor a usar: ')
    mensaje_valor_ingresado_valido(valor)
    
    # Se crean una lista y un diccionario vacíos
    lista_jugadores_superiores = []
    dict_nombres = {}
    
    # Se valida el valor ingresado
    if validar_valor_numerico(valor) == True:
        valor = float(valor)

        # Se obtiene el dato a buscar sin guiones bajos
        dato_reescrito = quitar_guiones_del_nombre(dato)
        
        # Se agregan los nombres a la lista y los valores al diccionario
        for indice in lista:
            if indice['estadisticas'][dato] > valor:
                lista_jugadores_superiores.append(indice['nombre'])
                dict_nombres[indice['nombre']] = indice['estadisticas'][dato]
        
        # Si hay resultados, se mostrará este mensaje
        if len(lista_jugadores_superiores) > 0:
            mensaje = 'Los jugador(es) con un {0} mayor a {1} son:'.format(dato_reescrito,valor)
            
            for indice in lista_jugadores_superiores:
                mensaje += '\n- {0} ({1})'.format(indice,dict_nombres[indice])
        
        # De lo contrario, se mostrará este otro
        else:
            mensaje = 'Nadie tiene un {0} mayor a {1}.'.format(dato_reescrito,valor)
        
        print(mensaje)
        
        mensaje_opcion_finalizada()
        
    else:
        mensaje_valor_ingresado_invalido()

# PUNTO 16
def mostrar_promedio_puntos_por_partido_salvo_por_el_menor_valor(lista:list):
    """
    \nQué hace:
    - Promedia los puntos por partido del equipo dejando de lado al que
    tenga menos puntos por partido.
    \nParámetros:
    - lista (list): la lista a analizar.
    """
    # Se crea una lista vacía
    lista_puntos_por_partido = []
    
    # Se añaden todos los puntos a la lista
    for indice in lista:
        lista_puntos_por_partido.append(indice['estadisticas']['promedio_puntos_por_partido'])
    
    # Se ordena la lista de menor a mayor
    lista_puntos_por_partido = quicksort(lista_puntos_por_partido,True)
    
    # Se suma todo, luego se resta el dato menor, después se divide por el
    # resto de jugadores y finalmente se redondea en 2 decimales
    promedio = sum(lista_puntos_por_partido) - lista_puntos_por_partido[0]
    promedio = promedio / (len(lista_puntos_por_partido) - 1)
    promedio = round(promedio, 2)
    
    print('El promedio resultante es de {0}.'.format(promedio))

    mensaje_opcion_finalizada()

# PUNTO 17
def mostrar_jugador_con_mas_logros(lista:list):
    """
    \nQué hace:
    - Muestra al jugador con la mayor cantidad de logros.
    \nParámetros:
    - lista (list): la lista a analizar.
    """    
    # Se crea una flag para la primera vuelta del for
    flag_primera_vuelta = True
    
    for indice in lista:
        # Se sobreescribe el dato mayor si el nuevo dato es mayor
        # o es la primera vuelta
        if flag_primera_vuelta == True or len(indice['logros']) > cantidad_mayor:
            cantidad_mayor = len(indice['logros'])
            nombre_mayor = indice['nombre']
        # Cambia la flag a False
        flag_primera_vuelta = False
    
    # Muestra todos los datos en pantalla
    print('El jugador con mayor cantidad de logros es {0}, con un total de {1}.'
          .format(nombre_mayor,cantidad_mayor))

    mensaje_opcion_finalizada()

# PUNTO 23
def conseguir_lista_de_jugadores_filtrada(lista:list):
    lista_de_nombres_filtrada = []
    
    for indice in lista:
        lista_de_nombres_filtrada.append(indice['nombre'])
    
    return lista_de_nombres_filtrada

def asignar_posicion_a_los_jugadores_segun_un_dato(lista:list,dato:str) -> list:
        
    # Lista de nombres en orden original
    lista_de_jugadores_original = conseguir_lista_de_jugadores_filtrada(lista)
    
    # Lista en la que se agregarán los datos en orden original
    lista_de_valores_original = []
    
    # Lista de nombres ordenados de mejor a peor según un dato
    lista_de_jugadores_ordenada = []
    
    # Lista de las posiciones según un dato en el orden original
    lista_de_posiciones = []    
    
    for indice in lista:
        # Se agrega el valor del dato a una lista y el nombre del jugador a otra
        lista_de_valores_original.append(indice['estadisticas'][dato])
    
    # Se ordena la lista_de_valores_original de mejor a peor
    lista_de_valores_ordenada = quicksort(lista_de_valores_original,False)
    
    # Se iteran dos listas, una dentro de otra, para después compararlos y
    # crear una lista de nombres ordenada. Es importante que lista_de_valores_ordenada
    # sea la primera en iterarse ya que así los elementos se comparan en
    # el orden correcto.    
    for indice_lista_ordenada in lista_de_valores_ordenada:
        for indice_lista_original in lista:
            # Compara los valores. Si son iguales, los agrega a lista_de_jugadores_ordenada.
            if indice_lista_ordenada == indice_lista_original['estadisticas'][dato]:
                lista_de_jugadores_ordenada.append(indice_lista_original['nombre'])

    # De forma similar a antes, se iteran dos listas, una dentro de otra.
    # Esta vez se busca averiguar la posición del jugador en el orden que
    # aparecen en la lista original.
    for indice_primero in lista_de_jugadores_original:
        for indice_segundo in lista_de_jugadores_ordenada:
            # Compara los valores. Si son iguales, se añade un elemento a la
            # lista según el indice en el que se encuentran y le suma 1, porque
            # las listas empiezan en el indice 0 y esa no es una posición válida.
            if indice_primero == indice_segundo:
                valor_a_agregar = lista_de_jugadores_ordenada.index(indice_segundo) + 1
                lista_de_posiciones.append(valor_a_agregar)
    
    return lista_de_posiciones
    
def exportar_posiciones_de_todas_las_estadisticas(lista:list):

    # Se consiguen las posiciones de todas las estadísticas pedidas
    lista_posiciones_puntos = asignar_posicion_a_los_jugadores_segun_un_dato(lista,'puntos_totales')
    lista_posiciones_rebotes = asignar_posicion_a_los_jugadores_segun_un_dato(lista,'rebotes_totales')
    lista_posiciones_asistencias = asignar_posicion_a_los_jugadores_segun_un_dato(lista,'asistencias_totales')
    lista_posiciones_robos = asignar_posicion_a_los_jugadores_segun_un_dato(lista,'robos_totales')
    
    # También se vuelve a traer la lista de jugadores original
    lista_de_jugadores_original = conseguir_lista_de_jugadores_filtrada(lista)
    
    # Se inicializa un contador en 0
    contador = 0
    
    # Se crea la primera fila del futuro texto a exportar a .csv
    texto_csv = 'Jugadores,Puntos,Rebotes,Asistencias,Robos\n'
    
    # Se crea un while de 12 pasadas porque hay 12 jugadores
    while contador < len(lista_de_jugadores_original):
        # Se asignan los valores de los indices a las variables para mayor claridad
        indice_jugadores = lista_de_jugadores_original[contador]
        indice_puntos = lista_posiciones_puntos[contador]
        indice_rebotes = lista_posiciones_rebotes[contador]
        indice_asistencias = lista_posiciones_asistencias[contador]
        indice_robos = lista_posiciones_robos[contador]
        
        # Se concatenan todos los datos
        texto_csv += ('{0},{1},{2},{3},{4}\n'.
              format(indice_jugadores,indice_puntos,indice_rebotes,indice_asistencias,indice_robos))
        
        # Se suma 1 al contador
        contador += 1

    # Se asigna la ruta de exportación
    ruta_export = 'exports/posiciones.csv'
    
    # Crea o sobrescribe el archivo .csv y exporta los datos
    with open(ruta_export, 'w+') as file:
        file.write(texto_csv)
    
    print('Los datos fueron exportados con éxito.')
    mensaje_opcion_finalizada()