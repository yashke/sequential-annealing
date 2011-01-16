import random

def triangularize(collection):
    result = []
    i = 0
    for item in collection:
        if i % 3 == 0:
            result.append([item])
        else:
            result[-1].append(item)
        i += 1
    return result

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

    def solve(self):
        best_solution = self.random_solution()
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

