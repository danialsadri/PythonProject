# class DigitError(Exception):
#     def __init__(self, s, message='Error'):
#         self.message = message
#         self.s = s
#         super().__init__(self.message)
#
#     def __str__(self):
#         return "DigitError"
#
#
# def func(s):
#     if not s.isdigit():
#         raise DigitError(s, 'the string deos not contain only numbers!!!')
#     numbers = []
#     for i in s:
#         numbers.append(int(i))
#     print(numbers)
#
#
# try:
#     func('0939p')
# except DigitError as de:
#     print(de)
#
# print('Ok!!!')
