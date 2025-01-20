# Juego del Ahorcado en Python 🎮

¡Bienvenido al **Juego del Ahorcado**! Este proyecto fue desarrollado como un ejercicio de programación en Python para implementar lógica condicional, manejo de listas y bucles. El objetivo del juego es adivinar una palabra letra por letra antes de quedarte sin vidas. 🎯

---

## 📋 Descripción del juego

El **Ahorcado** es un clásico juego de palabras en el que un jugador intenta adivinar una palabra oculta adivinando letras una a una. Cada letra incorrecta disminuye el número de vidas restantes. ¡Adivina todas las letras antes de quedarte sin vidas para ganar! 😄

Características principales:

- Entrada de usuario en tiempo real para adivinar letras.
- Seguimiento de letras usadas para evitar repeticiones.
- Indicador visual de progreso de la palabra oculta.
- Feedback dinámico y mensajes temáticos (¡incluyendo emojis 🎉!).

---

## 🚀 Cómo empezar

### Requisitos previos

Para ejecutar este proyecto necesitas:

- **Python 3.8+**

### Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/JZubiaga13/Ahorcado.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd ahorcado
   ```
3. Ejecuta el script principal:
   ```bash
   python ahorcado.py
   ```

---

## 📖 Instrucciones de uso

1. Ejecuta el programa e introduce la palabra que el jugador tendrá que adivinar. La palabra será automáticamente convertida a mayúsculas.
2. El jugador intentará adivinar la palabra ingresando letras una por una.
3. Cada acierto revela la posición de la letra en la palabra oculta.
4. Cada fallo reduce las vidas del jugador.
5. El juego termina cuando:
   - El jugador adivina toda la palabra (🎉 Victoria).
   - El jugador se queda sin vidas (😵 Derrota).
   - Introduzcas 3 veces un comando desconocido. Opción incluida para salir en cualquier momento.

---

## 🛠️ Funcion principal del juego:

- Solicita la palabra que se debe adivinar.
- Convierte la palabra en una lista y la oculta inicialmente usando guiones bajos (`_`).
- Permite al jugador adivinar letras mientras se cumplen las condiciones de juego.
- Lleva un registro de letras usadas para evitar repeticiones.
- Gestiona las vidas restantes y muestra mensajes personalizados según los aciertos o errores.
- Finaliza el juego mostrando un mensaje de victoria o derrota, junto con la palabra completa.

## 📌 Contribuciones

Si tienes sugerencias o mejoras para este proyecto, ¡no dudes en contribuir! Puedes abrir un issue o enviar un pull request. 🚀

---

## 🏆 Créditos

Este proyecto fue creado como parte de un ejercicio de programación en Python. ¡Espero que lo disfrutes tanto como yo al desarrollarlo! 😊


¡Gracias por jugar y diviértete adivinando palabras! 🎮✨

