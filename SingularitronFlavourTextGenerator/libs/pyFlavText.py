import random

# 16 very short verbs
# (max 4 letters)
verbShortVeryRoots = [
	"Cod", "Wir", "Add", "Warp", 
	"Zapp", "Form", "Revv", "Tun", 
	"Eat", "Writ", "Send", "Fus", 
	"Hid", "Load", "Read", "Link", 
	"Hack", "Sett", "Link", "Send",
	"Melt", "Pour", "Form", "Sell",
	"Buy"
]

# 36 short verbs
# (max 8 letters)
verbShortRoots = [
	"Build", "Generat", "Initiat", "Remov",
	"Crush", "Steer", "Encrypt", "Insert", 
	"Assembl", "Wrangl", "Align", "Plann",
	"Compil", "Engag", "Fabricat", "Decrypt",
	"Salvag", "Delet", "Encrypt", "Simulat", 
	"Connect", "Plugg", "Boot", "Start",
	"Comput", "Receiv", "Polish", "Packag",
	"3D Print", "Scann", "Remov", "Suspend",
	"Hijack", "Explod", "Detonat", "Solder",
	"Shredd", "Print", "Order"
]

# 11 long verbs
# (max 11 letters)
verbLongRoots = [
	"Calibrat", "Configur", "Reconnect", "Transmitt",
	"[REDACTED]", "Overclock", "Multiply", "Randomis",
	"Construct", "Initialis", "Download"
]

# 11 very short nouns
# (max 4 letters)
nounsShortVery = [
	"data", "bugs", "bits", "AI", 
	"code", "VPN", "lies", "DVDs", 
	"PCBs", "LEDs", "RAM"
]

# 39 nouns so far
# (max 9 letters)
nounsShort = [
	"signal", "Teensy", "Arduino", "cameras", 
	"circuits", "packets", "protocol", 
	"sensors", "wires", "cores", "androids", 
	"vectors", "photons", "waveform", "cables", 
	"numbers", "settings", "nothing.", "lenses",
	"things", "stuff", "disks", "drives", 
	"motors", "servos", "robots", "controls", 
	"notes", "parts"
]

# 20 long nouns
# (max 12 letters)
nounsLong = [
	"registers", "resistors", "capacitors", "dependencies", 
	"connectors", "interfaces", "automatons", "algorithms", 
	"frequencies", "terraflops", "Raspberry Pi", "everything", 
	"kilobytes", "megabytes", "gigabytes", "[REDACTED]",
	"the Matrix", "variables", "controllers", "electrons", 
]

def testingLOL():
	generateVersion = random.randint(0, 2)
	# very short verbs # long nouns
	if generateVersion == 0:
		selectVerb1 = random.choice(verbShortVeryRoots)
		selectVerb2 = selectVerb1+"ing"
		selectNoun = random.choice(nounsLong)
	# long verbs # very short nouns
	elif generateVersion == 1:
		selectVerb1 = random.choice(verbLongRoots)
		if selectVerb1 == "[REDACTED]":
			selectVerb2 = selectVerb1
		else:
			selectVerb2 = selectVerb1+"ing"
		selectNoun = random.choice(nounsShortVery)
	# mid verbs # mid nouns
	elif generateVersion == 2:
		selectVerb1 = random.choice(verbShortRoots)
		selectVerb2 = selectVerb1+"ing"
		selectNoun = random.choice(nounsShort)
	output = selectVerb2+" "+selectNoun
	print(output)
	# (debug) # print(generateVersion)
	return output
