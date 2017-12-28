"""
Simple OpenGL mesh renderer.

Uses PyOpenGL and PyGame(for key bindings)

METHODS:
draw - render function, should not be used alone
display_mesh - main function, setup and start the renderer
"""
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw(vertices, edges, surfaces, surface_type, wireframe_mode):
    """
    Render function.

    ARGUMENTS:
    vertices - tuple of mesh vertices
    edges - tuple of mesh edges
    surfaces - tuple of surfaces
    surface_type - shape of surfaces:"triangle" or "quad"
    wireframe_mode - boolean, if True draws only edges
    """
    # Wireframe mode - draw only edges
    if wireframe_mode:
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
    # normal rendering
    else:
        # color tuples to cycle through
        color = ((0.5, 0.5, 0.5),
                 (0.25, 0.25, 0.25),
                 (0.6, 0.6, 0.6),
                 (0.7, 0.7, 0.7))

        # surface type select
        if surface_type == "triangle":
            glBegin(GL_TRIANGLES)
        elif surface_type == "quad":
            glBegin(GL_QUADS)

        # draw surfaces
        for surface in surfaces:
            x = 0
            for vertex in surface:
                glColor3fv(color[x])
                glVertex3fv(vertices[vertex])
                x += 1
    glEnd()


def display_mesh(mesh_data):
    """
    Main function, setup and start of renderer.

    ARGUMENTS:
    mesh_data - tuple containing vertices tuple, edges tuple, surfaces tuple
                and surface_type, in this respective order
    """
    # breakout mesh_data into tuples, deufalt values setup
    vertices = mesh_data[0]
    edges = mesh_data[1]
    surfaces = mesh_data[2]
    surface_type = mesh_data[3]
    wireframe_mode = False
    autorotate = False

    # PyGame window setup
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # starting perspective
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -3)

    # enable z-buffering
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    # main loop - should be broken into separate functions, too complex
    while True:
        # check events
        for event in pygame.event.get():
            # quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # key presses breakdown
            if event.type == pygame.KEYDOWN:
                # exit
                if event.key == 27:  # ESC
                    pygame.quit()
                    quit()
                # rotation
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
                # autorotation toggle
                if event.key == 32:  # SPACE
                    if autorotate:
                        autorotate = False
                    else:
                        autorotate = True
                # wireframe toggle
                if event.key == 109:  # M
                    if wireframe_mode:
                        wireframe_mode = False
                    else:
                        wireframe_mode = True
        # autorotation
        if autorotate:
            glRotatef(0.3, 1, 3, 1)

        # render frame
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw(vertices, edges, surfaces, surface_type, wireframe_mode)
        pygame.display.flip()
        pygame.time.wait(10)
