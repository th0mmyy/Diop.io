import pygame
import math

from impostazioni import *

class Nemico:
    def __init__(self, x, y, velocita):
        self.rect = pygame.Rect(x, y, dimensione_player, dimensione_player)
        self.velocita = velocita
        self.immagine = pygame.image.load("img/scp.png")
        self.immagine = pygame.transform.scale(self.immagine, (dimensione_player, dimensione_player))

    def muovi_verso_player(self, x_player, y_player, muri):
        angolo = math.atan2(y_player - self.rect.centery, x_player - self.rect.centerx)
        nem_nuovaX = self.rect.x + self.velocita * math.cos(angolo)
        nem_nuovaY = self.rect.y + self.velocita * math.sin(angolo)
        nuovo_rect = pygame.Rect(nem_nuovaX, nem_nuovaY, dimensione_player, dimensione_player)

        # collisione con i muri dei nemici
        for muro in muri:
            if nuovo_rect.colliderect(muro):
                return
        # no collissioni -> aggiorna posizione
        self.rect.x = nem_nuovaX
        self.rect.y = nem_nuovaY

def pos_nemici():
    mario = Nemico(larghezza_schermo // 4, altezza_schermo // 4, vel_mar)
    luigi = Nemico(larghezza_schermo - larghezza_schermo //4, altezza_schermo - altezza_schermo // 4, vel_lui)
    return mario, luigi