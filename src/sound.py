# sound.py

import pygame
from settings import SOUND_SETTINGS


class SoundManager:
    '''
    Central class to manage sounds.
    '''
    def __init__(self):
        '''Load and initialize the sound manager.'''
        self.sounds = {
            'point': pygame.mixer.Sound("../assets/sounds/obstacle_sound.wav"),
            'flap': pygame.mixer.Sound("../assets/sounds/flap_sound.wav"),
            'gameover': pygame.mixer.Sound("../assets/sounds/gameover_sound.wav")
        }

        self.sounds['point'].set_volume(0.05)
        self.sounds['flap'].set_volume(0.3)
        self.sounds['gameover'].set_volume(0.1)

    def play(self, sound_name):
        '''Play a sound (if enabled in settings)'''
        if SOUND_SETTINGS["game"] and sound_name in self.sounds:
            self.sounds[sound_name].play()


def update_background_music():
    '''ensures background music follows settings.'''
    if SOUND_SETTINGS["background"]:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()