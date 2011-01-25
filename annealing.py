import random
from helpers import *

class SequentialAnnealing(object):
    "Sequential Annealing for Delivery Problem algorithm"

    def __init__(self):
        self.clients = []

    def append_client(self, client_tuple):
        self.clients.append(client_tuple)

    def random_solution(self):
        tmp_clients = self.clients[:]
        random.shuffle(tmp_clients)
        solution = triangularize(tmp_clients)
        return solution

    def squared_length(self):
        if self._squared_length:
            return self._squared_length
        else:
            self._squared_length = len(self.clients)**2
            return _squared_length

    def solve(self):
        old_solution = self.random_solution()
        best_solution = list(old_solution)
        equilibrium_counter = 0
        temp = cost(best_solution)
        while equilibrium_counter <= 20:
            for i in xrange(_squared_length):
                best_solution, old_solution, equilibrium_counter = annealing_step(old_solution, best_solution, equilibrium_counter)
        return best_solution


class AnnealingApp(object):
    """
    Sequential Annealing for Delivery Problem main app.
    """

    def __init__(self):
        pass

    def run(self):
        self.solver = SequentialAnnealing()
        self.read_data()
        self.solver.solve()

    def read_line_vars(self):
        return [int(x) for x in raw_input().strip().split(" ")]

    def read_data(self):
        self.solver.size = self.read_line_vars()
        self.solver.base = self.read_line_vars()
        self.solver.clients_count, = self.read_line_vars()
        for i in range(self.solver.clients_count):
            self.solver.append_client(self.read_line_vars())


if __name__ == "__main__":
    random.seed()
    app = AnnealingApp()
    app.run()

