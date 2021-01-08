"""
Faça um software que reproduza um audio de arquivo MP3
"""
import pygame

pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): pass
