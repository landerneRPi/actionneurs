import time 
import RPi.GPIO as GPIO
from RpiMotorLib import rpi_dc_lib 

print(" TEST: test moteur sur les broches 19 et 26 ") 
# configuration du moteur
DIRECTION_GPIO = 26
# vitesse => GPIO qui utilise le PWM
VITESSE_GPIO = 19
Motor = rpi_dc_lib.DRV8833NmDc(DIRECTION_GPIO ,VITESSE_GPIO ,50 ,True, "motor_one")

try:
  print("moteur en avant")
  Motor.forward(15)
  input("appuyer sur une touche pour stopper le moteur") 
  print("moteur à l'arrêt")
  Motor.stop(0)
  time.sleep(3)
finally:
  Motor.cleanup(False)
