example1 = "III"
example2 = "IV"


def romanToInt(s: str) -> int:
	number = 0
	romanNumber = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000
	}

	for character in range(0, len(s)-1):

		# If the next number is less than current number, then we just add as normal
		
		if romanNumber[s[character + 1]] <= romanNumber[s[character]]:
			number += romanNumber[s[character]]
		else:
			# If the next number is greater than current number, need to subtract current numbers value
			number -= romanNumber[s[character]]

	return number + romanNumber[s[-1]]


print(romanToInt(example1))
print(romanToInt(example2))
