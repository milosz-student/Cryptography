import itertools
from enigma.machine import EnigmaMachine
from string import ascii_uppercase
rotors = ["I", "II", "IV", "V", "VI", "VII", "VIII", 'III'] # , "Beta"]
reflectors = ['B', 'C', 'B-Thin', 'C-Thin']
# M4 / UKW ? / Beta ??? ??? ??? / 18 14 . . / T H G B/ wh at re yu lo ki ng fs qx cm
 
# Ciphertext: 'qtdaxvuvzxwbojdcatgxzpawfhenoor'
# 18th alphabet: 'R'
# 14th alphabet: 'N'
alphabet = ascii_uppercase.replace('Q', '').replace('T', '')
for rf in reflectors:
	for rotor in itertools.permutations(rotors, 3):
		for display in itertools.product(alphabet, repeat=2):
			actual = ['Beta'] + list(rotor)
			engine = EnigmaMachine.from_key_sheet(
				rotors=actual,
				ring_settings=f"R N {display[0]} {display[1]}",
				reflector=rf,
				plugboard_settings="WH AT RE YU LO KI NG FS QX CM")
			engine.set_display("THGB")
			plaintext = engine.process_text("qtdaxvuvzxwbojdcatgxzpawfhenoor".upper())
			if "PING" in plaintext[:4]:
				print("FOUND")
				print("REFLECTOR: ", rf)
				print("ROTORS: ", actual)
				print("DISPLAY: ", "THGB")
				print("RING: ", f"R N {display[0]} {display[1]}")
				print("PLAINTEXT: ", plaintext)
				print()
