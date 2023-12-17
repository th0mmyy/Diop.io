import pygame
import sys
from impostazioni import *
from nemici import *
from schermata_iniziale import mostra_schermata_iniziale
from vittoria import mostra_schermata_vittoria
from sconfitta import mostra_schermata_sconfitta
from impostazioni import *
from genera_porta import genera_porta
from collisione_bordi import *

def gestisci_eventi():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def gest_gameplay():
    pygame.init()

    schermata_vittoria = False
    schermata_sconfitta = False

    # inizializzazione schermo
    schermo = pygame.display.set_mode((larghezza_schermo, altezza_schermo))
    pygame.display.set_caption("Diop.io")

    # caricamento suono jumpscare
    jumpscare_sound = pygame.mixer.Sound("img/suono_jump.mp3")

    # ciclo di gioco
    clock = pygame.time.Clock()

    # porta
    porta_toccata = False
    portaX, portaY, porta_rect = genera_porta()

    # muri
    muri = [
        # orizzontali
        pygame.Rect(20, 640, 240, 20),     # left, top, spessore, altezza
        pygame.Rect(80, 80, 320, 20),
        pygame.Rect(160, 320, 240, 20),
        pygame.Rect(160, 480, 400, 20),
        pygame.Rect(560, 160, 640, 20),     # 5
        pygame.Rect(560, 560, 240, 20),
        pygame.Rect(880, 320, 160, 20),
        pygame.Rect(1200, 80, 80, 20),
        pygame.Rect(880, 640, 320, 20),
        pygame.Rect(1200, 560, 80, 20), # 10
        # verticali
        pygame.Rect(80, 80, 20, 240),     # left, top, spessore, altezza
        pygame.Rect(240, 0, 20, 80),
        pygame.Rect(160, 320, 20, 240),
        pygame.Rect(320, 480, 20, 400),
        pygame.Rect(480, 560, 20, 80),     # 5
        pygame.Rect(560, 240, 20, 160),
        pygame.Rect(800, 320, 20, 240),
        pygame.Rect(1040, 0, 20, 400),
        pygame.Rect(1120, 400, 20, 240),    #9
        #blocco
        pygame.Rect(1120, 240, 80, 160),
        #bordi
        pygame.Rect(larghezza_porta, 0, larghezza_schermo - larghezza_porta*2, spessore_muro),  #  superiore
        pygame.Rect(0, 0, spessore_muro, altezza_schermo),  #  sinistro
        pygame.Rect(larghezza_porta, altezza_schermo - spessore_muro, larghezza_schermo - larghezza_porta*2, spessore_muro),  # inferiore
        pygame.Rect(larghezza_schermo - spessore_muro, 0, spessore_muro, altezza_schermo),  # destro
    ]

    # sfondo
    img_sfondo = pygame.image.load("img/sfondo.jpg")
    img_sfondo = pygame.transform.scale(img_sfondo, (larghezza_schermo, altezza_schermo))

    # disegna muri
    for muro in muri:
        pygame.draw.rect(schermo, COLORE_MURO, muro)
    
    # start
    tempo_limite = mostra_schermata_iniziale(schermo, larghezza_schermo, altezza_schermo)
    schermata_gioco = True

    # timer
    tempo_iniziale = pygame.time.get_ticks() / 1000  # Tempo in secondi

    #player 
    img_player = pygame.image.load("img/player.png")
    img_player = pygame.transform.scale(img_player, (dimensione_player, dimensione_player))
    img_player_sinsitra = pygame.transform.flip(img_player, True, False)
    img_player_destra = img_player
    playerX = larghezza_schermo // 2 - dimensione_player // 2
    playerY = altezza_schermo // 2 - dimensione_player // 2 

    #nemici
    mario, luigi = pos_nemici()   
    velocita_mario = vel_mar
    velocita_luigi = vel_lui

    while schermata_gioco:
        gestisci_eventi()
                
        # timer
        tempo_trascorso = (pygame.time.get_ticks() / 1000) - tempo_iniziale
        tempo_restante = tempo_limite - tempo_trascorso

        # input movimento
        tasti = pygame.key.get_pressed()
        spostamento_sinistra = (tasti[pygame.K_LEFT] or tasti[pygame.K_a])
        spostamento_destra = (tasti[pygame.K_RIGHT] or tasti[pygame.K_d])
        spostamento_su = (tasti[pygame.K_UP] or tasti[pygame.K_w]) 
        spostamento_giu = (tasti[pygame.K_DOWN] or tasti[pygame.K_s])

        # hack
        if tasti[pygame.K_p]:
            torcia = torcia_hack
        else:
            torcia = dim_torcia
            
        # torcia
        torcia_raggio = pygame.Rect(playerX - torcia, playerY - torcia, dimensione_player + torcia * 2, dimensione_player + torcia * 2)

        # visibilità dei nemici
        mario_visibile = torcia_raggio.colliderect(mario)
        luigi_visibile = torcia_raggio.colliderect(luigi)

        # Movimento del mario
        mario.muovi_verso_player(playerX, playerY, muri)
        luigi.muovi_verso_player(playerX, playerY, muri)

        # movimento del giocatore
        playerX_precedente = playerX
        playerY_precedente = playerY

        if spostamento_sinistra:
            playerX -= velocita_player
            img_player = img_player_sinsitra
        if spostamento_destra:
            playerX += velocita_player
            img_player = img_player_destra
        if spostamento_su:
            playerY -= velocita_player
        if spostamento_giu:
            playerY += velocita_player

        # collisione con i muri
        for muro in muri:
            if (playerX < muro.x + muro.width
                and playerX + dimensione_player > muro.x
                and playerY < muro.y + muro.height
                and playerY + dimensione_player > muro.y):
                playerX = playerX_precedente
                playerY = playerY_precedente
        
        # collisione con i bordi
        playerX, playery = collisione_bordi(playerX, playerY, dimensione_player, larghezza_schermo, altezza_schermo)

        # sfondo
        sfondo_mask = pygame.Surface((larghezza_schermo, altezza_schermo), pygame.SRCALPHA)
        sfondo_mask.fill((0, 0, 0, 0))
        pygame.draw.ellipse(sfondo_mask, (255, 255, 255, 255), (playerX - torcia, playerY - torcia, torcia * 2, torcia * 2))
        schermo.blit(img_sfondo, (0, 0))
        schermo.blit(sfondo_mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        # muri
        for muro in muri:
            riquadro_muro = pygame.Rect(muro)
            intersezione = riquadro_muro.clip(pygame.Rect(playerX - torcia, playerY - torcia, torcia * 2, torcia * 2))
            if intersezione.width > 0 and intersezione.height > 0:
                pygame.draw.rect(schermo, COLORE_MURO, intersezione)
                
        # mario 1 solo se è all'interno della torcia
        if mario_visibile:
            schermo.blit(mario.immagine, mario.rect.topleft)
            velocita_player = 6
        else:
            velocita_player = 5

        # mario 2 solo se è all'interno della torcia
        if luigi_visibile:
            schermo.blit(luigi.immagine, luigi.rect.topleft)
            velocita_player = 7
        else:
            velocita_player = 5

        # collisione con i nemici
        if (playerX < mario.rect.x + mario.rect.width
            and playerX + dimensione_player > mario.rect.x
            and playerY < mario.rect.y + mario.rect.height
            and playerY + dimensione_player > mario.rect.y
        ) or (
            playerX < luigi.rect.x + luigi.rect.width
            and playerX + dimensione_player > luigi.rect.x
            and playerY < luigi.rect.y + luigi.rect.height
            and playerY + dimensione_player > luigi.rect.y):
            schermata_sconfitta = True
            schermata_gioco = False

        # disegna la porta solo se è all'interno della torica
        if torcia_raggio.colliderect(porta_rect):
            pygame.draw.rect(schermo, VERDE, porta_rect)

        # controllo se player ha toccato la porta
        if porta_rect.colliderect(pygame.Rect(playerX, playerY, dimensione_player, dimensione_player)):
            porta_toccata = True

        # porta toccata -> win
        if porta_toccata:
            schermata_vittoria = True
            schermata_gioco = False
        
        # disegna player
        schermo.blit(img_player, (playerX, playerY))

        # timer
        font = pygame.font.Font(None, 36)
        testo_timer = font.render(f"Tempo: {tempo_restante:.2f}", True, BIANCO)
        schermo.blit(testo_timer, (10, 10))

        # tempo scaduto + tempo sotto 10 sec
        if tempo_restante <= 10:
            velocita_mario += 1
            velocita_luigi += 1
        if tempo_restante <= 0:
            schermata_sconfitta = True
            schermata_gioco = False
        
        pygame.display.flip()
        clock.tick(FPS)

        if schermata_vittoria:
            ritorna_al_menu = mostra_schermata_vittoria(schermo, larghezza_schermo, altezza_schermo, clock, FPS)
            if ritorna_al_menu:
                schermata_vittoria = False
                schermata_iniziale = True

        if schermata_sconfitta:
            jumpscare_sound.play()
            jumpscare_image = pygame.image.load("img/imm_jump.jpg")
            jumpscare_image = pygame.transform.scale(jumpscare_image, (larghezza_schermo, altezza_schermo))
            schermo.blit(jumpscare_image, (0, 0))
            pygame.display.flip()
            pygame.time.delay(2000)
            ritorna_al_menu = mostra_schermata_sconfitta(schermo, larghezza_schermo, altezza_schermo, clock, FPS)
            if ritorna_al_menu:
                schermata_sconfitta = False
                schermata_iniziale = True