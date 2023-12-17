import pygame
import sys
from impostazioni import *

def tasto_centrato(schermo, testo, pulsante):
    testo_rect = testo.get_rect()
    schermo.blit(testo, (pulsante.x + pulsante.width // 2 - testo_rect.width // 2, pulsante.y + pulsante.height // 2 - testo_rect.height // 2))

def mostra_schermata_iniziale(schermo, larghezza_schermo, altezza_schermo):
    schermata_iniziale = True
    difficolta_selezionata = None

    while schermata_iniziale:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                # Controlla se il clic è avvenuto sui pulsanti
                if pulsante_facile.collidepoint(x, y):
                    difficolta_selezionata = diff_facile
                    schermata_iniziale = False
                elif pulsante_media.collidepoint(x, y):
                    difficolta_selezionata = diff_media
                    schermata_iniziale = False
                elif pulsante_difficile.collidepoint(x, y):
                    difficolta_selezionata = diff_difficile
                    schermata_iniziale = False

        schermo.fill(NERO)  # Sfondo nero

        sfondo_iniz = pygame.image.load("img/imm_iniziale.jpg")
        sfondo_iniz = pygame.transform.scale(sfondo_iniz, (larghezza_schermo, altezza_schermo))
        schermo.blit(sfondo_iniz, (0, 0))

        # Testo "Diop.io"
        font_titolo = pygame.font.Font(None, 72)
        testo_titolo = font_titolo.render("Diop.io", True, BIANCO)
        schermo.blit(testo_titolo, (larghezza_schermo // 2 - testo_titolo.get_width() // 2, 100))

        # Testo "Scegli la difficoltà"
        font_sottotitolo = pygame.font.Font(None, 36)
        testo_sottotitolo = font_sottotitolo.render("Scegli la difficoltà", True, BIANCO)
        schermo.blit(testo_sottotitolo, (larghezza_schermo // 2 - testo_sottotitolo.get_width() // 2, 200))

        # Pulsanti per la difficoltà
        pulsante_facile = pygame.Rect(250, altezza_schermo // 2, 200, 50)
        pulsante_media = pygame.Rect(larghezza_schermo // 2 - 100, altezza_schermo // 2, 200, 50)
        pulsante_difficile = pygame.Rect(larghezza_schermo - 450, altezza_schermo // 2, 200, 50)

        pygame.draw.rect(schermo, BIANCO, pulsante_facile)
        pygame.draw.rect(schermo, BIANCO, pulsante_media)
        pygame.draw.rect(schermo, BIANCO, pulsante_difficile)

        font_pulsante = pygame.font.Font(None, 36)
        testo_facile = font_pulsante.render("Facile", True, NERO)
        testo_media = font_pulsante.render("Media", True, NERO)
        testo_difficile = font_pulsante.render("Difficile", True, NERO)

        tasto_centrato(schermo, testo_facile, pulsante_facile)
        tasto_centrato(schermo, testo_media, pulsante_media)
        tasto_centrato(schermo, testo_difficile, pulsante_difficile)

        pygame.display.flip()

    return difficolta_selezionata