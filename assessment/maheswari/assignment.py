import random, time, winsound

while True:
    temp = random.randint(1,100)
    if temp > 60:
        print("Alert Temperature is high!!")
        winsound.PlaySound("beep-09a.wav",winsound.SND_FILENAME)
    else:
        print("Temperature is Normal")
    time.sleep(1)
