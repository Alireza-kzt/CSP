from csp import CSP
from hall import Hall
from ac3 import ac3


def lcv(hall: Hall, assignment):
    return sorted(hall.domain, key=lambda value: number_of_conflicts(hall, value, assignment))


def number_of_conflicts(hall, value, assignment) -> int:
    n = 0

    for neighbor in hall.domain:
        if neighbor in assignment:
            if assignment[neighbor] == value:
                n += 1

    return n


def mrv(csp: CSP, assignment: dict):
    neighbors = [(i, len(csp.halls[i].domain)) for i in range(1, csp.n + 1)]
    neighbors.sort(key=lambda x: x[1])

    for index_hall, count_of_neighbors_not_assign in neighbors:
        if index_hall not in assignment:
            return index_hall

    return None


def forward_checking(csp: CSP, hall_index: int, value: int):
    hall = csp.halls[hall_index]

    csp = csp.copy() 
    for neighbor in hall.constraint.union(hall.parent):
        if value in csp.halls[neighbor].domain:
            csp.halls[neighbor].domain.remove(value)

    # for i in range(1, csp.n + 1):
    #     if hall_index in csp.halls[i].constraint:
    #         csp.halls[i].domain = csp.halls[i].domain - {value}

    return csp


def conflict(csp: CSP, hall_index: int, value, assignment):
    hall = csp.halls[hall_index]

    for h in hall.constraint.union(hall.parent):
        if h in assignment:
            if assignment[h] == value:
                return True

    # for i in range(1, csp.n + 1):
    #     if hall_index in csp.halls[i].constraint and i in assignment:
    #         if assignment[i] == value:
    #             return True

    return False


def __backtracking(csp: CSP, assignment: dict) -> dict():
    if len(assignment) == csp.n:
        return assignment

    hall_index = mrv(csp, assignment)
    hall = csp.halls[hall_index]

    for value in lcv(hall, assignment):
        if not conflict(csp, hall_index, value, assignment):
            assignment[hall_index] = value
            csp = forward_checking(csp, hall_index, value)
            result = __backtracking(csp, assignment)
            if result is False:
                assignment.pop(hall_index)
            else:
                return assignment

    return False


def backtracking(csp: CSP, use_ac3=False):
    if use_ac3:
        succeed = ac3(csp)
        if not succeed:
            return "NO"

    assignment = __backtracking(csp, {})
    if assignment:
        return str(assignment.values())
    else:
        return "NO"
