from csp import CSP
from hall import Hall
from ac3 import ac3

def LCV(csp, hall:Hall, assignment):
    return hall.domain


def MRV(csp:CSP, assignment:dict):
    
    neighbors = [ (i,len(csp.halls[i].domain)) for i in range(1,csp.n+1) ]
    neighbors.sort(key=lambda x: x[1])

    for index_hall, count_of_neighbors_not_assign in neighbors:
        if index_hall not in assignment:
            return index_hall

    return None
        

def forwardChecking(csp:CSP,hall_index:int,value:int):
    hall = csp.halls[hall_index]
    
    csp = csp.copy()
    for neighbor in hall.constraint:
        csp.halls[neighbor].domain = csp.halls[neighbor].domain - {value}
        
    for i in range(1,csp.n+1):
        if hall_index in csp.halls[i].constraint:
            csp.halls[i].domain = csp.halls[i].domain - {value}
            
    return csp


def conflict(csp:CSP, hall_index:int, value, assignment):
    hall = csp.halls[hall_index]
    
    for h in hall.constraint:
        if h in assignment:
            if assignment[h] == value:
                return True
            
    for i in range(1,csp.n+1):
        if hall_index in csp.halls[i].constraint and i in assignment:
            if assignment[i] == value:
                return True
            
    return False


def backtracking(csp:CSP, assignment:dict=dict() , AI_ac3 = False) -> dict():
    if len(assignment) == csp.n: return assignment

    hall_index = MRV(csp, assignment)
    hall = csp.halls[hall_index]

    for value in LCV(csp, hall, assignment):
        if not conflict(csp, hall_index, value, assignment):
            assignment[hall_index] = value
            
            if AI_ac3 :
                _csp = csp.copy()
                if not ac3(_csp): return False
            else:
                _csp = forwardChecking(csp,hall_index,value)
                
            result = backtracking(_csp, assignment)
            
            if result is False :
                assignment.pop(hall_index)
            else:
                return assignment

    return False
