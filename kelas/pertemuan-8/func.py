import os
import time

def delayInput():
    delayEnter = input('Tekan Enter untuk melanjutkan . . .')

def clear():
    os.system('clear || cls')

def load(panjangLoading=30, waktu=3.5):
    for i in range(panjangLoading + 1):
        time.sleep(waktu / panjangLoading)  
        bar = "=" * i + "-" * (panjangLoading - i)  
        print(f"\rLoading: [{bar}] {i * 100 // panjangLoading}%", end="")