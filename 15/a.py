import networkx as nx
from networkx.classes.function import path_weight

with open('input.txt') as file:
    rows = [[int(v) for v in list(row.strip())] for row in file.readlines()]

G = nx.DiGraph()

X, Y = len(rows[0]), len(rows)

for y, row in enumerate(rows):
    for x, v in enumerate(row):
      G.add_node(f"{x},{y}")
      if x > 0: G.add_edge(f"{x},{y}", f"{x-1},{y}", weight=rows[y][x-1])
      if x < X - 1: G.add_edge(f"{x},{y}", f"{x+1},{y}", weight=rows[y][x+1])
      if y > 0: G.add_edge(f"{x},{y}", f"{x},{y-1}", weight=rows[y-1][x])
      if y < Y - 1: G.add_edge(f"{x},{y}", f"{x},{y+1}", weight=rows[y+1][x])

path = nx.shortest_path(G, f'{0},{0}', f'{X-1},{Y-1}', weight='weight')

print(f"Weight: {path_weight(G, path, weight='weight')}")
