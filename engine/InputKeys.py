import pygame

from enum import Enum


class InputKeys(Enum):
    ENTER = pygame.K_RETURN
    A = 97
    S = 115
    W = 119
    D = 100
    P = 112
    UP = 1073741906
    DOWN = 1073741905
    LEFT = 1073741904
    RIGHT = 1073741903
    ESCAPE = 27
    SPACE = 32
    MOUSE_LEFT = 1
    MOUSE_RIGHT = 3