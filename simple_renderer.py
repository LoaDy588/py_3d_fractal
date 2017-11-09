import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw(vertices, edges, surfaces, surface_type, wireframe_mode):
    if wireframe_mode:
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
    else:
        color = ((0.5, 0.5, 0.5),
                 (0.25, 0.25, 0.25),
                 (0.6, 0.6, 0.6))
        if surface_type == "triangle":
            glBegin(GL_TRIANGLES)
        elif surface_type == "quad":
            glBegin(GL_QUADS)
        for surface in surfaces:
            x = 0
            for vertex in surface:
                glColor3fv(color[x])
                glVertex3fv(vertices[vertex])
                x += 1
    glEnd()


def display_mesh(mesh_data):
    vertices = mesh_data[0]
    edges = mesh_data[1]
    surfaces = mesh_data[2]
    surface_type = mesh_data[3]
    wireframe_mode = False
    autorotate = False

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -3)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 27:
                    pygame.quit()
                    quit()
                if event.key == 113:  # Q
                    glRotatef(1, 0, 0, 1)
                if event.key == 101:  # E
                    glRotatef(1, 0, 0, -1)
                if event.key == 119:  # W
                    glRotatef(1, 1, 0, 0)
                if event.key == 115:  # S
                    glRotatef(1, -1, 0, 0)
                if event.key == 97:  # A
                    glRotatef(1, 0, 1, 0)
                if event.key == 100:  # D
                    glRotatef(1, 0, -1, 0)
                if event.key == 32:  # SPACE
                    if autorotate:
                        autorotate = False
                    else:
                        autorotate = True
                if event.key == 109:  # M
                    if wireframe_mode:
                        wireframe_mode = False
                    else:
                        wireframe_mode = True

        if autorotate:
            glRotatef(0.3, 1, 3, 1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw(vertices, edges, surfaces, surface_type, wireframe_mode)
        pygame.display.flip()
        pygame.time.wait(10)
