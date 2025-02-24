import sys

def main():
    if len(sys.argv) != 3:
        print("Error: Incorrect number of arguments. Usage: script.py <file> <string>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: Could not open the input file.")
        sys.exit(1)

    # Read states, final states, alphabet and transitions
    states, final_state, alphabet = [line.strip().split() for line in lines[:3]]
    alphabet.append('λ')  # Add lambda to the alphabet

    # Initialize transitions dictionary
    transitions = {}
    for state in states:
        transitions[state] = {symbol: [] for symbol in alphabet}

    for state_index, line in enumerate(lines[4:]):
        next_states = line.split("#")
        for index, symbol in enumerate(alphabet):
            transitions[states[state_index]][symbol] = next_states[index].split()

    #### CALCULATE LAMBDA CLOSURE ####
    initial_state = set()
    stack = [states[0]]  # Use a stack to avoid re-calculation

    while stack:
        state = stack.pop()
        if state not in initial_state:
            initial_state.add(state)
            stack.extend(transitions[state]["λ"])

    next_states = list(initial_state)
    print(f"Initial state: {next_states}")

    #### PROCESS EACH CHARACTER OF THE INPUT ####
    for character in sys.argv[2]:
        print(f"Input: {character} --> ", end="")
        next_states = {new_state for state in next_states for new_state in transitions[state][character] + transitions[state]["λ"] if new_state}
        print(f"New state: {list(next_states)}")

    #### CHECK FINAL STATE ####
    if any(state in final_state for state in next_states):
        print(f"{state} --> ACCEPTED")
    else:
        print(f"{state} --> REJECTED")

    input("\nPress ENTER to exit")
    

if __name__ == "__main__":
    main()