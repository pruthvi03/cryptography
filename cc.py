class Caesar():

	def encrypt(self, plain_txt, key):
		result_txt = ""
		
		for i in plain_txt:
			if (i.isupper()):
				result_txt += chr( ( ( ord(i) - 65 + key ) % 26) + 65 )
				# print(ch)
			elif (i.islower()):
				result_txt += chr( ( ( ord(i) - 97 + key ) % 26) + 97 )
			else:
				pass 
		return result_txt

	def decrypt(self, encrypt_txt, key):
		result_txt = ""
		
		for i in encrypt_txt:
			if (i.isupper()):
				result_txt += chr( ( ( ord(i) - 65 - key ) % 26) + 65 )
				# print(ch)
			elif (i.islower()):
				result_txt += chr( ( ( ord(i) - 97 - key ) % 26) + 97 )
			else:
				pass
		return result_txt
	def brute_decrypt(self, encrypt_txt, low_limit ,up_limit):
		result_txt = ""
		for j in range(low_limit,(up_limit+1)):
			for i in encrypt_txt:
				if (i.isupper()):
					result_txt += chr( ( ( ord(i) - 65 - j ) % 26) + 65 )
					# print(ch)
				elif (i.islower()):
					result_txt += chr( ( ( ord(i) - 97 - j ) % 26) + 97 )
				else:
					pass
			print("Key :",j," Result text :",result_txt)
			result_txt = ""

# Create Object of Caesar Class 
obj = Caesar()

# Call encrypt() function of Caser Class and pass plain text and key 
encrypt_txt = obj.encrypt(input("Enter a plain text: "),int(input("Enter a key(integer): ")))
print(encrypt_txt)
# Call decrypt() function of Caser Class and pass encrypted text and key
decrypt_text = obj.decrypt(input("Enter a encrypted text: "),int(input("Enter a key(integer): "))) 
print(decrypt_text)

print("\t\tBrute Force Approch")
# Call brute_decrypt() function of Caser Class and pass plain text and range of key
obj.brute_decrypt(input("Enter a encrypted text: "),int(input("Enter a lower key(integer): ")),
	int(input("Enter a upper key(integer): ")))
