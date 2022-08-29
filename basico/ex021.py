from playsound import playsound

playsound('D:\Downloads\Libera Me From Maromba.mp3')

"""
Ou você pode usar a biblioteca pygame:

import pygame

pygame.init()
pygame.mixer.music.load('D:\Downloads\Libera Me From Maromba.mp3)
pygame.mixer.music.play()
input()
pygame.event.wait()
"""