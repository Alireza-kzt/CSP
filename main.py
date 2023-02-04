from csp import CSP
from backtracking import backtracking
from datetime import datetime

if __name__ == '__main__':
    csp = CSP.from_input()
    
    start = datetime.now()
    print(backtracking(csp.copy()))
    end = datetime.now()
    print(end-start)
    start = datetime.now()
    print(backtracking(csp.copy(),AI_ac3=True))
    end = datetime.now()
    print(end-start)
    
