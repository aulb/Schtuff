def encrypt(latin_string):
	"""
	Assume valid lowercase latin alphabets.
	"crime" -> "dnotq"
	"""
	if not latin_string: return ""

	low, high = ord('a'), ord('z')
	prev = ord(latin_string[0]) + 1 # if 'z' is passed in
	encrypted = chr(prev) if prev <= high else chr(prev - 26)

	for i in range(1, len(latin_string)):
		prev = curr = prev + ord(latin_string[i])
		while not(low <= curr <= high):
			curr -= 26
		encrypted += chr(curr)
	return encrypted

def decrypt(encrypted_string):
	if not encrypted_string: return ""

	low, high = ord('a'), ord('z')
	prev = ord(encrypted_string[0]) - 1
	decrypted = chr(prev) if prev >= low else chr(prev + 26)
	prev = prev + 1

	for i in range(1, len(encrypted_string)):
		curr = ord(encrypted_string[i]) - prev
		while not (low <= curr <= high):
			curr += 26
		decrypted += chr(curr)

		prev = prev + curr

	return decrypted

if __name__ == '__main__':
	print(decrypt(encrypt('a')))
