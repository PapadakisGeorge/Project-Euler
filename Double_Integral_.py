from scipy import integrate
from numpy import sqrt,tan, pi, arccos


def f_1(x, y):
    return (arccos(y / sqrt(y**2 + x**2)) + arccos(y / sqrt(y**2+(50 - x)**2)))/(1200 * pi)


def bounds_x():
    return [0, 160/5]


def bounds_y(x):
    return [0, x * tan(arccos(4 / 5))]


def f_2(z, w):
    return (arccos(w / sqrt(w**2 + z**2)) + arccos(w / sqrt(w**2+(50 - z)**2)))/(1200 * pi)


def bounds_z():
    return [160/5, 50]


def bounds_w(z):
    return [0, (50 - z) * tan(arccos(3 / 5))]


print(integrate.nquad(f_1, [bounds_y, bounds_x]))
print(integrate.nquad(f_2, [bounds_w, bounds_z]))