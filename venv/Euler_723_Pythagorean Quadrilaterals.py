from My_module import Timer
import math
import numpy as np




@Timer.timeit
def main():
    def center_of_mass(list):
        length = len(list[0])
        center = [0 for i in range(0, length)]
        for i in range(0, length):
            for point in list:
                center[i] += point[i]
        final_center = [i/len(list) for i in center]
        return final_center

    def angle(point):
        if point[0] >= 0 and point[1] >= 0:
            angle = np.arccos((point[0])/(math.sqrt(point[0]**2 + point[1]**2)))
        elif point[0] > 0 and point[1] < 0:
            angle = np.arccos((point[0]) / (math.sqrt(point[0] ** 2 + point[1] ** 2))) + math.pi / 2
        elif point[0] <= 0 and point[1] <= 0:
            angle = np.arccos((point[0]) / (math.sqrt(point[0] ** 2 + point[1] ** 2)))+ math.pi
        elif point[0] <= 0 and point[1] >= 0:
            angle = np.arccos((point[0]) / (math.sqrt(point[0] ** 2 + point[1] ** 2)))+ (3/2) * math.pi
        return angle

    def create_quadrilateral(list):
        if not len(list) == 4:
            print("give 4 points")
        else:
            quadrilateral = []
            centered_quadrilateral = []
            center = center_of_mass(list)
            centered_points = []
            for point in list:
                centered_points.append((point[0] + center[0], point[1] + center[1]))

            angles = {}

            for point in centered_points:
                angles[angle(point)] = point
            for key in sorted(angles.keys()):
                centered_quadrilateral.append(angles[key])
            for point in centered_quadrilateral:
                quadrilateral.append((point[0] - center[0], point[1] - center[1]))

        return quadrilateral



    # Enter a radius r and the function will generate all the possible points and group them depending on which quarter
    # of the plane they are.

    def integer_points_of_circle(r):
        points = []
        n = int(r // 1)

        #First quarter
        for i in range(n + 1, -2, -1):
            for j in range(0, n + 1):
                if i ** 2 + j ** 2 == int(r ** 2):
                    if (i, j) not in points:
                        points.append((i, j))

        #Second quarter
        for i in range(-1, -(n + 1), -1):
            for j in range(n + 1, -1, -1):
                if i ** 2 + j ** 2 == int(r ** 2):
                    if (i, j) not in points:
                        points.append((i, j))

        #Third quarter
        for i in range(n + 1, -2, -1):
            for j in range(-1, -(n + 1), -1):
                if i ** 2 + j ** 2 == int(r ** 2):
                    if (i, j) not in points:
                        points.append((-i, j))

        #Fourth quarter
        for i in range(0, n + 1):
            for j in range(n + 1, -2, -1):
                if i ** 2 + j ** 2 == int(r ** 2):
                    if (i, j) not in points:
                        points.append((i, -j))
        return points

    print(integer_points_of_circle(math.sqrt(5)))

    # Enter a radius r and the function will create (a set of) all the different plq inscribed
    #in the circle with radius r starting at the first point of the set of integer candidates
    # and will return the plurality of the created set.
    def pythagorean_lattice_quadrilaterals_with_starting_point(r):
        pql = []
        points = integer_points_of_circle(r)
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    for l in range(k + 1, len(points)):

                        candidate = [np.array(points[i]), np.array(points[j]), np.array(points[k]), np.array(points[l])]
                        if np.inner(candidate[0], candidate[1]) \
                            + np.inner(candidate[1], candidate[2])\
                            + np.inner(candidate[2] , candidate[3]) \
                            + np.inner(candidate[3], candidate[0])\
                            == 0:
                            pql.append(candidate)

        return len(pql)
        # Something is wrong! We get less quadriratelars than expected.
    print(pythagorean_lattice_quadrilaterals_with_starting_point(math.sqrt(5)))

    # Each point generates the same amount of quadrilaterals as the starting point, so the final number of
    # quadrilaterals could be the number of candidates multiplied by the number of quadrilaterals found above. But then
    # we would double count some quadrilaterals.
    def all_pythagorean_lattice_quadrilaterals(r):
        points = integer_points_of_circle(r)
        N = pythagorean_lattice_quadrilaterals_with_starting_point(r)
        plurality = 0
        for i in range(0, len(points)):
            plurality += N - i


        return plurality

    print(all_pythagorean_lattice_quadrilaterals(math.sqrt(5)))



    # The requested function.
    def s(n):
        pass









if __name__ == '__main__':
    main()