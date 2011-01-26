import random
from helpers import *

class SequentialAnnealing(object):
    "Sequential Annealing for Delivery Problem algorithm"

    ALPHA = 0.9

    def __init__(self):
        self.clients = []
        self._squared_length = None

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
            return self._squared_length

    def solve(self):
        old_solution = self.random_solution()
        best_solution = list(old_solution)
        equilibrium_counter = 0
        temp = cost(best_solution, self.base)
        while equilibrium_counter <= 20:
            for i in xrange(self.squared_length()):
                best_solution, old_solution, equilibrium_counter, temp = self.annealing_step(old_solution, best_solution, equilibrium_counter, temp)
            temp = temp * self.ALPHA
            equilibrium_counter += 1
        return best_solution

    def annealing_step(self, old_solution, best_solution, equilibrium_counter, temp):
        customer = random.choice(self.clients)
        customer_route = filter(lambda x: customer in x, old_solution)[0]
        routes_without_customer = map(lambda x: list(x), filter(lambda x: not customer in x, list(old_solution)))
        for_select = list(routes_without_customer)
        for_select.append([])

        route = random.choice(for_select)

        new_solution = None
        if len(route) < 3:
            new_solution = filter(lambda x: route != x, routes_without_customer)
            route.append(customer)
            new_solution.append(route)
            new_solution.append(filter(lambda x: customer != x, customer_route))
        else:
            new_solution = filter(lambda x: route != x, routes_without_customer)
            customer2 = random.choice(route)
            route1 = filter(lambda x: customer != x, customer_route)
            route1.append(customer2)
            route2 = filter(lambda x: customer2 != x, route)
            route2.append(customer)
            new_solution.append(route1)
            new_solution.append(route2)

        new_solution = filter(lambda x: len(x) > 0, new_solution)

        x = random.random()
        delta = cost(new_solution, self.base) - cost(old_solution, self.base)

        if delta < 0 or x < temp / (temp + delta):
            old_solution = new_solution
            if cost(new_solution, self.base) < cost(best_solution, self.base):
                best_solution = new_solution
                equilibrium_counter = 0

        return old_solution, best_solution, equilibrium_counter, temp


class AnnealingApp(object):
    """
    Sequential Annealing for Delivery Problem main app.
    """

    def __init__(self):
        pass

    def run(self):
        self.solver = SequentialAnnealing()
        self.read_data()
        best_solution = self.solver.solve()
        print best_solution
        print cost(best_solution, self.solver.base)

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

