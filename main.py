import pyautogui as py
import random
import time

time.sleep(5)

mensagens = ['sla','vai tomar banho','oi']

for i in range(100):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press('enter')

