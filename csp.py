from hall import Hall


class CSP:
    def __init__(self) -> None:
        self.n = None
        self.m = None
        self.e = None
        self.halls = {}
        self.constraints = set()

    def from_input(self):
        self.n, self.m = tuple(map(int, input().split()))
        self.halls = {i: Hall() for i in range(1, self.n + 1)}

        for group_number in range(self.n):
            hall_numbers = list(input().split())
            for hall_number in hall_numbers:
                self.halls[hall_number].domain.add(group_number)

        self.e = int(input())

        for c in range(self.e):
            i, j = tuple(map(int, input().split()))
            self.halls[i].constraint.add(j)
            self.constraints.add((i, j))
