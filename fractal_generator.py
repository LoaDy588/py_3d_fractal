def generate_sierpenski(a, b, c, d, depth):
    vertices = []
    edges = []
    surfaces = []
    sierpenski(a, b, c, d, depth, vertices, edges, surfaces)
    return (tuple(vertices), tuple(edges), tuple(surfaces), "triangle")


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
    return middle
