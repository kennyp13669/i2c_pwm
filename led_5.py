#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)#, PWM(0x41), PWM(0x42), PWM(0x43)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)         # changed 0 to 1

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
#while (True):

#for x in range (1): 
 # changes stuff on channel 0
#    import time                                          #imports the time library
#    import random
#    pwm.setPWM(1, 0, 500)   # changed 0 to 13 to 1
#    pwm.setPWM(2, 0, 500)   # changed 0 to 14 to 2
#    pwm.setPWM(3, 0, 500)   # changed 0 to 15 to 3
#    for x in range(1, 100):                               #performs something 100 times 
#      random_number = random.randint(0, 1000)
#      random_second_number = random.randint(0, 1000)
#      random_third_number = random.randint(0, 1000)
#      pwm.setPWM(1, 0, random_number)            # changed 0 to 13 to 1
#      pwm.setPWM(2, 0, random_second_number)     # changed 0 to 14 to 2
#      pwm.setPWM(3, 0, random_third_number)      # changed 0 to 15 to 3
#       
#      time.sleep(0.2)                                  #waits a fifth second
#      pwm.setPWM(1, 0, 0)    # changed 0 to 13 to 1
#      pwm.setPWM(2, 0, 0)    # changed 0 to 14 to 2
#      pwm.setPWM(3, 0, 0)    # changed 0 to 15 to 3


pwm = PWM(0x40)                         
for x in range(1, 2):                           #perform the while loop 1 times
  new_number = 1
  while new_number < 17:
    pwm.setPWM(new_number, 0, 500)   
    new_number = new_number + 1
    time.sleep(0.05)                             # waits a twentieth second. change frequency: p.ChangeFrequency(new frequency in Hz)
pwm = PWM(0x41)                                
for x in range(1, 2):                           #perform the while loop 1 times
  new_number_2 = 1  
  while new_number_2 < 17:
    pwm.setPWM(new_number_2, 0, 500)   
    new_number_2 = new_number_2 + 1
    time.sleep(0.05)                             # waits a twentieth second. change frequency: p.ChangeFrequency(new frequency in Hz)
pwm = PWM(0x42)                                
for x in range(1, 2):                           #perform the while loop 1 times
  new_number_3 = 1
  while new_number_3 < 17:
    pwm.setPWM(new_number_3, 0, 500)   
    new_number_3 = new_number_3 + 1
    time.sleep(0.05)                             # waits a twentieth second. change frequency: p.ChangeFrequency(new frequency in Hz)
pwm = PWM(0x43)                                   
for x in range(1, 2):                           #perform the while loop 1 times
  new_number_4 = 1
  while new_number_4 < 17:
    pwm.setPWM(new_number_4, 0, 500)   
    new_number_4 = new_number_4 + 1
    time.sleep(0.05)                             # waits a twentieth second. change frequency: p.ChangeFrequency(new frequency in Hz)



pwm = PWM(0x43)
for x in range(1, 2):                           #perform the while loop 1 times
  new_number_4 = 1
  while new_number_4 < 17:
    pwm.setPWM(new_number_4, 0, 500)   
    new_number_4 = new_number_4 + 1                     
  new_number_5 = 16
  while new_number_5 > 0:
    pwm.setPWM(new_number_5, 0, 0)   
    new_number_5 = new_number_5 - 1
    time.sleep(0.05)                             # waits a twentieth second. change frequency: p.ChangeFrequency(new frequency in Hz)
pwm = PWM(0x42)
for x in range(1, 2):                           #perform the while loop 1 times
  new_number_3 = 1
  while new_number_3 < 17:
    pwm.setPWM(new_number_3, 0, 500)   
    new_number_3 = new_number_3 + 1
  new_number_6 = 16
  while new_number_6 > 0:
    pwm.setPWM(new_number_6, 0, 0)   
    new_number_6 = new_number_6 - 1
    time.sleep(0.05)                             # waits a twentieth second. change frequency: p.ChangeFrequency(new frequency in Hz)
pwm = PWM(0x41)
for x in range(1, 2):                           #perform the while loop 1 times
  new_number_2 = 1  
  while new_number_2 < 17:
    pwm.setPWM(new_number_2, 0, 500)   
    new_number_2 = new_number_2 + 1
  new_number_7 = 16
  while new_number_7 > 0:
    pwm.setPWM(new_number_7, 0, 0)   
    new_number_7 = new_number_7 - 1
    time.sleep(0.05)                             # waits a twentieth second. change frequency: p.ChangeFrequency(new frequency in Hz)
pwm = PWM(0x40)
for x in range(1, 2):                           #perform the while loop 1 times
  new_number = 1
  while new_number < 17:
    pwm.setPWM(new_number, 0, 500)   
    new_number = new_number + 1
  new_number_8 = 16
  while new_number_8 > 0:
    pwm.setPWM(new_number_8, 0, 0)   
    new_number_8 = new_number_8 - 1
    time.sleep(0.05)                             # waits a twentieth second. change frequency: p.ChangeFrequency(new frequency in Hz)
