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

def add_paths_from_node(node_name, path, done, node_to_double):
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
        if node_to_double:
            done.append(node_name)
            for neigh_name in node.neighbours:
                add_paths_from_node(neigh_name, path.copy(), done.copy(), node_to_double)
        else:
            for neigh_name in node.neighbours:
                done_if_selected = done.copy()
                done_if_selected.append(node_name)
                add_paths_from_node(neigh_name, path.copy(), done_if_selected, None)
                add_paths_from_node(neigh_name, path.copy(), done.copy(), node.name)
    else:
        for neigh_name in node.neighbours:
            add_paths_from_node(neigh_name, path.copy(), done.copy(), node_to_double)

add_paths_from_node('start', [], [], None)
print(len(set([''.join(path) for path in paths])))
