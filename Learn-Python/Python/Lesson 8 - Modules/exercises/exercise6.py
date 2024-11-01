# Create a list comprehension for a battlship board
# [A-E], [1-5]
# [A1,A2,...,B1,B2,...,E5]
# Remove the value C3

battleship_board = [
    f"{a}{b}"
    for a in ("A", "B", "C", "D", "E")
    for b in range(1, 6)
    if f"{a}{b}" != "C3"
]
print(battleship_board)
