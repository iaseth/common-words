import json

with open("20k.txt") as f:
	text20k = f.read()

words20k = text20k.split("\n")
del words20k[-1]

for x in [10, 100, 1000]:
	for y in range(2, 11):
		n = x * y
		print(f"For n = {n}:")
		words = words20k[:n]

		txt_filename = f"txt/{n}.txt"
		text = "\n".join(words)
		with open(txt_filename, "w") as f:
			f.write(text)
			print(f"\tSaved: {txt_filename}")

		json_filename = f"json/{n}.json"
		jo = {}
		jo["words"] = words
		with open(json_filename, "w") as f:
			json.dump(jo, f)
			print(f"\tSaved: {json_filename}")
		print

