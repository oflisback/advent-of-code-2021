from node import Node

def find_node(name, nodes):
    return next((n for n in nodes if n.name == name), None)

with open('input.txt') as file:
    rows = [row.strip().split('-') for row in file.readlines()]

nodes = []

for row in rows:
    for i, name in enumerate(row):
        node = find_node(name, nodes)
        if not node:
            node = Node(name)
            nodes.append(node)
        node.add_path(row[(i + 1) % 2])

paths = []

def add_paths_from_node(node_name, path, done):
    node = find_node(node_name, nodes)
    if node.name in done:
        return
    if len(path) > 0 and node.name == "start":
        return
    path.append(node.name)
    if node.name == "end":
        paths.append(path)
        return
    if node.small:
        done.append(node.name)
    for neigh_name in node.neighbours:
        add_paths_from_node(neigh_name, path.copy(), done.copy())

add_paths_from_node('start', [], [])
print(f"Nbr paths: {len(paths)}")
