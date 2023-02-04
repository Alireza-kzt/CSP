class Hall:
    def __init__(self, hall: 'Hall' = None):
        if hall is None:
            self.domain = set()
            self.constraint = set()
        else:
            self.domain = hall.domain.copy()
            self.constraint = hall.constraint.copy()

    def copy(self) -> 'Hall':
        return Hall(self)
