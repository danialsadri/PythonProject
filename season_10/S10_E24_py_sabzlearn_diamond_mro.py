class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print('Calling method on BaseClass!!!')
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print('Calling method on LeftSubClass!!!')
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print('Calling method on RightSubClass!!!')
        self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        # LeftSubClass.call_me(self)
        # RightSubClass.call_me(self)
        super().call_me()
        print('Calling method on SubClass!!!')
        self.num_sub_calls += 1


s = SubClass()
s.call_me()
print(f"{s.num_sub_calls} {s.num_left_calls} {s.num_right_calls} {s.num_base_calls}")
print(SubClass.__mro__)

# =====================  result ==========================
# Calling method on BaseClass!!!
# Calling method on RightSubClass!!!
# Calling method on LeftSubClass!!!
# Calling method on SubClass!!!
# 1 1 1 1
# (<class '__main__.SubClass'>,
#  <class '__main__.LeftSubClass'>,
#  <class '__main__.RightSubClass'>,
#  <class '__main__.BaseClass'>,
#  <class 'object'>)
