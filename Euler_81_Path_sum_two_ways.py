from utils import Timer
import re
import numpy as np
import sys


@Timer.timeit
def main():
    class Graph(object):

        def __init__(self, graph_dictionary=None, weights_dictionary=None):
            if graph_dictionary is None:
                graph_dictionary = {}
            else:
                self.graph_dictionary = graph_dictionary
            if weights_dictionary is None:
                weights_dictionary = {}
            else:
                self.weights_dictionary = weights_dictionary

        def vertices(self):
            return list(self.graph_dictionary.keys())

        def edges(self):
            edges = []
            for vertex in self.graph_dictionary:
                for neighbour in self.graph_dictionary[vertex]:
                    if [vertex, neighbour] not in edges:
                        edges.append([vertex, neighbour])
            return edges

        def add_vertex(self, vertex):
            if vertex not in self.graph_dictionary:
                self.graph_dictionary[vertex] = []

        def add_edge(self, edge):
            edge = set(edge)
            (vertex_1, vertex_2) = tuple(edge)
            if vertex_1 in self.graph_dictionary:
                self.graph_dictionary[vertex_1].append(vertex_2)
            else:
                self.graph_dictionary[vertex_1] = [vertex_2]

        def weights(self, vertex):
            return self.weights_dictionary[vertex]

        def neighbours(self, vertex_1, vertex_2, flag=False):
            if [vertex_1, vertex_2] in self.edges():
                flag = True
            return flag

        def all_neighbours(self, vertex):
            all_neighbours = []
            for i in self.vertices():
                if self.neighbours(vertex, i):
                    all_neighbours.append(i)
            return all_neighbours

        def parents(self, vertex_1, vertex_2, flag=False):
            if [vertex_2, vertex_1] in self.edges:
                flag = True
            return flag

        def all_parents(self, vertex):
            all_parents = []
            for i in self.vertices():
                if self.parents(vertex, i):
                    all_parents.append(i)
            return all_parents

        def find_path(self, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            for i in self.all_neighbours(start):
                if i not in path:
                    new_path = self.find_path(i, end, path)
                    if new_path: return new_path
            return None

        def find_all_paths(self, start, end, path=[]):
            path = path + [start]
            if start == end:
                return [path]
            paths = []
            for i in self.all_neighbours(start):
                if i not in path:
                    new_paths = self.find_all_paths(i, end, path)
                    for new_path in new_paths:
                        paths.append(new_path)
            return paths

        def weight_of_path(self, path):
            weight = 0
            for i in path:
                weight += self.weights(i)
            return weight

        def find_shortest_path(self, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            shortest = None
            for i in self.all_neighbours(start):
                if i not in path:
                    new_path = self.find_shortest_path(i, end, path)
                    if new_path:
                        if not shortest or len(new_path) < len(shortest):
                            shortest = new_path
            return shortest

        def path_Dijkstra(self, start, end):
            vertices = self.vertices().copy()
            visited = {}
            distances = {}

            # Creating a list (visited) for each vertex, which gives us if the vertex is visited.
            # Creating a list (distances) for each vertex, with values infinity for every vertex
            # except the starting one.
            # This is the list of the tentative distances from the starting vertex.

            for vertex in vertices:
                if vertex == start:
                    visited[vertex] = True
                    distances[vertex] = self.weights(vertex)
                else:
                    visited[vertex] = False
                    distances[vertex] = sys.maxsize

            current_vertex = start

            while current_vertex != end:

                # _min is used in order to choose the next current vertex.
                _min = sys.maxsize

                # Choosing the next current vertex.
                for vertex in vertices:
                    if not visited[vertex]:
                        if distances[vertex] < _min:
                            _min = distances[vertex]
                            current_vertex = vertex

                visited[current_vertex] = True
                # Change the values of the current vertex neigbhours' tentative distances.
                for neighbour in self.all_neighbours(current_vertex):
                    if not visited[neighbour]:
                        if distances[neighbour] > self.weights(neighbour) + \
                                distances[current_vertex]:
                            distances[neighbour] = self.weights(neighbour) + \
                                                   distances[current_vertex]
            return distances[current_vertex]

        def dijkstra_2(self, start, end):
            distances = {}
            ancestor = {}
            unseen_nodes = self.vertices().copy()
            infinity = sys.maxsize
            path = []

            for node in unseen_nodes:
                distances[node] = infinity
            distances[start] = self.weights(start)

            while unseen_nodes:

                min_dist_node = None

                for node in unseen_nodes:
                    if min_dist_node is None:
                        min_dist_node = node
                    elif distances[node] < distances[min_dist_node]:
                        min_dist_node = node

                for node in self.all_neighbours(min_dist_node):

                    if self.weights(node) + distances[min_dist_node] < distances[node]:
                        distances[node] = self.weights(node) + distances[min_dist_node]
                        ancestor[node] = min_dist_node
                unseen_nodes.remove(min_dist_node)
                print("Removed", min_dist_node)
            return distances[end]

        def method_BFS(self, vertex):
            visited = {}
            for vertex in self.vertices():
                visited[vertex] = False

            path = [vertex]
            current_vertex = vertex
            visited[vertex] = True
            flag = True
            while flag:

                for vertex in self.all_neighbours(current_vertex):
                    if not visited[vertex]:
                        path.append(vertex)
                        visited[vertex] = True
                        current_vertex = vertex
                        flag = True
                        break
                    else:
                        flag = False
            return path

    def matrix_graph(_matrix, directions):
        vertices = []
        graph_dictionary = {}
        weights_dictionary = {}
        for i in range(0, _matrix.shape[0]):
            for j in range(0, _matrix.shape[1]):
                neighbours = []
                vertices.append((i, j))
                for k in range(0, len(directions)):
                    if (i, j) != (i + directions[k][0], j + directions[k][1]):
                        if not (i + directions[k][0] < 0 or j + directions[k][1] < 0 or
                                i + directions[k][0] > _matrix.shape[0] + 1 or j
                                + directions[k][1] > _matrix.shape[1] + 1):
                            neighbours.append((i + directions[k][0], j + directions[k][1]))
                weights_dictionary.update({(i, j): _matrix[i, j]})
                graph_dictionary.update({(i, j): neighbours})

        graph_of_matrix = Graph(graph_dictionary, weights_dictionary)

        return graph_of_matrix

    filename = "p081_matrix.txt"
    file = open(filename, "r")
    pattern = re.compile(",|\n")
    x_81 = pattern.split(file.read())
    x_81 = list(map(int, x_81[0:6400]))
    matrix = np.array(x_81).reshape(80, 80)
    gm_81 = matrix_graph(np.array(matrix), [[0, 1], [1, 0]])
    # print(gm_81.path_Dijkstra((0, 0), (79, 79)))
    print(gm_81.dijkstra_2((0, 0), (79, 79)))
    test = matrix_graph(np.array([[131, 673, 234, 103, 18],
                                  [201, 96, 342, 965, 150],
                                  [630, 803, 746, 422, 111],
                                  [537, 699, 497, 121, 956],
                                  [805, 732, 524, 37, 331]]), [[0, 1], [1, 0]])
    # print(test.path_Dijkstra((0, 0), (4, 4)))
    # print(test.dijkstra_2((0,0), (4,4)))

    filename_82 = "p082_matrix.txt"
    file_82 = open(filename_82, "r")
    pattern_82 = re.compile(",|\n")
    x_82 = pattern_82.split(file_82.read())
    x_82 = list(map(int, x_82[0:6400]))
    matrix_82 = np.array(x_82).reshape(80, 80)
    gm_82 = matrix_graph(np.array(matrix_82), [[0, 1], [1, 0], [-1, 0]])
    # print(gm_82.path_Dijkstra((0, 0), (79, 79)))


if __name__ == '__main__':
    main()
