from csp import CSP


def ac3(csp: CSP) -> bool:
    queue = list(csp.constraints)

    while len(queue) != 0:
        i, j = queue.pop(0)
        if revise(csp, i, j):
            if len(csp.halls[i].domain) == 0:
                return False
            for k in (csp.halls[i].constraint - {j}):
                if (k, i) not in queue:
                    queue.append((k, i))

    return True


def revise(csp, i, j) -> bool:
    revised = False
    deleted = set()

    for x in csp.halls[i].domain:
        if not csp.halls[j].domain - {x}:
            deleted.add(x)
            revised = True

    csp.halls[i].domain = csp.halls[j].domain - deleted

    return revised
