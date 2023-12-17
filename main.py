# Diop.io
# Progetto per l'open day del 16 dicembre 2023

# Game developers:
# - Manzoni Thomas
# - Duhanhiu Hegi

# Game artist:
# - Duhanhiu Hegi

import pygame
import sys
from gameplay import *
from impostazioni import *

def main():
    while True:
        gest_gameplay()
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()