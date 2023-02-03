def ac3(csp) -> bool:
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

    for x in csp.halls[i].domain.copy():
        if not csp.halls[j].domain - {x}:
            csp.halls[j].domain.remove(x)
            revised = True

    return revised
