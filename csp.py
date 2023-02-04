from hall import Hall


class CSP:
    def __init__(self, csp: 'CSP' = None) -> None:
        if csp is None:
            self.n = None
            self.m = None
            self.e = None
            self.halls = {}
            self.constraints = set()
        else:
            self.n = csp.n
            self.m = csp.m
            self.e = csp.e
            self.halls = {i: Hall(csp.halls[i]) for i in range(1, csp.n + 1)}
            self.constraints = csp.constraints

    def copy(self) -> 'CSP':
        return CSP(self)

    @staticmethod
    def from_input() -> 'CSP':
        csp = CSP()

        csp.n, csp.m = tuple(map(int, input().split()))
        csp.halls = {i: Hall() for i in range(1, csp.n + 1)}

        for group_number in range(csp.m):
            hall_numbers = list(map(int, input().split()))
            for hall_number in hall_numbers:
                csp.halls[hall_number].domain.add(group_number)

        csp.e = int(input())

        for c in range(csp.e):
            i, j = tuple(map(int, input().split()))
            csp.halls[i].constraint.add(j)
            csp.halls[j].parent.add(i)
            csp.constraints.add((i, j))

        return csp

    @staticmethod
    def generate(n, m, e):
        from random import randint as rant
        from random import choices
        csp = CSP()
        csp.n, csp.m = tuple(map(int, f"{n} {m}".split()))
        csp.halls = {i: Hall() for i in range(1, csp.n + 1)}
        L = [str(i) for i in range(1, n + 1)]
        for group_number in range(csp.m):
            hall_numbers = list(map(int, choices(L, k=rant(1, n))))
            for hall_number in hall_numbers:
                csp.halls[hall_number].domain.add(group_number)

        csp.e = e

        edges = set()

        while len(edges) != csp.e:
            t = tuple(x for x in choices(L, k=2))
            t_e = (t[1], t[0])
            if t_e not in edges:
                edges.add(t)

        for edge in edges:
            i, j = tuple(map(int, f"{edge[0]} {edge[1]}".split()))
            csp.halls[i].constraint.add(j)
            csp.halls[j].parent.add(i)
            csp.constraints.add((i, j))

        return csp
