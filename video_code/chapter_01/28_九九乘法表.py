for row in range(1, 10):
    for item in range(1, row + 1):
        print(f"{item}*{row}={item * row}", end="\t")
    print()
