"""Simulate a DFA using the dfa description and input file.
Output a text file with accepting and rejecting, as well as
a log file."""

import sys
import os

def simulate(list_of_dict, accepts, input_list):
    """
    Simulate() does the actual simulation taking the completed list of
    transitions for each state reading each character: 'list_of_dict',
    and determining if the input strings are accepted by the transitions
    using the known accepting states. The integer variables "start_state" 
    and "go_to_state" are the index variables for the 'list_of_dict'.
    list_of_dict at the start_state reading the first letter of the
    first string goes to a "go_to_state". 

    Programming Logic: (Might need to remove this comment section eventually)
            # list_of_dict at start_state reading letter goes to X 
            # X = g̶o̶_̶t̶o̶_̶s̶t̶a̶t̶e̶ curr_state
            # list_of dict at curr_state reading letter goes to X 
            # repeat above till no letters
            # if curr_state == accept state
            # ansfile.write("ACCEPTS" in_string)
            # else ansfile.write("REJECTS" in )
    """
    # print(list_of_dict)
    # print(list_of_dict[0]['0'])
    # print(accepts)
    # print(input_list)

    if os.path.exists("simulate_dfa_output.txt"):
        os.remove("simulate_dfa_output.txt")

    ansfile = open("simulate_dfa_output.txt", "w")

    # start_state = 0
    #go_to_state = ""

    for in_string in input_list:
        curr_state = 0
        for letter in in_string:
            # print(curr_state)
            next_state = list_of_dict[curr_state][letter]
            curr_state = int(next_state)
        
        for elem in accepts:
            #print(int(elem))
            if int(elem) == curr_state:
                ansfile.write(f"ACCEPT {in_string} \n")
                break
        else:
            ansfile.write(f"REJECT {in_string} \n")
            








def makedict(trans, alph, scount):
    """
    This functions fills a list of dictionaries for the DFA
    simulation. Each index of the list will contain a
    dictionary for the state corresponding to the index.
    i.e list.at(1) = transitions for state 1.
    """
    # print(trans)
    the_dict_list = []
    ss_trans = {} # Empty dictionary for the transitions of each state
    for state in range(scount):
        i = 0
        # print(len(alph))
        while i < len(alph):
            # print(i)
            #print(f"At state {state} reading {alph[i]} go to {trans[state][i]}")
            ss_trans[alph[i]] = trans[state][i]
            # print(ss_trans)
            i = i + 1

        if ss_trans:
            ss_trans_copy = ss_trans.copy()
            the_dict_list.append(ss_trans_copy)
            ss_trans = {}

    #print(the_dict_list)

    return the_dict_list


def main():
    """
    main() reads the files, parses the information into usable formats,
    and calls on the various functions to do the simulation.
    """
    states = '' # number of states
    acc_states = '' # accepting states
    alpha = '' # alphabet
    transit = '' # transitions
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
    in_list = []
    with open(sys.argv[2]) as file_object_two:
        in_list = [line.rstrip() for line in file_object_two]
    # print(in_list)
    

    states = states.rsplit(':', 1)[1]
    # print(states)
    states = int(states)
    
    acc_states = (acc_states.rsplit(':', 1)[1]).lstrip().rstrip()
    acc_list = acc_states.split(' ')
    alpha = (alpha.rsplit(':', 1)[1]).lstrip().rstrip()
    
   # print(transit)
    #print(transit.split('\n'))
    tr_list = []
    for line in transit.split('\n'):
        if line != '' and line != ' ':
            tr_list += [line.split(' ')]

    # print(tr_list)

    # print("###########")
    # tr_list_list = [tr_list[x:x+states] for x in range(0, len(tr_list), states)]
    # print(tr_list_list)
    # # tr_list_new = []
    # # for x in range(0 , len(tr_list), states):
    # #     tr_list_new += [tr_list[x:x+states]]
    # # print(tr_list_new)
    # print("###########")
    # print(tr_list)
 
    # print(acc_list)
    # acc_states = int(acc_states)
    # print(acc_states)
 
    #print(alpha)
    the_dict_list = makedict(tr_list, alpha, states) # main list of dictionaries
   # print(the_dict_list) # LIST OF DICTIONARY TEST CORRECT FOR LARGE 
    simulate(the_dict_list, acc_list, in_list)
    #print(the_dict_list)
    


if __name__ == "__main__":
    if os.path.exists("simulate_dfa_log.txt"):
        os.remove("simulate_dfa_log.txt")
    logf = open("simulate_dfa_log.txt", "w")
    logf.write("SIMULATE DFA LOGFILE\n")
    main()
