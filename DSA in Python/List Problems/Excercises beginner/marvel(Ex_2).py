heros = ["spiderman", "thor", "hulk", "iron man", "captain america"]

print(len(heros))

heros.append("black panther")
print(heros)

heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

heros = heros[:1] + ["doctor strange"] + heros[3:]
print(heros)

heros.sort()
print(heros)
