#https://github.com/Axel-Germany/Micropython_Pico_DRV8825/edit/main/Pico-DRV8825.py
from time import sleep
from machine import Pin
#STEPPER CONECTION
#RESET both conected with 3.3V                             VMOT       12V+           
#SLEEP both conected with 3.3V                             GROUND MOT 12V-
pSTEP = Pin(15, Pin.OUT)    # create output pin on GPIO16  B2 coilB red    NEMA14
pDIR = Pin(14, Pin.OUT)     # create output pin on GPIO17  B1 coilB blue   NEMA14
pEN = Pin(13, Pin.OUT)      # create output pin on GPIO18  A1 coilA black  NEMA14
#                                                          A2 coilA green  NEMA14           
#                                                          GROUND LOGIC  conected to PICO-Ground

steps = 250 # number of steps
usDelay = 1000 # number of microseconds
uS = 0.000001 # one microsecond


pEN.off()  #EN off switches motor on


def turnsteppercw(Msteps):
    pEN.off()  #EN allows power to stepper
    pDIR.off()        
    for i in range(Msteps):
        pSTEP.on()                 # set pin to high level
        sleep(uS * usDelay)
        pSTEP.off()                # set pin to lowlevel
        sleep(uS * usDelay)
    sleep(0.5)
    print("Motor turned CW")
    pEN.on()  #EN on takes power away from stepper   
def turnstepperccw(Msteps):        
    pDIR.on()
    pEN.off()  #EN allows power to stepper
    for i in range(Msteps):
        pSTEP.on()                 # set pin to high level
        sleep(uS * usDelay)
        pSTEP.off()                # set pin to low level
        sleep(uS * usDelay)
    sleep(0.5)
    print("Motor turned CCW")
    pEN.on()  #EN on takes power away from stepper
try: # Main program loop
    while True:
        print("stopp loop with Ctrl + C")
        turnsteppercw(steps)
        sleep(1.5)
        turnstepperccw(steps)
    
# Scavenging work after the end of the program
except KeyboardInterrupt:
    pEN.on()    #EN on switches power on motor of
    print("fertig")
    
