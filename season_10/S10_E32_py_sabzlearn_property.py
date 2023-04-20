# class Color:
#     def __init__(self, rgb, name):
#         self._rgb = rgb
#         if name:
#             self._name = name
#         else:
#             raise ValueError(f'Invalid name {name!r}')
#
#     def set_name(self, name):
#         if name:
#             self._name = name
#         else:
#             raise ValueError(f'Invalid name {name!r}')
#
#     def get_name(self):
#         return self._name
#
#     def set_rgb(self, rgb):
#         self._rgb = rgb
#
#     def get_rgb(self):
#         return self._rgb
#
#
# c1 = Color(rgb=0x6783F5, name='light blue')
# print(f"rgb: {c1.get_rgb()} name: {c1.get_name()}")
# c1.set_rgb(0x091B66)
# c1.set_name('blue')
# print(f"rgb: {c1.get_rgb()} name: {c1.get_name()}")
#
#
# c2 = Color(rgb=0xED1F1F, name='light red')
# print(f"rgb: {c2._rgb} name: {c2._name}")
# c2._rgb = 0xED1F1F
# c2._name = 'red'
# print(f"rgb: {c2._rgb} name: {c2._name}")
# ====================================================================================
class Color:
    def __init__(self, rgb, name):
        self.rgb = rgb
        self.name = name

    def _set_name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f'Invalid name {name!r}')

    def _get_name(self):
        return self._name

    def _set_rgb(self, rgb):
        self._rgb = rgb

    def _get_rgb(self):
        return self._rgb

    name = property(fget=_get_name, fset=_set_name)
    rgb = property(fget=_get_rgb, fset=_set_rgb)


# c1 = Color(rgb=0x6783F5, name='light blue')
# print(f"rgb: {c1._get_rgb()} name: {c1._get_name()}")
# c1._set_rgb(0x091B66)
# c1._set_name('blue')
# print(f"rgb: {c1._get_rgb()} name: {c1._get_name()}")


c2 = Color(rgb=0xED1F1F, name='light red')
print(f"rgb: {c2.rgb} name: {c2.name}")
c2.rgb = 0xED1F1F
c2.name = 'red'
print(f"rgb: {c2.rgb} name: {c2.name}")

