
#
import sys
import os
#
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
        print(f"{elem}",end="")
    print()
    for state in range(state_count):
        i = 0
        while i < len(alphabet):
            if i+1 == len(alphabet):
                print(f"{t_list_d[state][alphabet[i]]}",end="")
            else:
                print(f"{t_list_d[state][alphabet[i]]}",end=" ")
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
    # Print everything if Complement:
    if(sys.argv[1:] == 1):
        printnewdfa(state_count, new_accepted, alphabet, t_list_d)
    return new_accepted

def intersect(a_states, a_acc, alphabet, a_dfa_list, b_states, b_acc, b_dfa_list):
    """
    intersect() takes advantage of complement by complementing both DFAs, finding the union of the DFAs,
    then complementing said union. (DeMorgan's Law)
    """
    complement_a = complement(a_states, a_acc, alphabet, a_dfa_list)
    complement_b = complement(b_states, b_acc, alphabet, b_dfa_list)

    inter_states = a_states + b_states
    accepting_states = complement_a + complement_b
    print(inter_states)
    print(accepting_states)
    print(a_dfa_list)
    print()
    print(b_dfa_list)



def makedict(transitions, alphabet, states_num):
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
    #
    # 
    # Intersection:
    if len(sys.argv[1:]) == 2:
        states_b = ''
        acc_b = ''
        alpha_b = '' # Expected to be the same as A alphabet
        transit_b = ''
        with open(sys.argv[2]) as file_object:
            lines = file_object.readlines()
        for line in lines:
            if states_b == '':
                states_b = line
            elif acc_b == '':
                acc_b = line
            elif alpha_b == '':
                alpha_b = line
            else:
                transit_b = transit_b + line.rstrip() + '\n'
        #
        states_b = int(states_b.rsplit(":", 1)[1])
        acc_b = (acc_b.rsplit(':', 1)[1]).lstrip().rstrip()
        acc_blist = acc_b.split(' ')
        alpha_b = (alpha_b.rsplit(':', 1)[1]).lstrip().rstrip()
        tr_blist = []
        for line in transit_b.split('\n'):
            if line not in '' and line not in ' ':
                tr_blist += [line.split(' ')]
        dfa_b = makedict(tr_blist, alpha_b, states_b)
        intersect(states, acc_list, alpha, dfa_a, states_b, acc_blist, dfa_b)
    else:
        pass

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0 or len(sys.argv[1:]) > 2:
        print("Please refer to the following for correct program arguments:")
        print("For Complement:")
        print(f"> {sys.argv[0]} 'DFA_description text file'")
        print("For Intersection:")
        print(f"> {sys.argv[0]} 'DFA_description text file A' 'DFA_description text file B'")
        sys.exit()
    if os.path.exists("complement_dfa_log.txt"):
        os.remove("complement_dfa_log.txt")
    if os.path.exists("intersection_dfa_log.txt"):
        os.remove("intersection_dfa_log.txt")
    main()