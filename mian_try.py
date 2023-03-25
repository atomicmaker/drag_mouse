import pygame

import sys

mouse_flag = False
class Main:
    '''主程序控制'''
    def __init__(self):
        '''初始化窗口'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        # 背景颜色
        self.back_color = (135, 255, 255)
        #在（0，0）处创建一个矩形
        self.rect=pygame.Rect(0,0,50,60)
        self.rect_color=(0,0,0)

        pygame.display.set_caption('拖动尝试')

    def check_event(self,):
        '''监测鼠标和键盘事件'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_drag_mouse(event)

    def _check_drag_mouse(self,event):
        global mouse_flag

        if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_flag=True
        if event.type==pygame.MOUSEBUTTONUP:
                mouse_flag=False

        if event.type==pygame.MOUSEMOTION:
            if mouse_flag:
                self._drag_mouse()


    def _drag_mouse(self,):
        '''拖动鼠标时的响应'''
        self.mouse_pos = pygame.mouse.get_pos()
        self._check_rect_mouse()

    def _check_rect_mouse(self):
        '''监测矩形与鼠标的碰撞'''
        if self.rect.collidepoint(self.mouse_pos):
            self.rect.center=self.mouse_pos


    def update_screen(self):
        '''更新屏幕'''
        self.screen.fill(self.back_color)
        pygame.draw.rect(self.screen,self.rect_color,self.rect)

        pygame.display.flip()

    def run_main(self):
        '''运行主程序'''
        while True:
            self.check_event()
            self.update_screen()

if __name__=='__main__':
    main=Main()
    main.run_main()
