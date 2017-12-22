import fractal_generator
import simple_renderer
import math

def load_config(file_location):
    print("loading config " + file_location)
    config = []
    f = open(file_location, "r")
    data = f.read()[:-1]
    f.close()
    data_split = data.split(";")
    config.append(data_split[0])
    for item in data_split[1:]:
        temp = item[1:-1].split(",")
        temp2 = []
        if temp == [""]:
            config.append(temp2)
        else:
            for thing in temp:
                temp2.append(int(thing))
            config.append(temp2)
    return tuple(config)



def tetrahedron(depth, config):
    print("Generating mesh")
    a = (math.sqrt(8/9), 0, -1/3)
    b = (-(math.sqrt(2/9)), math.sqrt(2/3), -1/3)
    c = (-(math.sqrt(2/9)), -(math.sqrt(2/3)), -1/3)
    d = (0, 0, 1)
    mesh_data = fractal_generator.generate_tetrahedron(a, b, c, d, depth, config)
    return mesh_data


def cube(depth, config):
    print("Generating mesh")
    a = (-1, -1, -1)
    b = (1, -1, -1)
    c = (1, 1, -1)
    d = (-1, 1, -1)
    e = (-1, -1, 1)
    f = (1, -1, 1)
    g = (1, 1, 1)
    h = (-1, 1, 1)
    mesh_data = fractal_generator.generate_cube(a, b, c, d, e, f, g, h,
                                                depth, config)
    return mesh_data


def main():
    print("Python 3D fractal rendering v0.3")
    print("================================")
    print("FOOOOOOOBAR!")
    print("---------------------------------")
    file_location = input("File: ")
    depth = int(input("Depth: "))
    config = load_config(file_location)
    if config[0] == "cube":
        mesh_data = cube(depth, config[1:])
    elif config[0] == "tetrahedron":
        mesh_data = cube(depth, config[1:])
    print("---------------------------------")
    print("Q W E A S D - rotation")
    print("M - wireframe mode")
    print("Spacebar - auto rotation")
    print("Escape - quit")
    simple_renderer.display_mesh(mesh_data)


if __name__ == "__main__":
    main()
