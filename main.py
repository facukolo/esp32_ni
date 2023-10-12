# Main: Facundo
from machine import Pin
import time
print("Por FNK 2023")
print("Blink LED con boton")
sw = Pin(23, Pin.IN)
led = Pin(22, Pin.OUT)

debounce_time = 10  # Tiempo de debounce en milisegundos
button_state = sw.value()
led_state = 0  # Estado inicial del LED
contador=0
while True:
    new_button_state = sw.value()

    # Detección de flanco ascendente (botón presionado)
    if new_button_state == 1 and button_state == 0:
        time.sleep_ms(debounce_time)  # Espera de debounce
        if sw.value() == 1:  # Comprueba si el botón sigue siendo presionado
            contador += 1
            print("Contador: ",contador)
            led.value(not led.value())

    button_state = new_button_state
    time.sleep_ms(10)  # Pequeña pausa para reducir la carga del bucle
    