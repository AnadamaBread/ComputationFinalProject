"""
Determine the properties of a DFA by reading the 
DFA description from a text file and write to 
standard output (console):
1. if the language is empty
2. if the language is finite
Note:
1. nonempty <=> final state is reachable from start state.
#
2. infinite <=> there exists some cycle that is 
reachable from the start state which can reach a 
final state.
"""
#
import sys
import os
#
def trace_final(state, alphabet, list_of_dicts, accepted_list, visited_list):
    curr_state = state
    if int(curr_state) not in visited_list:
        visited_list.append(int(curr_state))
    # else:
    #     return visited_list
        # curr_state = int(state)
    if str(curr_state) not in accepted_list:
        for elem in alphabet:
            next_state = list_of_dicts[curr_state][elem]
            # print (next_state)
            # if str(next_state) not in accepted_list:
            #     if int(next_state) in visited_list:
            #         trace_final(int(next_state), alphabet, list_of_dicts, accepted_list, visited_list)
            #         #break
            #     else:
            #         visited_list.append(int(next_state))
            #         trace_final(int(next_state), alphabet, list_of_dicts, accepted_list, visited_list)
            # else:
            #     if str(next_state) not in visited_list:
            #         visited_list.append(int(curr_state))
            #         break
            if int(next_state) in visited_list:
                break
            else:
                visited_list.append(int(next_state))
            if str(next_state) in accepted_list:
                return visited_list
            else:
                trace_final(int(next_state), alphabet, list_of_dicts, accepted_list, visited_list)
    else:
        if int(curr_state) not in visited_list:
            visited_list.append(int(curr_state))
    return visited_list
        
            

    



def properties(state_num, accepted_list, alphabet, trans_list):
    """
    properties() first creates a dictionary of all the transitions,
    then does the following two things:
    1. Loop from any state, can said state reach the final state? 
    If yes, DFA language is nonempty.
    2. A loop from the start state, reading any string of any length (start at 
    length = 1 then increase). If the end state after reading said string is the same for
    two or more strings (and the state is not a final state?) then the language is infinite.
    """

    list_of_dicts = []
    push_diction = {}
    for state in range(state_num):
        i = 0
        while i < len(alphabet):
            push_diction[alphabet[i]] = trans_list[state][i]
            i = i + 1
        if push_diction:
            push_diction_copy = push_diction.copy()
            list_of_dicts.append(push_diction_copy)
            push_diction = {}
    print(list_of_dicts)
    print('\n')
    #Can any state reach the Final State?
    final_reachable = []
    # visited_states = []
    visit_states = []
    for state in range(state_num):
        visited_states = []
        visit_states.append(trace_final(state, alphabet, list_of_dicts, accepted_list, visited_states))
        print(f"Visit from state: {state} : {visit_states}")
        


def main():

    states = ''
    acc_states = ''
    alpha = ''
    transit = ''
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
    states = int(states.rsplit(':',1 )[1])
    acc_states = (acc_states.rsplit(':', 1)[1]).lstrip().rstrip()
    accept_list = acc_states.split(' ')
    alpha = (alpha.rsplit(':', 1)[1]).lstrip().rstrip()
    print(f"Number of states: {states}\nAccepting States: {accept_list}\n")
    print(f"alphabet: {alpha}")
    trans_list = []
    for line in transit.split('\n'):
        if line not in '' and line not in ' ':
            trans_list += [line.split(' ')]

    print(trans_list)
    properties(states, accept_list, alpha, trans_list)

if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        print("Please refer to the following for correct program arguments:")
        print(f"> {sys.argv[0]} 'DFA_description text file'")
        sys.exit()
    if os.path.exists("properties_dfa_log.txt"):
        os.remove("properties_dfa_log.txt")
    LOGF = open("properties_dfa_log.txt", "w")
    LOGF.write("PROPERTIES DFA LOGFILE\n\n")
    main()