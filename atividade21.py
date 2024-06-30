import pygame

pygame.init() # Initialize the Pygame library
print(pygame.init()) # Check if initialization was successful
pygame.mixer.init() # Initialize the mixer module
pygame.mixer.music.load('atividade21.mp3')  # Load the music file
pygame.mixer.music.play() # Play the music
input() # Wait for user input
pygame.event.wait() # Wait for an event
