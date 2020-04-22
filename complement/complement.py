"""
Program written by Luis Baez.
Complement a DFA given a description of a DFA. Output
to standard out using the complemented DFA.
"""
import sys
def printnewdfa(state_count, accepted, alphabet, t_list_d):
    """
    printnewdfa() prints out a dfa description formatted as
    requried. Exactly the same as the input dfa descriptions.
    The description is printed to standard output.
    """
    print(f"Number of states: {state_count}")
    print(f"Accepting states:", end=' ')
    for elem in accepted:
        if elem == accepted[-1]:
            print(f"{elem}", end='')
        else:
            print(f"{elem}", end=' ')
    print()
    print("Alphabet:", end=' ')
    for elem in alphabet:
        print(f"{elem}", end="")
    print()
    for state in range(state_count):
        i = 0
        while i < len(alphabet):
            if i+1 == len(alphabet):
                print(f"{t_list_d[state][alphabet[i]]}", end="")
            else:
                print(f"{t_list_d[state][alphabet[i]]}", end=" ")
            i = i + 1
        print()

def complement(state_count, accepted, alphabet, t_list_d):
    """
    complement() complements a DFA by turning originally normal states into
    accepting states and originally accepting states into normal states.
    """
    new_accepted = []
    for state in range(state_count):
        if str(state) not in accepted:
            new_accepted.append(int(state))
    printnewdfa(state_count, new_accepted, alphabet, t_list_d)
    return new_accepted

def makedict(transitions, alphabet, states_num):
    """
    makedict() fills a list of dictionaries for the DFA. Each index of the list will contain a
    dictionary for the state corresponding to the index.
    i.e list.at(1) = transitions for state 1.
    """
    list_of_dicts = []
    push_defined = {} # Empty dictionary for the transitions of each state
    for state in range(states_num):
        i = 0
        while i < len(alphabet):
            push_defined[alphabet[i]] = transitions[state][i]
            i = i + 1
        if push_defined:
            push_defined_copy = push_defined.copy()
            list_of_dicts.append(push_defined_copy)
            push_defined = {}

    # print(list_of_dicts)
    return list_of_dicts

def main():
    """
    main() reads the files, parses the information into usable formats,
    and calls on one function to start the complementing.
    """
    states = ''
    acc_states = ''
    alpha = ''
    transit = ''
    # if len(sys.argv[1:]) == 1:
    with open(sys.argv[1]) as file_object:
        lines = file_object.readlines()
    for line in lines:
        if states == '':
            states = line
        elif acc_states == '':
            acc_states = line
        elif alpha == '':
            alpha = line
        else:
            transit = transit + line.rstrip() + '\n'
    #
    states = int(states.rsplit(":", 1)[1])
    acc_states = (acc_states.rsplit(':', 1)[1]).lstrip().rstrip()
    acc_list = acc_states.split(' ')
    alpha = (alpha.rsplit(':', 1)[1]).lstrip().rstrip()
    tr_list = []
    for line in transit.split('\n'):
        if line not in '' and line not in ' ':
            tr_list += [line.split(' ')]
    dfa_a = makedict(tr_list, alpha, states)

    complement(states, acc_list, alpha, dfa_a)

if __name__ == "__main__":
    main()
