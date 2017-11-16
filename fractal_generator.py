import math

def generate_cube(a, b, c, d, e, f, g, h, depth):
    vertices = []
    edges = []
    surfaces = []
    cube(a, b, c, d, e, f, g, h, depth, vertices, edges, surfaces, False)
    return (tuple(vertices), tuple(edges), tuple(surfaces), "quad")


def generate_sierpenski(a, b, c, d, depth):
    vertices = []
    edges = []
    surfaces = []
    sierpenski(a, b, c, d, depth, vertices, edges, surfaces)
    return (tuple(vertices), tuple(edges), tuple(surfaces), "triangle")


def cube(a, b, c, d, e, f, g, h, depth, vertices, edges, surfaces, center):
    if depth == 0:
        if center:
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

        last = len(vertices)-1

        edges.append((last-7, last-6))
        edges.append((last-6, last-5))
        edges.append((last-5, last-4))
        edges.append((last-4, last-7))
        edges.append((last-3, last-2))
        edges.append((last-2, last-1))
        edges.append((last-1, last))
        edges.append((last, last-3))
        edges.append((last-7, last-3))
        edges.append((last-6, last-2))
        edges.append((last-5, last-1))
        edges.append((last-4, last))

        surfaces.append((last-7, last-6, last-5, last-4))
        surfaces.append((last-3, last-2, last-1, last))
        surfaces.append((last-7, last-6, last-2, last-3))
        surfaces.append((last-6, last-5, last-1, last-2))
        surfaces.append((last-5, last-4, last, last-1))
        surfaces.append((last-4, last-7, last-3, last))

    else:
        cubes = generate_sub_cubes(a, b, c, d, e, f, g, h)
        for index, item in enumerate(cubes):
            if index == 6:
                cube(item[0], item[1], item[2], item[3], item[4], item[5],
                     item[6], item[7], 0,
                     vertices, edges, surfaces, True)
            else:
                cube(item[0], item[1], item[2], item[3], item[4], item[5],
                     item[6], item[7], depth-1,
                     vertices, edges, surfaces, False)


def sierpenski(a, b, c, d, depth, vertices, edges, surfaces):
    if depth == 0:
        vertices.append(a)
        vertices.append(b)
        vertices.append(c)
        vertices.append(d)

        last = len(vertices)-1

        edges.append((last-3, last-2))
        edges.append((last-2, last-1))
        edges.append((last-1, last-3))
        edges.append((last, last-3))
        edges.append((last, last-2))
        edges.append((last, last-1))

        surfaces.append((last-3, last-2, last-1))
        surfaces.append((last-3, last-2, last))
        surfaces.append((last-3, last, last-1))
        surfaces.append((last, last-2, last-1))

    else:
        sierpenski(a, midpoint(a, b), midpoint(a, c), midpoint(a, d),
                   depth-1, vertices, edges, surfaces)
        sierpenski(midpoint(a, b), b, midpoint(b, c), midpoint(b, d),
                   depth-1, vertices, edges, surfaces)
        sierpenski(midpoint(a, c), midpoint(b, c), c, midpoint(c, d),
                   depth-1, vertices, edges, surfaces)
        sierpenski(midpoint(a, d), midpoint(b, d), midpoint(c, d), d,
                   depth-1, vertices, edges, surfaces)


def midpoint(a, b):
    middle = []
    for i in range(len(a)):
        middle.append((a[i]+b[i])/2)
    return tuple(middle)


def one_third(a, b):
    point = []
    for i in range(len(a)):
        temp = a[i]+((1/3)*(b[i]-a[i]))
        point.append(temp)
    return tuple(point)


def generate_sub_cubes(a, b, c, d, e, f, g, h):
    sub_cubes = []
    origin_points = generate_sub_origins(a, b, c, d, e, f, g, h)
    dimension = one_third(a, b)[0]-a[0]
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
    corners = (a, one_third(b, a), one_third(c, a), one_third(d, a),
               one_third(e, a), one_third(f, a), one_third(g, a), one_third(h, a))
    origins = []
    for corner in corners:
        if corner not in origins:
            origins.append(corner)
        for corner2 in corners:
            temp = midpoint(corner, corner2)
            if temp not in origins:
                origins.append(temp)

    return tuple(origins)


a = (-1, -1, -1)
b = (1, -1, -1)
c = (1, 1, -1)
d = (-1, 1, -1)

e = (-1, -1, 1)
f = (1, -1, 1)
g = (1, 1, 1)
h = (-1, 1, 1)
