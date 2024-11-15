import ctypes

CArray = ctypes.py_object * 5
slots = CArray()

for i in range(5):
    slots[i] = None

slots[1] = 12
slots[3] = 54
slots[4] = 39

print(slots[1])

slots[3] = None

print(slots[3])
