import pygame
import sys
from impostazioni import NERO, BIANCO

def mostra_schermata_vittoria(schermo, larghezza_schermo, altezza_schermo, clock, FPS):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        schermo.fill(NERO)
        
        sfondo_win = pygame.image.load("img/win.jpg")
        sfondo_win = pygame.transform.scale(sfondo_win, (larghezza_schermo, altezza_schermo))
        schermo.blit(sfondo_win, (0, 0))

        # Torna al Menu
        pulsante_menu = pygame.Rect(larghezza_schermo // 2 - 100, 500, 200, 50)
        pygame.draw.rect(schermo, BIANCO, pulsante_menu)

        font_pulsante = pygame.font.Font(None, 36)
        testo_pulsante = font_pulsante.render("Torna al Menu", True, (0, 0, 0))
        schermo.blit(testo_pulsante, (larghezza_schermo // 2 - testo_pulsante.get_width() // 2, 515))

        # Chiudi Gioco
        pulsante_chiudi = pygame.Rect(larghezza_schermo // 2 - 100, 600, 200, 50)
        pygame.draw.rect(schermo, BIANCO, pulsante_chiudi)

        testo_chiudi = font_pulsante.render("Chiudi Gioco", True, (0, 0, 0))
        schermo.blit(testo_chiudi, (larghezza_schermo // 2 - testo_chiudi.get_width() // 2, 615))

        # input
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # click pulsanti
        if pulsante_menu.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            return True
        
        if pulsante_chiudi.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

