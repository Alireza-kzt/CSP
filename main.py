from ac3 import ac3
from csp import CSP
from backtracking import forwardChecking

if __name__ == '__main__':
    csp = CSP.from_input()
    
    print(forwardChecking(csp,csp.halls[3],1).halls[6].domain)