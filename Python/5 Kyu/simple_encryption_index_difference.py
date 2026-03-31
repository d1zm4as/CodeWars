# Encryption region definition
REGION = (
	''.join([chr(i) for i in range(ord('A'), ord('Z')+1)]) +
	''.join([chr(i) for i in range(ord('a'), ord('z')+1)]) +
	''.join([chr(i) for i in range(ord('0'), ord('9')+1)]) +
	".,:;-?! '()$%&\""
)

def encrypt(text):
	if text is None or text == '':
		return text
	if any(c not in REGION for c in text):
		raise Exception('Invalid character in input')

	# Step 1: Switch case for every second char
	chars = list(text)
	for i in range(1, len(chars), 2):
		c = chars[i]
		if c.islower():
			chars[i] = c.upper()
		elif c.isupper():
			chars[i] = c.lower()
		# else leave unchanged
	# Step 2: Index difference encoding
	encoded = [chars[0]]
	for i in range(1, len(chars)):
		idx_prev = REGION.index(chars[i-1])
		idx_cur = REGION.index(chars[i])
		diff = (idx_prev - idx_cur) % len(REGION)
		encoded.append(REGION[diff])
	# Step 3: Mirror first char
	idx_first = REGION.index(encoded[0])
	mirrored = REGION[len(REGION)-1 - idx_first]
	encoded[0] = mirrored
	return ''.join(encoded)

def decrypt(encrypted_text):
	if encrypted_text is None or encrypted_text == '':
		return encrypted_text
	if any(c not in REGION for c in encrypted_text):
		raise Exception('Invalid character in input')

	# Step 3: Unmirror first char
	idx_mirrored = REGION.index(encrypted_text[0])
	orig_first = REGION[len(REGION)-1 - idx_mirrored]
	decoded = [orig_first]
	# Step 2: Reverse index difference
	for i in range(1, len(encrypted_text)):
		idx_prev = REGION.index(decoded[i-1])
		idx_cur = REGION.index(encrypted_text[i])
		orig_idx = (idx_prev - idx_cur) % len(REGION)
		decoded.append(REGION[orig_idx])
	# Step 1: Reverse case switch for every second char
	for i in range(1, len(decoded), 2):
		c = decoded[i]
		if c.islower():
			decoded[i] = c.upper()
		elif c.isupper():
			decoded[i] = c.lower()
	return ''.join(decoded)
