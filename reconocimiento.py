# reconocimiento.py - Micrófono V2
# Usa io.BytesIO en memoria (sin archivo temporal) para evitar congelamiento

import io
import time
import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr

SAMPLE_RATE = 16000   # 16kHz óptimo para voz
DURATION    = 5

recognizer = sr.Recognizer()


def capturar_y_reconocer(codigo_idioma="en-US"):
    """Graba audio y devuelve texto reconocido, o None si falla."""
    try:
        # Cuenta regresiva
        for n in ["3", "2", "1", "¡YA!"]:
            print(f"  ⏳ {n}", end="  ", flush=True)
            time.sleep(1)
        print()
        print(f"  🎙️ [Grabando {DURATION}s... ¡habla ahora!]")

        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )
        sd.wait()
        print("  ✅ [Grabación terminada. Procesando...]")

        # WAV en memoria (evita el bug del archivo temporal congelado)
        buffer = io.BytesIO()
        wav.write(buffer, SAMPLE_RATE, audio)
        buffer.seek(0)

        with sr.AudioFile(buffer) as source:
            audio_data = recognizer.record(source)

        texto = recognizer.recognize_google(audio_data, language=codigo_idioma)
        return texto.lower().strip()

    except sr.UnknownValueError:
        print("⚠️ No se entendió el audio.")
        return None
    except sr.RequestError:
        print("⚠️ Error del servicio de reconocimiento.")
        return None
    except Exception as e:
        print(f"⚠️ Error de micrófono: {e}")
        return None