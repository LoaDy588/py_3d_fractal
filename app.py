import fractal_generator
import simple_renderer
import math


def sierpenski(depth):
    a = (math.sqrt(8/9), 0, -1/3)
    b = (-(math.sqrt(2/9)), math.sqrt(2/3), -1/3)
    c = (-(math.sqrt(2/9)), -(math.sqrt(2/3)), -1/3)
    d = (0, 0, 1)
    mesh_data = fractal_generator.generate_sierpenski(a, b, c, d, depth)
    return mesh_data


def cube(depth):
    a = (-1, -1, -1)
    b = (1, -1, -1)
    c = (1, 1, -1)
    d = (-1, 1, -1)
    e = (-1, -1, 1)
    f = (1, -1, 1)
    g = (1, 1, 1)
    h = (-1, 1, 1)
    mesh_data = fractal_generator.generate_cube(a, b, c, d, e, f, g, h, depth)
    return mesh_data


def main():
    print("Python 3D fractal rendering v0.1")
    print("================================")
    print("a) Sierpenski Tetrahedron")
    print("b) Morgen Sponge Inverted")
    print("--------------------------------")
    selection = input("Select fractal: ")
    depth = int(input("Depth: "))
    print("--------------------------------")
    print("Generating fractal mesh data")
    if selection == "a":
        mesh_data = sierpenski(depth)
    elif selection == "b":
        mesh_data = cube(depth)
    print("---------------------------------")
    print("Q W E A S D - rotation")
    print("M - wireframe mode")
    print("Spacebar - auto rotation")
    print("Escape - quit")
    simple_renderer.display_mesh(mesh_data)

if __name__ == "__main__":
    main()
