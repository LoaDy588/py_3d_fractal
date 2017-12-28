"""
Simple app for loading fractal defining file and rendering it in OpenGL.
"""
import fractal_generator
import simple_renderer
import math


def load_config(file_location):
    """
    Load config file and parse it to suitable config format for renderer.

    Requires config file location as argument.
    """
    print("loading config " + file_location)
    config = []

    # Load file(without newline at the end)
    f = open(file_location, "r")
    data = f.read()[:-1]
    f.close()

    # parse the file into required format
    data_split = data.split(";")
    config.append(data_split[0])
    for item in data_split[1:]:
        item_split = item[1:-1].split(",")
        temp = []
        if item_split == [""]:
            config.append(temp)
        else:
            for value in item_split:
                temp2.append(int(value))
            config.append(temp)
    return tuple(config)


def tetrahedron(depth, config):
    """Generate mesh for tetrahedron fractal based on config and depth."""
    print("Generating mesh")

    # starting values(tetrahedron inside unit sphere)
    a = (math.sqrt(8/9), 0, -1/3)
    b = (-(math.sqrt(2/9)), math.sqrt(2/3), -1/3)
    c = (-(math.sqrt(2/9)), -(math.sqrt(2/3)), -1/3)
    d = (0, 0, 1)

    # pass data to fractal generator
    mesh_data = fractal_generator.generate_tetrahedron(a, b, c, d, depth, config)
    return mesh_data


def pyramid(depth, config):
    """Generate mesh for pyramid fractal based on config and depth."""
    print("Generating mesh")

    # starting values(pyramid with length of sqrt(2))
    a = (-1, 0, 0)
    b = (0, -1, 0)
    c = (1, 0, 0)
    d = (-0, 1, 0)
    e = (0, 0, 1)

    # pass data to fractal generator
    mesh_data = fractal_generator.generate_pyramid(a, b, c, d, e, depth, config)
    return mesh_data


def cube(depth, config):
    """Generate mesh for cube fractal based on config and depth."""
    print("Generating mesh")

    # starting values(cube with side length of 2)
    a = (-1, -1, -1)
    b = (1, -1, -1)
    c = (1, 1, -1)
    d = (-1, 1, -1)
    e = (-1, -1, 1)
    f = (1, -1, 1)
    g = (1, 1, 1)
    h = (-1, 1, 1)

    # pass data to fractal generator
    mesh_data = fractal_generator.generate_cube(a, b, c, d, e, f, g, h,
                                                depth, config)
    return mesh_data


def main():
    """Main function - menu and control."""
    print("Python 3D fractal rendering v0.3")
    print("================================")
    print("Please select a .fdf file to render")
    print("---------------------------------")

    # file input
    file_location = input("File: ")
    depth = int(input("Depth(iterations): "))
    config = load_config(file_location)

    # mesh generation
    if config[0] == "cube":
        mesh_data = cube(depth, config[1:])
    elif config[0] == "tetrahedron":
        mesh_data = tetrahedron(depth, config[1:])
    elif config[0] == "pyramid":
        mesh_data = pyramid(depth, config[1:])

    # keys
    print("---------------------------------")
    print("Q W E A S D - rotation")
    print("M - wireframe mode")
    print("Spacebar - auto rotation")
    print("Escape - quit")

    # render mesh
    simple_renderer.display_mesh(mesh_data)


if __name__ == "__main__":
    main()
