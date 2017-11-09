import fractal_generator
import simple_renderer
import math

a = (math.sqrt(8/9), 0, -1/3)
b = (-(math.sqrt(2/9)), math.sqrt(2/3), -1/3)
c = (-(math.sqrt(2/9)), -(math.sqrt(2/3)), -1/3)
d = (0, 0, 1)
mesh_data = fractal_generator.generate_sierpenski(a, b, c, d, 3)
simple_renderer.display_mesh(mesh_data)
