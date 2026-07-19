def infinite_chai():
    count = 1
    while True:
        yield f"chai no #{count}"
        count += 1


chai_ord = infinite_chai()
user2 = infinite_chai()

for _ in range(10):
    print(next(chai_ord))

for _ in range(5):
    print(next(user2))