import pygame


class MusicPlayer:
    def initialize_music():
        pygame.mixer.init()

    def load_song(path):
        pygame.mixer.music.load(path)

    def play_song():
        pygame.mixer.music.play()

    def is_Playing():
        return pygame.mixer.music.get_busy()

