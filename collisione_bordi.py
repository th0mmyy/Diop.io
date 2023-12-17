def collisione_bordi(playerX, playerY, dimensione_player, larghezza_schermo, altezza_schermo):
    if playerX < 0:
        playerX = 0
    elif playerX > larghezza_schermo - dimensione_player:
        playerX = larghezza_schermo - dimensione_player
    if playerY < 0:
        playerY = 0
    elif playerY > altezza_schermo - dimensione_player:
        playerY = altezza_schermo - dimensione_player

    return playerX, playerY