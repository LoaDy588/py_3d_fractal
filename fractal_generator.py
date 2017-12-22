def generate_cube(a, b, c, d, e, f, g, h, depth, config):
    vertices = []
    edges = []
    surfaces = []
    cube(a, b, c, d, e, f, g, h, depth, vertices, edges, surfaces, config, False)
    return (tuple(vertices), tuple(edges), tuple(surfaces), "quad")


def generate_tetrahedron(a, b, c, d, depth, config):
    vertices = []
    edges = []
    surfaces = []
    tetrahedron(a, b, c, d, depth, vertices, edges, surfaces, config)
    return (tuple(vertices), tuple(edges), tuple(surfaces), "triangle")


def cube(a, b, c, d, e, f, g, h,
         depth, vertices, edges, surfaces, config, no_gap):
    if depth == 0:
        draw_cube(a, b, c, d, e, f, g, h, vertices, edges, surfaces, no_gap)
    else:
        cubes = generate_sub_cubes(a, b, c, d, e, f, g, h)
        for index, item in enumerate(cubes):
            depth_iter = depth-1
            fill = False
            if index in config[0]:
                if index in config[1]:
                    depth_iter = 0
                if index in config[2]:
                    fill = True
                cube(item[0], item[1], item[2], item[3], item[4], item[5],
                     item[6], item[7], depth_iter,
                     vertices, edges, surfaces, config, fill)


def tetrahedron(a, b, c, d, depth, vertices, edges, surfaces, config):
    if depth == 0:
        draw_tetrahedron(a, b, c, d, vertices, edges, surfaces)
    else:
        tetrahedrons = generate_sub_tetrahedrons(a, b, c, d)
        for index, item in enumerate(tetrahedrons):
            depth_iter = depth-1
            if index in config[0]:
                if index in config[1]:
                    depth_iter = 0
                tetrahedron(item[0], item[1], item[2], item[3],
                            depth_iter, vertices, edges, surfaces, config)


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


def generate_sub_tetrahedrons(a, b, c, d):
    sub_tetra = []
    sub_tetra.append((a, midpoint(a, b), midpoint(a, c), midpoint(a, d)))
    sub_tetra.append((midpoint(a, b), b, midpoint(b, c), midpoint(b, d)))
    sub_tetra.append((midpoint(a, c), midpoint(b, c), c, midpoint(c, d)))
    sub_tetra.append((midpoint(a, d), midpoint(b, d), midpoint(c, d), d))
    return tuple(sub_tetra)


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
    corners = (
        a, one_third(b, a), one_third(c, a), one_third(d, a),
        one_third(e, a), one_third(f, a), one_third(g, a), one_third(h, a)
        )
    origins = []
    for corner in corners:
        if corner not in origins:
            origins.append(corner)
        for corner2 in corners:
            temp = midpoint(corner, corner2)
            if temp not in origins:
                origins.append(temp)

    return tuple(origins)


def draw_cube(a, b, c, d, e, f, g, h, vertices, edges, surfaces, no_gap):
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


def draw_tetrahedron(a, b, c, d, vertices, edges, surfaces):
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
