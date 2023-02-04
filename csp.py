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
            csp.constraints.add((i, j))

        return csp
