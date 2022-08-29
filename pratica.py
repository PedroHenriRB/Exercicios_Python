import pygame

pygame.init()
pygame.mixer.music.load('D:\Downloads\Libera Me From Maromba.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()