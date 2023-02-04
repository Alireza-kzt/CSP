from csp import CSP
def LCV():
    pass

def MVR():
    pass

def forwardChecking(csp:CSP,assignment:dict):
    pass

def conflict(csp,hall,value,assignment):
    for hall_index in hall.constraint:
        if hall_index in assignment :
            if assignment[hall_index] == value:
                return True
    return False

def backtracking(csp:CSP, assignment:dict=dict()) -> dict():
    if len(assignment) == csp.n: return assignment
    
    hall_index = MVR(csp, assignment)
    hall = csp.halls[hall_index]
    
    for value in LCV(csp,hall.domain,assignment):
        if not conflict(csp,hall,value,assignment):
            assignment[hall_index] = value
            result = backtracking(forwardChecking(csp,hall,value), assignment)
            if result is False :
                result.pop(hall_index)
            else:
                return assignment
    
    return False