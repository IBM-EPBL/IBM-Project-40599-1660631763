import random, time, winsound

while True:
    temp = random.randint(1,100)
    if temp > 60:
        print("Alert Temperature is high!!",temp)
        winsound.PlaySound("bell.wav",winsound.SND_FILENAME)
    else:
        print("Temperature is Normal",temp)
    time.sleep(1)
