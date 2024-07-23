from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    init_back = time()
    init_neck = time()
    watersecs = 50*60
    exsecs = 75*60
    eyessecs = 30*60
    backsecs = 5*60
    necksecs = 10*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'done' to stop the alarm.")
            musiconloop('water.mp3', 'done')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'done' to stop the alarm.")
            musiconloop('eyes.mp3', 'done')
            init_eyes = time()
            log_now("Done Eye exercise at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'done' to stop the alarm.")
            musiconloop('physical.mp3', 'done')
            init_exercise = time()
            log_now("Physical exercise done at")

        if time() - init_back > backsecs:
            print("Straight Time. Enter 'done' to stop the alarm.")
            musiconloop('physical.mp3', 'done')
            init_back = time()
            log_now("Body straighted at")

        if time() - init_neck > necksecs:
            print("Neck Exercise Time. Enter 'done' to stop the alarm.")
            musiconloop('eyes.mp3', 'done')
            init_neck = time()
            log_now("Neck exercise done at")