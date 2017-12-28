"""
Three dimensional fractal generator.

Creates fractals based on 3 shapes - cube, tetrahedron and pyramid.
Fractal shape is defined by config tuple - info in README
Outputs tuple suitable for usage in simple_renderer.py - info in README

GENERATION METHODS:
generate_cube - generates cube-based fractal mesh
generate_tetrahedron - generates tetrahedron-based fractal mesh
generate_pyramid - generates pyramid-based fractal mesh

INTERNAL/UTILITY METHODS:
cube - main recursive method for cube-based fractal generation
tetrahedron - main recursive method for tetrahedron-based fractal generation
pyramid - main recursive method for pyramid-based fractal generation
midpoint - calculate midpoint between two points
one_third - calculate one third between two points
generate_sub_tetrahedrons - generate sub-tetrahedrons
generate_sub_pyramids - generate sub-pyramids
generate_sub_cubes - generate sub-cubes
generate_sub_origins - generates sub-origins for sub_cubes
draw_tetrahedron
draw_pyramid
draw_cube
"""


def generate_cube(a, b, c, d, e, f, g, h, depth, config):
    """
    Generate cube-based fractal mesh.

    ARGUMENTS:
    a, b, c, d, e, f, g, h - cube vertices
    depth - number of iterations to generate
    config - config tuple for fractal
    """
    # create lists for mesh data
    vertices = []
    edges = []
    surfaces = []
    # start recursive generation
    cube(a, b, c, d, e, f, g, h, depth, vertices, edges, surfaces, config, False)
    # return mesh data tuple
    return (tuple(vertices), tuple(edges), tuple(surfaces), "quad")


def generate_tetrahedron(a, b, c, d, depth, config):
    """
    Generate tetrahedron-based fractal mesh.

    ARGUMENTS:
    a, b, c, d - tetrahedron vertices
    depth - number of iterations to generate
    config - config tuple for fractal
    """
    # create lists for mesh data
    vertices = []
    edges = []
    surfaces = []
    # start recursive generation
    tetrahedron(a, b, c, d, depth, vertices, edges, surfaces, config)
    # return mesh data tuple
    return (tuple(vertices), tuple(edges), tuple(surfaces), "triangle")


def generate_pyramid(a, b, c, d, e, depth, config):
    """
    Generate pyramid-based fractal mesh.

    ARGUMENTS:
    a, b, c, d, e - pyramid vertices
    depth - number of iterations to generate
    config - config tuple for fractal
    """
    # create lists for mesh data
    vertices = []
    edges = []
    surfaces = []
    # start recursive generation
    pyramid(a, b, c, d, e, depth, vertices, edges, surfaces, config)
    # return mesh data tuple
    return (tuple(vertices), tuple(edges), tuple(surfaces), "triangle")


def cube(a, b, c, d, e, f, g, h,
         depth, vertices, edges, surfaces, config, no_gap):
    """
    Recursive cube fractal generation.

    ARGUMENTS:
    a, b, c, d, e, f, g, h - cube vertices
    depth - how deep in interations
    vertices, edges, surfaces - mesh data lists
    config - config tuple to generate from
    no_gap - if True, cube fills the whole space defined by vertices
    """
    # if zero depth, final iteration, draw cube
    if depth == 0:
        draw_cube(a, b, c, d, e, f, g, h, vertices, edges, surfaces, no_gap)
    else:
        # divide cube into 27 cubes and iterate over all of them
        cubes = generate_sub_cubes(a, b, c, d, e, f, g, h)
        for index, item in enumerate(cubes):
            # default values
            depth_iter = depth-1
            fill = False
            # setup next cube according to config
            if index in config[0]:
                if index in config[1]:
                    depth_iter = 0
                if index in config[2]:
                    fill = True
                # recursive call
                cube(item[0], item[1], item[2], item[3], item[4], item[5],
                     item[6], item[7], depth_iter,
                     vertices, edges, surfaces, config, fill)


def tetrahedron(a, b, c, d, depth, vertices, edges, surfaces, config):
    """
    Recursive tetrahedron fractal generation.

    ARGUMENTS:
    a, b, c, d - tetrahedron vertices
    depth - how deep in interations
    vertices, edges, surfaces - mesh data lists
    config - config tuple to generate from
    """
    # if zero depth, final iteration, draw tetrahedron
    if depth == 0:
        draw_tetrahedron(a, b, c, d, vertices, edges, surfaces)
    else:
        # create sub-tetrahedrons and iterate over them
        tetrahedrons = generate_sub_tetrahedrons(a, b, c, d)
        for index, item in enumerate(tetrahedrons):
            depth_iter = depth-1  # helper variable
            # setup next tetrahedron according to config
            if index in config[0]:
                if index in config[1]:
                    depth_iter = 0
                # recursive call
                tetrahedron(item[0], item[1], item[2], item[3],
                            depth_iter, vertices, edges, surfaces, config)


def pyramid(a, b, c, d, e, depth, vertices, edges, surfaces, config):
    """
    Recursive pyramid fractal generation.

    ARGUMENTS:
    a, b, c, d, e - pyramid vertices
    depth - how deep in interations
    vertices, edges, surfaces - mesh data lists
    config - config tuple to generate from
    """
    # if depth zero, final iteration, draw pyramid
    if depth == 0:
        draw_pyramid(a, b, c, d, e, vertices, edges, surfaces)
    else:
        # create sub-pyramids and iterate over them
        pyramids = generate_sub_pyramids(a, b, c, d, e)
        for index, item in enumerate(pyramids):
            depth_iter = depth-1  # helper variable
            # setup next pyramid according to config
            if index in config[0]:
                if index in config[1]:
                    depth_iter = 0
                # recursive call
                pyramid(item[0], item[1], item[2], item[3], item[4],
                        depth_iter, vertices, edges, surfaces, config)


def midpoint(a, b):
    """
    Calculate midpoint between two points.

    Works in any number of dimensions.

    ARGUMENTS: a, b - two points to find mindpoint between.
    """
    middle = []
    for i in range(len(a)):
        middle.append((a[i]+b[i])/2)
    return tuple(middle)


def one_third(a, b):
    """
    Calculate one-third between two points.

    Works in any number of dimensions, result depends on order of points.

    ARGUMENTS: a, b, - two points to find 1/3 between.
    """
    point = []
    for i in range(len(a)):
        temp = a[i]+((1/3)*(b[i]-a[i]))
        point.append(temp)
    return tuple(point)


def generate_sub_tetrahedrons(a, b, c, d):
    """
    Generate sub-tetrahedrons.

    Returns tuple of tetrahedrons.

    ARGUMENTS: a, b, c, d - vertices of tetrahedron
    """
    sub_tetra = []
    sub_tetra.append((a, midpoint(a, b), midpoint(a, c), midpoint(a, d)))
    sub_tetra.append((midpoint(a, b), b, midpoint(b, c), midpoint(b, d)))
    sub_tetra.append((midpoint(a, c), midpoint(b, c), c, midpoint(c, d)))
    sub_tetra.append((midpoint(a, d), midpoint(b, d), midpoint(c, d), d))
    return tuple(sub_tetra)


def generate_sub_pyramids(a, b, c, d, e):
    """
    Generate sub-pyramids.

    Returns tuple of pyramids.

    ARGUMENTS: a, b, c, d, e - vertices of pyramid
    """
    sub_pyramids = []
    sub_pyramids.append((a, midpoint(a, b), midpoint(a, c),
                        midpoint(a, d), midpoint(a, e)))
    sub_pyramids.append((midpoint(a, b), b, midpoint(b, c),
                        midpoint(b, d), midpoint(b, e)))
    sub_pyramids.append((midpoint(a, c), midpoint(b, c), c,
                        midpoint(c, d), midpoint(c, e)))
    sub_pyramids.append((midpoint(a, d), midpoint(a, c), midpoint(c, d),
                         d, midpoint(d, e)))
    sub_pyramids.append((midpoint(a, e), midpoint(b, e), midpoint(c, e),
                         midpoint(d, e), e))
    sub_pyramids.append((midpoint(a, e), midpoint(b, e), midpoint(c, e),
                         midpoint(d, e), midpoint(a, c)))
    return tuple(sub_pyramids)


def generate_sub_cubes(a, b, c, d, e, f, g, h):
    """
    Generate sub-cubes.

    Returns tuple of cubes.

    ARGUMENTS: a, b, c, d, e, f, g, h - vertices of cube
    """
    sub_cubes = []
    # generate origin points for sub_cubes and calculate dimension of cube
    origin_points = generate_sub_origins(a, b, c, d, e, f, g, h)
    dimension = one_third(a, b)[0]-a[0]  # hack, expects cube to be aligned to axis.
    # for every origin, create new cube
    for origin in origin_points:
        new_a = origin
        new_b = (origin[0]+dimension, origin[1], origin[2])
        new_c = (origin[0]+dimension, origin[1]+dimension, origin[2])
        new_d = (origin[0], origin[1]+dimension, origin[2])

        new_e = (origin[0], origin[1], origin[2]+dimension)
        new_f = (origin[0]+dimension, origin[1], origin[2]+dimension)
        new_g = (origin[0]+dimension, origin[1]+dimension, origin[2]+dimension)
        new_h = (origin[0], origin[1]+dimension, origin[2]+dimension)
        sub_cubes.append((new_a, new_b, new_c, new_d,
                          new_e, new_f, new_g, new_h))
    return tuple(sub_cubes)


def generate_sub_origins(a, b, c, d, e, f, g, h):
    """
    Generate origins of sub-cubes.

    Returns tuple of sub-origins.

    ARGUMENTS: a, b, c, d, e, f, g, h - vertices of cube
    """
    # create cube 2/3 the size of original cube
    corners = (
        a, one_third(b, a), one_third(c, a), one_third(d, a),
        one_third(e, a), one_third(f, a), one_third(g, a), one_third(h, a)
        )
    origins = []
    # add every corner of new cube and every midpoint in the cube to origins
    for corner in corners:
        if corner not in origins:
            origins.append(corner)
        for corner2 in corners:
            temp = midpoint(corner, corner2)
            if temp not in origins:
                origins.append(temp)

    return tuple(origins)


def draw_cube(a, b, c, d, e, f, g, h, vertices, edges, surfaces, no_gap):
    """Draw cube function, self explanatory."""
    if no_gap:
        vertices.append(a)  # A
        vertices.append(b)  # B
        vertices.append(c)  # C
        vertices.append(d)  # D
        vertices.append(e)  # E
        vertices.append(f)  # F
        vertices.append(g)  # G
        vertices.append(h)  # H
    else:
        vertices.append(one_third(a, g))  # A
        vertices.append(one_third(b, h))  # B
        vertices.append(one_third(c, e))  # C
        vertices.append(one_third(d, f))  # D
        vertices.append(one_third(e, c))  # E
        vertices.append(one_third(f, d))  # F
        vertices.append(one_third(g, a))  # G
        vertices.append(one_third(h, b))  # H

    last = len(vertices) - 1

    edges.append((last-7, last-6))  # AB
    edges.append((last-6, last-5))  # BC
    edges.append((last-5, last-4))  # CD
    edges.append((last-4, last-7))  # DA
    edges.append((last-3, last-2))  # EF
    edges.append((last-2, last-1))  # FG
    edges.append((last-1, last))  # GH
    edges.append((last, last-3))  # HE
    edges.append((last-7, last-3))  # AE
    edges.append((last-6, last-2))  # BF
    edges.append((last-5, last-1))  # CG
    edges.append((last-4, last))  # DH

    surfaces.append((last-7, last-6, last-5, last-4))  # ABCD
    surfaces.append((last-3, last-2, last-1, last))  # EFGH
    surfaces.append((last-7, last-6, last-2, last-3))  # ABFE
    surfaces.append((last-6, last-5, last-1, last-2))  # BCGF
    surfaces.append((last-5, last-4, last, last-1))  # CDHG
    surfaces.append((last-4, last-7, last-3, last))  # DAEH


def draw_tetrahedron(a, b, c, d, vertices, edges, surfaces):
    """Draw cube tetrahedron, self explanatory."""
    for vertex in (a, b, c, d):
        vertices.append(vertex)

    last = len(vertices)-1

    edges.append((last-3, last-2))  # AB
    edges.append((last-2, last-1))  # BC
    edges.append((last-1, last-3))  # CA
    edges.append((last, last-3))  # DA
    edges.append((last, last-2))  # DB
    edges.append((last, last-1))  # DC

    surfaces.append((last-3, last-2, last-1))  # ABC
    surfaces.append((last-3, last-2, last))  # ABD
    surfaces.append((last-3, last, last-1))  # ADC
    surfaces.append((last, last-2, last-1))  # DBC


def draw_pyramid(a, b, c, d, e, vertices, edges, surfaces):
    """Draw cube pyramid, self explanatory."""
    for vertex in (a, b, c, d, e):
        vertices.append(vertex)

    last = len(vertices)-1

    edges.append((last-4, last-3))  # AB
    edges.append((last-3, last-2))  # BC
    edges.append((last-2, last-1))  # CD
    edges.append((last-1, last-4))  # DA
    edges.append((last-4, last))  # AE
    edges.append((last-3, last))  # BE
    edges.append((last-2, last))  # CE
    edges.append((last-1, last))  # DE

    surfaces.append((last-4, last-2, last-3))  # ACB
    surfaces.append((last-1, last-4, last-2))  # DAC
    surfaces.append((last-4, last-3, last))  # ABE
    surfaces.append((last-3, last-2, last))  # BCE
    surfaces.append((last-2, last-1, last))  # CDE
    surfaces.append((last-1, last-4, last))  # DAE
