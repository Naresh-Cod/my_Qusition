# Chunks of size N

def Break(list):
    end = len(list)
    step = 2
    for i in range(0, end, step):
        x = i
        print(list[x:x + step])

sin = [10, 20, 30, 40, 50, 60, 70, 80]
print("Value is chunks of size 2")
Break(sin)
