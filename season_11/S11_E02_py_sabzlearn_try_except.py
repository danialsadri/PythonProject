# while True:
#     try:
#         x = int(input('x: '))
#         break
#     except:
#         print('Try again...')
#
# print(x)
# -----------------------------------------------
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     z = x / y
#
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ValueError:
#     print('ValueError')
# except TypeError:
#     print('TypeError')
# except:
#     print('Error')
# -----------------------------------------------
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     z = x / y + 'a'
#
# except(ZeroDivisionError, ValueError) as E:
#     print('ZeroDivisionError or ValueError')
#     print(f'{E}')
#     print(E.__class__.__name__)
#
# except TypeError as T:
#     print('TypeError')
#     print(f'{T}')
#     print(T.__class__.__name__)
#
# except:
#     print('Error')
# -----------------------------------------------
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     z = x / y
# except Exception as Ex:
#     print(Ex.__class__.__name__)
# -----------------------------------------------
