from csp import CSP
from hall import Hall


def LCV():
    pass


def MVR(csp:CSP, assignment:dict):
    
    neighbors = [ (i,len(csp.halls[i].domain)) for i in range(1,csp.n+1) ]
    neighbors.sort(key=lambda x: x[1])

    for index_hall, count_of_neighbors_not_assign in neighbors:
        if index_hall not in assignment:
            return index_hall

    return None
        

def forwardChecking(csp:CSP,hall:Hall,hall_index:int,value:int):
    csp = csp.copy()
    for neighbor in hall.constraint:
        csp.halls[neighbor].domain = csp.halls[neighbor].domain - {value}
        
    for i in range(1,csp.n+1):
        if hall_index in csp.halls[i].constraint:
            csp.halls[i].domain = csp.halls[i].domain - {value}
            
    return csp


def conflict(csp, hall, value, assignment):
    for hall_index in hall.constraint:
        if hall_index in assignment:
            if assignment[hall_index] == value:
                return True
    return False


def backtracking(csp:CSP, assignment:dict=dict()) -> dict():
    if len(assignment) == csp.n: return assignment

    hall_index = MVR(csp, assignment)
    hall = csp.halls[hall_index]

    for value in LCV(csp, hall.domain, assignment):
        if not conflict(csp, hall, value, assignment):
            assignment[hall_index] = value
            result = backtracking(forwardChecking(csp,hall,hall_index,value), assignment)
            if result is False :
                assignment.pop(hall_index)
            else:
                return assignment

    return False
