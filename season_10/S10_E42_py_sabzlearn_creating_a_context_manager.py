# from season_9 import S09_E08_py_sabzlearn_with_as <== توضیحات کامل

# ------------------------------------------------------------
# class A:
#     def __enter__(self):
#         print('Start!!!')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('End!!!')
#
#
# with A() as a:
#     print("*" * 20)
#     print(a.__class__)
#     print('danial')
#     print("*" * 20)
# ------------------------------------------------------------
# class A:
#     def __enter__(self):
#         print('Start!!!')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         print('End!!!')
# #       return True
#
#
# with A() as a:
#     print("*" * 20)
#     print(10/0)
#     print('danial')
#     print("*" * 20)
# ------------------------------------------------------------
# class FileManager:
#     def __init__(self, filename, mode):
#         self.file_name = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         print('the file was opened.')
#         self.file = open(file=self.file_name, mode=self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('the file was closed.')
#         self.file.close()
#
#
# with FileManager(filename='test.txt', mode='wt') as f:
#     f.write('hello')
#
# print(f.closed)
# ------------------------------------------------------------
