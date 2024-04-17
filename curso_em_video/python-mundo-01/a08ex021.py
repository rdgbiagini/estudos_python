""" Faça um programa em Python que abra e reproduza um arquivo de áudio em mp3. """

import pygame

pygame.init()
pygame.mixer.music.load('a08ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()