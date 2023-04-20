# import sys
# from sys import stdin, stdout, stderr

# stdin ==>  keyboard ==> input()
# stdout ==> screen ==> print()
# stderr ==> screen ==> exc

# ---------  stdin  ------------------
# f = stdin.readline()
# print(f)
# ------------------------------------

# ---------  stdout  ------------------
# stdout.write('hi')
# ------------------------------------

# ---------  stderr  ------------------
# stderr.write('Error!!!')
# ------------------------------------

# =============================================================
# بجای نشان دادن داخل اسکرین داخل فایل نشون میده

# stdout_temp = stdout
# stdout = open(file='test.txt', mode='wt')
# stdout.write('hiiiiiii')
# stdout.close()
# stdout = stdout_temp
# =============================================================
# بجای اینکه از کیبورد بخونه از فایل من میخونه
# stdin_temp = sys.stdin
# sys.stdin = open(file='test.txt', mode='rt')
# 
# f = sys.stdin.readline()
# print(f)
# sys.stdin.close()
# 
# sys.stdin = stdin_temp
# =============================================================
# f = open(file='test.txt', mode='wt')
# print('hello goodbye', sep='|', end='\t', file=f, flush=False)
# input()
# =============================================================
