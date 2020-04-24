class AvailableValues:
    values = []

    def __init__(self):

        values = []
        for value in range(1, 10):
            values.append(value)

        self.values = values


class Vector(AvailableValues):

    def is_exist(self, n):
        if n in self.values:
            return True
        else:
            return False
