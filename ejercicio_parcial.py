# Importa todo lo que está dentro de /basket_biblioteca
from basket_biblioteca import *

# La ruta del archivo de los datos a utilizar
ruta_archivo_json = 'dt.json'

# Se crea una lista para utilizarlos más fácilmente
lista_datos_dream_team = cargar_datos_json(ruta_archivo_json)

while True:
    menu_de_opciones()
    opcion = input('Ingrese la opción deseada: ')
    
    # Se valida el valor ingresado
    if validar_valor_numerico(opcion) == True:
        opcion_casteada = int(opcion)
        if opcion_casteada > -1 and opcion_casteada < 28:
            mensaje_valor_ingresado_valido(opcion)
            if opcion_casteada == 1:
                mostrar_nombre_y_posicion(lista_datos_dream_team)
            elif opcion_casteada == 2:
                mostrar_estadisticas_de_jugador_especifico(lista_datos_dream_team)
            elif opcion_casteada == 3:
                mostrar_logros_de_jugador_especifico(lista_datos_dream_team)
            elif opcion_casteada == 4:
                mostrar_promedio_puntos_por_partido_en_orden_alfabético_ascendente(lista_datos_dream_team)
            elif opcion_casteada == 5:
                mostrar_si_es_del_salon_de_la_fama(lista_datos_dream_team)
            elif opcion_casteada == 6:
                mostrar_el_jugador_con_mayor_estadistica(lista_datos_dream_team,'rebotes_totales')
            elif opcion_casteada == 7:
                mostrar_el_jugador_con_mayor_estadistica(lista_datos_dream_team,'porcentaje_tiros_de_campo')
            elif opcion_casteada == 8:
                mostrar_el_jugador_con_mayor_estadistica(lista_datos_dream_team,'asistencias_totales')
            elif opcion_casteada == 9:
                mostrar_jugadores_con_estadistica_sobre_valor_ingresado(lista_datos_dream_team,'promedio_puntos_por_partido',False)
            elif opcion_casteada == 10:
                mostrar_jugadores_con_estadistica_sobre_valor_ingresado(lista_datos_dream_team,'promedio_rebotes_por_partido',False)
            elif opcion_casteada == 11:
                mostrar_jugadores_con_estadistica_sobre_valor_ingresado(lista_datos_dream_team,'promedio_asistencias_por_partido',False)
            elif opcion_casteada == 12:
                mostrar_el_jugador_con_mayor_estadistica(lista_datos_dream_team,'robos_totales')
            elif opcion_casteada == 13:
                mostrar_el_jugador_con_mayor_estadistica(lista_datos_dream_team,'bloqueos_totales')
            elif opcion_casteada == 14:
                mostrar_jugadores_con_estadistica_sobre_valor_ingresado(lista_datos_dream_team,'porcentaje_tiros_libres',False)
            elif opcion_casteada == 15:
                mostrar_promedio_puntos_por_partido_salvo_por_el_menor_valor(lista_datos_dream_team)
            elif opcion_casteada == 16:
                mostrar_jugador_con_mas_logros(lista_datos_dream_team)
            elif opcion_casteada == 17:
                mostrar_jugadores_con_estadistica_sobre_valor_ingresado(lista_datos_dream_team,'porcentaje_tiros_triples',False)
            elif opcion_casteada == 18:
                mostrar_el_jugador_con_mayor_estadistica(lista_datos_dream_team,'temporadas')
            elif opcion_casteada == 19:
                mostrar_jugadores_con_estadistica_sobre_valor_ingresado(lista_datos_dream_team,'porcentaje_tiros_de_campo',True)
            elif opcion_casteada == 20:
                exportar_posiciones_de_todas_las_estadisticas(lista_datos_dream_team)
            elif opcion_casteada == 21:
                mostrar_cantidad_de_jugadores_por_posicion(lista_datos_dream_team)
            elif opcion_casteada == 0:
                input('Ha decidido cerrar el programa. Nos vemos otro día.')
                # El break hace que se deje de ejecutar el código
                break
        else:
            mensaje_valor_ingresado_invalido()
    else:
        mensaje_valor_ingresado_invalido()