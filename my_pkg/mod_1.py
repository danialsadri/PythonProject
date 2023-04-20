def func_1(x):
    return x ** 2


def func_2(s):
    return s.lower()


def _func_3(x, y):
    return x ** y


number = 10
name = 'danial_sadri'
_age = 17

# ---------------------------------
if __name__ == '__main__':
    print(func_1(number))
    print(func_2('danial'))
    print(_func_3(_age, 2))
    print(__name__)
