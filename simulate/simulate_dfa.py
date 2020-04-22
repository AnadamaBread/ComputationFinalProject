"""
Simulate a DFA using a DFA description and an input file.
Output (to standard out) the acceptance or rejection from
each input in the text file after being ran through the DFA
created by the DFA description
"""

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
    """
    if os.path.exists("simulate_dfa_output.txt"):
        os.remove("simulate_dfa_output.txt")
    ansfile = open("simulate_dfa_output.txt", "w")

    for in_string in input_list:
        LOGF.write(f"\nSIM: reading '{in_string}'\n")
        curr_state = 0
        for letter in in_string:
            #
            LOGF.write(f"IN STATE: {curr_state} READING: {letter} "
                       f"TRANSITIONS {list_of_dict[curr_state]}\n")
            next_state = list_of_dict[curr_state][letter]
            LOGF.write(f"IN STATE: {curr_state} READING: {letter} "
                       f"TRANSITIONS: {list_of_dict[curr_state]} CHANGING TO STATE {next_state}\n")
            curr_state = int(next_state)

        for elem in accepts:

            if int(elem) == curr_state:
                print(f"ACCEPT {in_string}")
                ansfile.write(f"ACCEPT {in_string} \n")
                LOGF.write(f"ACCEPT {in_string} \n")
                break
        else:
            print(f"REJECT {in_string}")
            ansfile.write(f"REJECT {in_string} \n")
            LOGF.write(f"REJECT {in_string} \n")

def makedict(trans, alph, scount):
    """
    makedict() fills a list of dictionaries for the DFA
    simulation. Each index of the list will contain a
    dictionary for the state corresponding to the index.
    i.e list.at(1) = transitions for state 1.
    """
    the_dict_list = []
    ss_trans = {}
    LOGF.write(f"\n#### TRANSITIONS ####\n")
    for state in range(scount):
        i = 0
        while i < len(alph):
            LOGF.write(f"SIM: At state {state} reading {alph[i]} go to {trans[state][i]}\n")
            ss_trans[alph[i]] = trans[state][i]
            i = i + 1
        if ss_trans:
            ss_trans_copy = ss_trans.copy()
            the_dict_list.append(ss_trans_copy)
            ss_trans = {}

    return the_dict_list

def main():
    """
    main() reads the files and parses the information into usable formats.
    The number of states is parsed into an integer, the alphabet into a string
    format variable "alpha", the accepted states and transitions are parsed into
    two separate lists. The transitions is further broken down into a list of lists.
    A dictionary is made with the 'makedict()' function and is used as a parameter
    for the actual simulation.
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


    states = states.rsplit(':', 1)[1]
    states = int(states)

    acc_states = (acc_states.rsplit(':', 1)[1]).lstrip().rstrip()
    acc_list = acc_states.split(' ')
    alpha = (alpha.rsplit(':', 1)[1]).lstrip().rstrip()

    tr_list = []
    for line in transit.split('\n'):
        if line not in '' and line not in ' ':
            tr_list += [line.split(' ')]


    LOGF.write(f"SIM: NUMBER OF STATES: {states}\n")
    LOGF.write(f"SIM: ACCEPTING STATES: {acc_states} \n")
    LOGF.write(f"SIM: ALPHABET: {alpha}\n")

    the_dict_list = makedict(tr_list, alpha, states)
    simulate(the_dict_list, acc_list, in_list)

if __name__ == "__main__":
    if len(sys.argv[1:]) != 2:
        print("Please refer to the following for correct program arguments:")
        print(f"> {sys.argv[0]} 'DFA_description text file' 'DFA_input text file'")
        sys.exit()
    if os.path.exists("simulate_dfa_log.txt"):
        os.remove("simulate_dfa_log.txt")
    LOGF = open("simulate_dfa_log.txt", "w")
    LOGF.write("SIMULATE DFA LOGFILE\n\n")
    print("Simulate Log and Output Files created!")
    main()
