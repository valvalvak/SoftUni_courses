mydict = {'cheese': 2, 'tomatoes': 1}
result = []
for k, v in mydict.items():
    result.extend([f"{k}: {str(v)}"])
print(", ".join(x for x in result))
