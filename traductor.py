# traductor.py - Validación V2

from deep_translator import GoogleTranslator


def traducir(texto, origen, destino):
    try:
        return GoogleTranslator(
            source=origen,
            target=destino
        ).translate(texto).lower().strip()

    except Exception:
        return None


def validar_traduccion(respuesta_usuario, correcta_local,
                       frase_original, origen, destino):

    respuesta_usuario = respuesta_usuario.lower().strip()

    if respuesta_usuario == correcta_local.lower().strip():
        return True

    traduccion_online = traducir(frase_original, origen, destino)

    if traduccion_online and respuesta_usuario == traduccion_online:
        return True

    return False