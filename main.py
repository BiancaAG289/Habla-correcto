"""
main.py - Versión 2 (Habla Correcto)
El director del juego. Conecta los menús, el procesamiento de voz y el motor de combate.
"""
import sys
import random

# Importamos nuestros módulos locales
import idiomas
import diccionario
import jugadores
import combate
import reconocimiento
import traductor

def mostrar_ayuda_idiomas():
    """Muestra de forma ordenada los 14 idiomas disponibles y sus códigos."""
    print("\n🌍 ===== IDIOMAS DISPONIBLES =====")
    columnas = list(idiomas.IDIOMAS.items())
    # Los mostramos en dos columnas para que se vea ordenado en la terminal
    for i in range(0, len(columnas), 2):
        cod1, datos1 = columnas[i]
        col1 = f"{cod1}: {datos1['nombre']}"
        if i + 1 < len(columnas):
            cod2, datos2 = columnas[i+1]
            col2 = f"{cod2}: {datos2['nombre']}"
            print(f"  🔹 {col1:<20} 🔹 {col2}")
        else:
            print(f"  🔹 {col1}")
    print("====================================")

def mostrar_como_jugar():
    """Explica las reglas y mecánicas del juego al usuario."""
    combate.limpiar_pantalla()
    print("📖 ================= ¿CÓMO JUGAR? ================= 📖")
    print("\n1. 👥 CONFIGURA LOS EQUIPOS:")
    print("   Elige la modalidad (desde 1v1 hasta 5v5) e ingresa los nombres.")
    print("\n2. 🌍 SELECCIONA EL DESAFÍO:")
    print("   Elige el idioma de origen, el idioma al que vas a traducir,")
    print("   la dificultad (facil/medio/dificil) y tipo (palabras/oraciones).")
    print("\n3. ⚔️ EL COMBATE POR TURNOS:")
    print("   Cada jugador tiene 3 vidas ❤️ y jugará por turnos.")
    print("   El juego te dará una frase en el idioma origen y tendrás 5 segundos")
    print("   para decirla en voz alta traducida al idioma destino.")
    print("\n4. 🎙️ VALIDACIÓN INTELIGENTE:")
    print("   El sistema te escuchará. Si coincide con el diccionario local")
    print("   o con la traducción de respaldo online, ¡salvas tu vida! Si no, pierdes una ❤️.")
    print("\n🏁 ¡El último equipo con jugadores en pie gana la partida!")
    print("======================================================")
    input("\n⌨️ Presiona ENTER para volver al menú principal...")

def verificar_desafio_turno(jugador, idioma_origen, idioma_destino, nivel, tipo_desafio):
    """
    Función de validación (Callback) para el motor de turnos.
    Selecciona el reto, activa el micrófono mediante reconocimiento.py y valida el resultado.
    """
    # 1. Seleccionar un desafío aleatorio del diccionario universal
    lista_desafios = diccionario.diccionario[nivel][tipo_desafio]
    desafio = random.choice(lista_desafios)
    
    # CONTROL DE SEGURIDAD (Evita el KeyError): Si falta el idioma en este desafío específico
    if idioma_origen not in desafio or idioma_destino not in desafio:
        print(f"\n⚠️ Nota: El desafío seleccionado no cuenta con traducción directa.")
        print("🔍 Usando el traductor automático para generar el reto...")
        try:
            # Si falta en el diccionario local, generamos la frase base dinámicamente
            frase_original = desafio.get(idioma_origen) or list(desafio.values())[0]
            traduccion_local = traductor.GoogleTranslator(source=idioma_origen, target=idioma_destino).translate(frase_original).lower().strip()
        except Exception:
            print("❌ Error crítico al generar el desafío. El turno se considerará válido para no penalizar.")
            return True
    else:
        frase_original = desafio[idioma_origen]
        traduccion_local = desafio[idioma_destino].lower().strip()
    
    print(f"\n🗣️ Tu frase en '{idiomas.IDIOMAS[idioma_origen]['nombre']}' es: **{frase_original}**")
    print(f"🎯 Debes decirla traducida al '{idiomas.IDIOMAS[idioma_destino]['nombre']}'.")
    
    # 2. Capturar el audio usando el módulo especializado de reconocimiento
    codigo_speech = idiomas.IDIOMAS[idioma_destino]["speech"]
    print("🎤 Grabando... ¡HABLA AHORA!")
    respuesta_usuario = reconocimiento.capturar_y_reconocer(codigo_speech)
    
    if not respuesta_usuario:
        jugador.registrar_error(tiempo=5.0)
        print(f"❌ No se detectó respuesta válida. Se esperaba: '{traduccion_local}'")
        return False
        
    print(f"📝 El sistema entendió: '{respuesta_usuario}'")
    
    # 3. Validar usando el traductor (Búsqueda local + respaldo online con deep_translator)
    es_correcto = traductor.validar_traduccion(
        respuesta_usuario, 
        traduccion_local, 
        frase_original, 
        idioma_origen, 
        idioma_destino
    )
    
    if es_correcto:
        jugador.registrar_acierto(tiempo=3.0, tipo=tipo_desafio[:-1])
        return True
    else:
        jugador.registrar_error(tiempo=5.0)
        print(f"❌ Incorrecto. La respuesta esperada era: '{traduccion_local}'")
        return False

def menu_principal():
    while True:
        combate.limpiar_pantalla()
        print("🎙️ ========================================= 🎙️")
        print(" 🎉  BIENVENIDO A HABLA CORRECTO - V2 (EXPANSIÓN) 🎉")
        print("🎙️ ========================================= 🎙️")

        print("1. ⚔️ Iniciar Combate Local (Por Equipos)")
        print("2. 📖 ¿Cómo jugar?")
        print("3. 📊 Ver Historial y Estadísticas (Próximamente)")
        print("4. ❌ Salir")

        opcion = input("🟩 Selecciona una opción: ").strip()

        if opcion == "1":
            equipos_configurados = jugadores.crear_equipos()

            if not equipos_configurados:
                continue   # 👈 ESTE continue SÍ ESTÁ BIEN AQUÍ

            while True:
                combate.limpiar_pantalla()
                mostrar_ayuda_idiomas()

                id_origen = input("Idioma origen: ").strip().lower()
                id_destino = input("Idioma destino: ").strip().lower()
                nivel = input("Nivel: ").strip().lower()
                tipo = input("Tipo: ").strip().lower()

                if id_origen not in idiomas.IDIOMAS or id_destino not in idiomas.IDIOMAS:
                    print("Error idioma")
                    input("ENTER...")
                    continue

                if nivel not in ["facil", "medio", "dificil"] or tipo not in ["palabras", "oraciones"]:
                    print("Error nivel/tipo")
                    input("ENTER...")
                    continue

                break  # ✔ sale del bucle de configuración

            def callback_juego(jugador_actual):
                return verificar_desafio_turno(
                    jugador_actual,
                    id_origen,
                    id_destino,
                    nivel,
                    tipo
                )

            combate.iniciar_combate(equipos_configurados, callback_juego)

            input("\nENTER para volver al menú...")

        elif opcion == "2":
            mostrar_como_jugar()

        elif opcion == "3":
            print("Estadísticas luego")

        elif opcion == "4":
            sys.exit()
            
if __name__ == "__main__":
    menu_principal()