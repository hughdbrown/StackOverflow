import base64
def translate_uuid(uuid):
	def get_lookup_table():
		b = list(str(i) for i in range(10)) + list("abcdef")
		return dict((k,v) for v,k in enumerate(b))
	a = uuid.replace('-', '')
	table = get_lookup_table()
	x = [chr(table[c1]*16 + table[c2]) for c1, c2 in zip(a[::2], a[1::2])]
	return base64.b64encode("".join(x))

def b85encode(x):
	table = 
	result = []


if __name__ == '__main__':
	guid = '9f218a38-12cd-5942-b877-80adc0589315'
	new_guid = translate_uuid(guid)
	print guid, len(guid)
	print new_guid, len(new_guid)
