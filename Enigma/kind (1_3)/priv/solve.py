import itertools
from enigma.machine import EnigmaMachine
rotors = ["I", "II", "IV", "V", "VI", "VII", "VIII", 'Beta'] # , "III"]
reflectors = ['B', 'C', 'B-Thin', 'C-Thin']
# M3 / UKW ? / III ??? ??? / 10 6 9 / 7 15 12 / gi ve to yb ac kp lz xr qh fn
 
# “Ciphertext: gjmsjnjbijovlrcnkem” 
# 10 6 9		|	j f i
# 7 15 12		|	g o l

for rf in reflectors:
	for rotor in itertools.permutations(rotors, 2):
		actual = ['III'] + list(rotor)
		engine = EnigmaMachine.from_key_sheet(
			rotors=actual,
			ring_settings="J F I",
			reflector=rf,
			plugboard_settings="GI VE TO YB AC KP LZ XR QH FN")
		engine.set_display("GOL")
		plaintext = engine.process_text("gjmsjnjbijovlrcnkem".upper())
		if "PING" in plaintext:
			print("FOUND")
			print("REFLECTOR: ", rf)
			print("ROTORS: ", actual)
			print("PLAINTEXT: ", plaintext)
