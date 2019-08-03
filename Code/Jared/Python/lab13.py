from string import(ascii_lowercase as lower, ascii_uppercase as upper)

def encode(text, rotation=13):
	cypher = []
	for letter in text:
		if letter.islower():
			cypher.append(lower[(lower.find(letter) + rotation) % 26])
		elif letter.isupper():
			cypher.append(upper[(upper.find(letter) + rotation) % 26])
		else:
			cypher.append(letter)

	return ''.join(cypher)

def decode(text, rotation=-13):
	cypher = []
	for letter in text:
		if letter.islower():
			cypher.append(lower[(lower.find(letter) + rotation) % 26])
		elif letter.isupper():
			cypher.append(upper[(upper.find(letter) + rotation) % 26])
		else:
			cypher.append(letter)

	return ''.join(cypher)


print(encode('Hi there'))
print(decode('Uv gurer'))