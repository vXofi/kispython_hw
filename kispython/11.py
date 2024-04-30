class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def code(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise MealyError('code')

    def chalk(self):
        if self.state == 'A':
            self.state = 'C'
            return 2
        if self.state == 'B':
            self.state = 'D'
            return 4
        if self.state == 'C':
            self.state = 'E'
            return 6
        if self.state == 'D':
            self.state = 'E'
            return 7
        else:
            raise MealyError('chalk')

    def load(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 5
        else:
            raise MealyError('load')


def test():
    o = main()

    assert o.code() == 0
    o.state = 'E'
    assert o.code() == 8
    o.state = 'F'
    try:
        o.code()
    except MealyError:
        pass

    o.state = 'A'
    assert o.chalk() == 2
    o.state = 'C'
    assert o.chalk() == 6
    o.state = 'B'
    assert o.chalk() == 4
    o.state = 'D'
    assert o.chalk() == 7
    o.state = 'F'
    try:
        o.chalk()
    except MealyError:
        pass

    o.state = 'A'
    assert o.load() == 1
    o.state = 'B'
    assert o.load() == 3
    o.state = 'C'
    assert o.load() == 5
    o.state = 'F'
    try:
        o.load()
    except MealyError:
        pass


def main():
    return Mealy()


test()
