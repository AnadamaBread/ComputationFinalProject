"""Simulate a DFA using the dfa description and input file.
Output a text file with accepting and rejecting, as well as
a log file."""

import sys

def simulate(list_of_dict, accepts, input_list):
    """
    Simulate() does the actual simulation taking the completed list of
    transitions for each state reading each character: 'list_of_dict',
    and determining if the input strings are accepted by the transitions
    using the known accepting states
    """
    


def makedict(trans, alph, scount):
    """
    This functions fills a list of dictionaries for the DFA
    simulation. Each index of the list will contain a
    dictionary for the state corresponding to the index.
    i.e list.at(1) = transitions for state 1.
    """
    the_dict_list = []
    ss_trans = {} # Empty dictionary for the transitions of each state
    for state in range(scount):
        i = 0
        while i < len(alph):
            # print(f"At state {state} reading {alph[i]} go to {tr[state][i]}")
            ss_trans[alph[i]] = trans[state][i]
            #print(ss_trans)
            i = i + 1

        if ss_trans:
            ss_trans_copy = ss_trans.copy()
            the_dict_list.append(ss_trans_copy)
            ss_trans = {}

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
    print(in_list)
    tr_list = []
    for line in transit.split('\n'):
        if line != '':
            tr_list += [line.replace(" ", "")]
    states = states.rsplit(':', 1)[1]
    print(states)
    states = int(states)
    acc_states = acc_states.rsplit(':', 1)[1]
    # acc_states = int(acc_states)
    print(acc_states)
    alpha = (alpha.rsplit(':', 1)[1]).lstrip().rstrip()
    the_dict_list = makedict(tr_list, alpha, states) # main list of dictionaries
    # simulate(the_dict_list, acc_states, in_list)
    print(the_dict_list)


if __name__ == "__main__":
    main()
