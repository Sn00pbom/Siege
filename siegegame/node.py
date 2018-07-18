import pygame as pg

class Node(pg.sprite.Sprite):

    def __init__(self):

        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('./siegegame/img/node.png')
        self.rect = pg.image.get_rect()

        self.connected = []

    def connect_node(self, node):
        self.connected.append(node)
        node.connect_node(self)
