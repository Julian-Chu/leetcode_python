def main():
    used = set()
    used.add(1)

    if 1 in used:
        used.remove(1)

    # join by using union or update
    set1 = {"a"}
    set2 = {"b"}
    set3 = set1.union(set2)
    set4 = set1.update(set2)
