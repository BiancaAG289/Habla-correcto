🗣️ Habla Correcto - V2

Juego educativo de pronunciación por equipos. Di en voz alta la traducción de una palabra o frase y el sistema valida tu respuesta en tiempo real usando reconocimiento de voz.


🚀 Instalación

bashpip install sounddevice scipy speechrecognition deep-translator

Luego ejecuta:

bashpython main.py


🎮 ¿Cómo jugar?


Configura los equipos — elige cuántos jugadores y escribe sus nombres. El juego los divide automáticamente en Equipo Azul y Equipo Rojo.
Elige el desafío — selecciona idioma origen, idioma destino, nivel de dificultad y tipo (palabras u oraciones).
Combate por turnos — cada jugador tiene 3 vidas ❤️. El juego muestra una palabra o frase y tienes 5 segundos para pronunciar la traducción en voz alta.
Gana el último equipo en pie — si todos los jugadores de un equipo pierden sus vidas, el otro equipo gana.



🌍 Idiomas disponibles (14)

CódigoIdiomaCódigoIdiomaesEspañoldeAlemánenInglésruRusofrFrancésjaJaponésitItalianozhChinoptPortuguéskoCoreanoarÁrabehiHinditrTurconlHolandés


📁 Estructura del proyecto

habla_correcto/
├── main.py            ← Menú principal (punto de entrada)
├── combate.py         ← Motor de turnos y fin del juego
├── reconocimiento.py  ← Captura y reconocimiento de voz
├── traductor.py       ← Validación y traducción automática
├── diccionario.py     ← Banco de palabras y frases por nivel
├── idiomas.py         ← Configuración de los 14 idiomas
├── jugadores.py       ← Clase Jugador y creación de equipos
├── estadisticas.py    ← Registro de aciertos, errores y rachas
├── puntuacion.py      ← Cálculo de puntos y bonus
├── records.py         ← Historial guardado en JSON
├── records.json       ← Se crea automáticamente al jugar
└── README.md          ← Este archivo


🏆 Sistema de puntos

NivelPalabrasOracionesFácil10 pts15 ptsMedio20 pts30 ptsDifícil35 pts52 pts


🔥 Bonus racha x3 → +5 pts extra
🔥 Bonus racha x5 → +10 pts extra



🛠️ Tecnologías usadas


Python 3.11+
sounddevice — grabación de audio
scipy — procesamiento de audio WAV
speechrecognition — reconocimiento de voz (Google Speech)
deep-translator — traducción automática de respaldo



👩‍💻 Desarrollado por

Habla Correcto V2 — Expansión multijugador e multiidioma
