import struct
import pygame, os, sys
from pygame.locals import *

import moderngl

def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

class Graphic_engine:
    def __init__(self, screen, style = 1, VIRTUAL_RES=(800, 600), cpu_only=False, fullscreen=False):
        pygame.init()
        self.VIRTUAL_RES = VIRTUAL_RES
        self.cpu_only = cpu_only
        self.screen = screen
        self.fullscreen = fullscreen
        if not(self.cpu_only):
            self.ctx = moderngl.create_context()
            self.texture_coordinates = [0, 1,  1, 1,
                                        0, 0,  1, 0]
            self.world_coordinates = [-1, -1,  1, -1,
                                    -1,  1,  1,  1]
            self.render_indices = [0, 1, 2,
                                1, 2, 3]

            self.style = style
            # shader style : 0, no shader. 1, crt. 2, flat_crt.
            self.prog = self.ctx.program(
                vertex_shader=open(resource_path('shaders/VERTEX_SHADER.glsl')).read(),
                fragment_shader=open(resource_path('shaders/FRAGMENT_SHADER.glsl')).read(),
            )
            self.prog['mode'] = self.style

            self.screen_texture = self.ctx.texture(
                self.VIRTUAL_RES, 3,
                pygame.image.tostring(screen, "RGB", 1)
                )

            self.screen_texture.repeat_x = False
            self.screen_texture.repeat_y = False

            self.vbo = self.ctx.buffer(struct.pack('8f', *self.world_coordinates))
            self.uvmap = self.ctx.buffer(struct.pack('8f', *self.texture_coordinates))
            self.ibo= self.ctx.buffer(struct.pack('6I', *self.render_indices))

            self.vao_content = [
                (self.vbo, '2f', 'vert'),
                (self.uvmap, '2f', 'in_text'),
            ]

            self.vao = self.ctx.vertex_array(self.prog, self.vao_content, index_buffer=self.ibo)
        else:
            self.diaplay = pygame.display.get_surface()

    def change_shader(self):
        if not self.cpu_only:
            self.__init__(self.screen, (self.style + 1) % 3, self.VIRTUAL_RES)

    def render(self):
        if not(self.cpu_only):
            texture_data = self.screen.get_view('1')
            self.screen_texture.write(texture_data)
            self.ctx.clear(14/255,40/255,66/255)
            self.screen_texture.use()
            self.vao.render()
            pygame.display.flip()
        else:
            self.diaplay.blit(self.screen, (0, 0))
            pygame.display.update()
    
    def Full_screen(self, REAL_RES):
        if not(self.cpu_only):
            if not(self.fullscreen):
                pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)
            else:
                pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL|pygame.FULLSCREEN)
        else:
            if not(self.fullscreen):
                pygame.display.set_mode(self.VIRTUAL_RES)
            else:
                pygame.display.set_mode(self.VIRTUAL_RES, pygame.FULLSCREEN)
    
    def __call__(self):
        return self.render()
