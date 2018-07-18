import pygame as pg
from player import Player
from player_node import PlayerNode

class SiegeGame(object):

    def __init__(self):
        self.neutral_nodes = pg.sprite.Group
        self.player1 = Player()
        self.player2 = Player()
        self.p1_node = PlayerNode(self.player1)
        self.p2_node = PlayerNode(self.player2)

        self.running = True

    def run(self):
        #primary game loop

        while self.running:
            pass
