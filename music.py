import pygame


class MusicPlayer:
    def initialize_music(self):
        pygame.mixer.init()

    def load_song(self, path):
        pygame.mixer.music.load(path)

    def play_song(self):
        pygame.mixer.music.play()

    def is_Playing(self):
        return pygame.mixer.music.get_busy()
