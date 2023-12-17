import random
from gameplay import *

def genera_porta():
    angolo_porta = random.choice(['alto_sinistra', 'alto_destra', 'basso_sinistra', 'basso_destra'])
    if angolo_porta == 'alto_sinistra':
        portaX = 0
        portaY = 0
    elif angolo_porta == 'alto_destra':
        portaX = larghezza_schermo - larghezza_porta
        portaY = 0
    elif angolo_porta == 'basso_sinistra':
        portaX = 0
        portaY = altezza_schermo - spessore_porta
    elif angolo_porta == 'basso_destra':
        portaX = larghezza_schermo - larghezza_porta
        portaY = altezza_schermo - spessore_porta
    porta_rect = pygame.Rect(portaX, portaY, larghezza_porta, spessore_porta)
    return portaX, portaY, porta_rect