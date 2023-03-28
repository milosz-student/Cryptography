import itertools
from enigma.machine import EnigmaMachine
from string import ascii_uppercase
from time import time
'''
“We are worried for Mr. Kowalski's Wife. We have search his father house and he was gone,
but he left the ciphermessage on the table. Next to written on the table TOOLATE Can you
recover the message?”

M3 / UKW ? / ??? ??? ??? / D I E / ... / w? xs ol de vi jq hu rt fa mz
“Ciphertext: rjzdexbilwzqpabtjpmsppwscbcnhpykjidgkg” 
'''
rotors = ["I", "II", "IV", "V", "VI", "VII", "VIII", "III", "Beta"]
plug_to_replace = "xs ol de vi jq hu rt fa mz w".replace(" ", "").upper()
plug_board_alphabet = ""
for c in ascii_uppercase:
	if not c in plug_to_replace:
		plug_board_alphabet += c
rotors_alphabet = itertools.permutations(rotors, 3)
reflectors_alphabet = ['B', 'C', 'B-Thin', 'C-Thin']
display_alphabet = itertools.product(ascii_uppercase, repeat=3)
display_alphabet_as_list = []
for i in display_alphabet:
	display_alphabet_as_list.append(list(i))

ciphertext = "rjzdexbilwzqpabtjpmsppwscbcnhpykjidgkg"
rotors_alphabet_as_list = []
for rotorz in rotors_alphabet:
	rotors_alphabet_as_list.append(list(rotorz))

start_time = time()
for rf in reflectors_alphabet:
	for rotorz in rotors_alphabet_as_list:
		for plug_1 in plug_board_alphabet:
			for dp in display_alphabet_as_list:
				plugz = f" w{plug_1} xs ol de vi jq hu rt fa mz".upper()
				ringz = f"D I E"
				displayz = f"{dp[0]}{dp[1]}{dp[2]}"
				engine = EnigmaMachine.from_key_sheet(
					rotors=rotorz,
					ring_settings=ringz,
					reflector=rf,
					plugboard_settings=plugz)
				engine.set_display(displayz)
				plaintext = engine.process_text(ciphertext.upper(), matching="PING")
				if "PING" in plaintext[:4] and "TOOLATE" in plaintext:
					print("FOUND")
					print("REFLECTOR: ", rf)
					print("ROTORS: ", rotorz)
					print("DISPLAY: ", displayz)
					print("RING: ", ringz)
					print("PLAINTEXT: ", plaintext)
					print("PLUGBOARD: ", plugz)
					end_time = time()
					print("Time: ", end_time - start_time)
					print()
end_time = time()
print("Time: ", end_time - start_time)


# FOUND
# REFLECTOR:  B
# ROTORS:  ['II', 'IV', 'III']
# DISPLAY:  NBK
# RING:  D I E
# PLAINTEXT:  PINGTOOLATEYOUWILLNEVERFINDHERANDMYSON
# PLUGBOARD:   WY XS OL DE VI JQ HU RT FA MZ
# Time:  1190.2077322006226