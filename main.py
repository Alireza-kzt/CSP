from csp import CSP
from backtracking import backtracking
from datetime import datetime

if __name__ == '__main__':
    start = datetime.now()
    csp = CSP.generate(500,500,1000)
    end = datetime.now()
    print(end-start)
    start = datetime.now()
    print(backtracking(csp.copy()))
    end = datetime.now()
    print(end-start)
    start = datetime.now()
    print(backtracking(csp.copy(),AI_ac3=True))
    end = datetime.now()
    print(end-start)
    
