from azul2.types import Tile

row_1 = [Tile.BLUE, Tile.YELLOW, Tile.RED, Tile.BLACK, Tile.WHITE]
all_rows = []

for i in range(5):
    row_i = row_1.copy()
    for _ in range(i):
        last_item = row_i.pop()
        row_i.insert(0, last_item)
    all_rows.append(row_i)


for row in all_rows:
    print(row)
