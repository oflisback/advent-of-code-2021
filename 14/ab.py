from collections import Counter

with open('input.txt') as file:
    rows = [row.strip() for row in file.readlines()]

template = list(rows[0])

rule_rows = [[v.strip() for v in inst.split('->')] for inst in rows[2:]]

rules = {}
for rule_row in rule_rows:
    rules[rule_row[0]] = rule_row[1]

mappings = dictlist = [dict() for _ in range(40+1)]

def count(pair, remaining_steps):
    if pair in mappings[remaining_steps].keys():
        return mappings[remaining_steps][pair]

    if (remaining_steps == 0):
        res = Counter(pair)
        return res

    template = pair[0] + rules[''.join(pair)] + pair[1]

    new_steps = remaining_steps - 1
    sub_result = count(template[0] + template[1], new_steps) + count(template[1] + template[2], new_steps) - Counter(template[1])
    if not pair in mappings:
        mappings[remaining_steps][pair] = sub_result

    return sub_result

for steps in [10, 40]:
    total = Counter()
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        total += count(pair, steps)

    total -= Counter(template[1:len(template)-1])
    print(f"Max frequency diff after {steps} steps: {max(total.values()) - min(total.values())}")
