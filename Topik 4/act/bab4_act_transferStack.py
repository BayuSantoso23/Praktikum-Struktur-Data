from linkedliststack import Stack

def transferStack(stackSumber, stackTujuan):
    # Memindahkan semua elemen dari stackSumber ke stackTujuan dalam urutan terbalik
    while not stackSumber.isEmpty():
        stackTujuan.push(stackSumber.pop())

