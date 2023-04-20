class First(object):
    def __init__(self):
        print('first')


class Second(First):
    def __init__(self):
        super().__init__()
        print('Second')


class Third(Second):
    def __init__(self):
        super().__init__()
        print('Third')


class Fourth(Third):
    def __init__(self):
        super().__init__()
        print("that's is it")


Fourth()
