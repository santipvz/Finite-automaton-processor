import sys

def main():

	if(len(sys.argv) != 3):
		print("Number of argmunets incorrect")
		return

	# Load
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()

		states = []  # First state == initial state
		final_state = []
		alphabet = []
		transitions = {}

		# Process first 3 lines
		for i in range(3):
			for word in lines[i].strip().split(" "):
				if i == 0:
					states.append(word)
				elif i == 1:
					final_state.append(word)
				elif i == 2:
					alphabet.append(word)

		# Empty
		alphabet.append('λ')
 
		# Process transitions
		for state_index, line in enumerate(lines[4:]):
			transitions[states[state_index]] = {}  # New hashmap for current state
			next_states = line.split("#")
			for index, alphabet_entry in enumerate(alphabet): # For each entry save his next states
				transitions[states[state_index]][alphabet_entry] = next_states[index].strip(' ').split(' ')


	#### MAIN FUNCTIONALITY ####
	initial_state = []
	future_states = []
	
	# Calculate empty clausure
	next_states = [states[0], ]
	while(next_states):
		for state in next_states:
			if(state not in initial_state):
				future_states.extend(transitions[state]["λ"])
				initial_state.append(state) # Add state to clausure
		
		while("" in future_states):
			future_states.remove("")

		next_states = list(set(future_states))
		future_states = []


	next_states = initial_state

	print(f"Initial state: {next_states}")

	# Process each entry
	for character in sys.argv[2]:
		print("Entry: " + character, end=" --> ")
		for state in next_states:
			future_states.extend(transitions[state][character])
			future_states.extend(transitions[state]["λ"])

		while("" in future_states):
			future_states.remove("")

		next_states = list(set(future_states)) # Remove duplicates
		future_states = []
		print(f"New state: {next_states}")

	for state in next_states:
		if state in final_state:
			print(f"{state} --> ACCEPTED")
		else:
			print(f"{state} --> REJECTED")

	print("\nPress ENTER to exit")
	input()


if __name__=="__main__":
	main()