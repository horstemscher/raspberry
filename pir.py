# ################################################################
#
# pir.py
#
# python script fuer die Benutzung des Bewegungssensors
#
# Quelle: https://tutorials-raspberrypi.de/raspberry-pi-bewegungsmelder-sensor-pir/
# letzer Aufruf: 21.03.2020
#
# ################################################################
#
import RPi.GPIO as GPIO
import time

LED_PIN = 22
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
 
def mein_callback(channel):
    # Hier kann alternativ eine Anwendung/Befehl etc. gestartet werden.
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    GPIO.output(LED_PIN, GPIO.HIGH)
    print(result)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback)
  
    GPIO.output(LED_PIN, GPIO.HIGH)
    print('Starten ...')
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    
    while True:
        time.sleep(10)
        GPIO.output(LED_PIN, GPIO.LOW)
except KeyboardInterrupt:
    print "Beende..."
GPIO.cleanup()

# ################################################################
# eof pir.py
# ################################################################
