import struct
import pygame
from pygame.locals import *
from settings import *
import moderngl

class Graphic_engine:
    # you need to give this class screen
    # screen is a Surface you declare to replace display
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.ctx = moderngl.create_context()
        self.texture_coordinates = [0, 1,  1, 1,
                                    0, 0,  1, 0]
        self.world_coordinates = [-1, -1,  1, -1,
                                  -1,  1,  1,  1]
        self.render_indices = [0, 1, 2,
                               1, 2, 3]

        self.prog = self.ctx.program(
            vertex_shader=open('shaders/VERTEX_SHADER.glsl').read(),
            fragment_shader=open('shaders/FRAGMENT_SHADER.glsl').read(),
        )

        self.screen_texture = self.ctx.texture(
            VIRTUAL_RES, 3,
            pygame.image.tostring(screen, "RGB", 1)
            )

        self.screen_texture.repeat_x = False
        self.screen_texture.repeat_y = False

        self.vbo = self.ctx.buffer(struct.pack('8f', *self.world_coordinates))
        self.uvmap = self.ctx.buffer(struct.pack('8f', *self.texture_coordinates))
        self.ibo= self.ctx.buffer(struct.pack('6I', *self.render_indices))

        self.vao_content = [
            (self.vbo, '2f', 'vert'),
            (self.uvmap, '2f', 'in_text')
        ]

        self.vao = self.ctx.vertex_array(self.prog, self.vao_content, self.ibo)

    def render(self):
        # render will do all the work and update the screen
        texture_data = self.screen.get_view('1')
        self.screen_texture.write(texture_data)
        self.ctx.clear(14/255,40/255,66/255)
        self.screen_texture.use()
        self.vao.render()
        pygame.display.flip()
    
    def __call__(self):
        return self.render()
