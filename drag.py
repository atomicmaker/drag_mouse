import pygame
import sys


#鼠标拖动标志
mouse_flag = False
def _check_drag_mouse(event,rect):
    '''监测鼠标的拖动'''
    global mouse_flag

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_flag = True
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_flag = False

    if event.type == pygame.MOUSEMOTION:
        if mouse_flag:
            _drag_mouse(rect)


def _drag_mouse(rect):
    '''拖动鼠标时的响应'''
    mouse_pos = pygame.mouse.get_pos()

    #拖动鼠标改变图片位置
    if rect.collidepoint(mouse_pos):
        rect.center=mouse_pos

