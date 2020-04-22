"""
Minimize a DFA given a description of a DFA. Output
to standard out using the table-of-distinguishable-states
to minimize. Ordering of states may differ compared to output.
"""


import sys
import os


def printnewdfa(state_count, accepted, alphabet, t_list_d):
    """
    printnewdfa() prints out a dfa description formatted as
    required. Exactly the same as the input dfa descriptions.
    The description is printed to standard output.
    """
    print(f"Number of states: {state_count}")
    print(f"Accepting states:", end=' ')
    OUTF.write(f"Number of states: {state_count}\n")
    OUTF.write(f"Accepting states: ")
    for elem in accepted:
        if elem == accepted[-1]:
            print(f"{elem}", end='')
            OUTF.write(f"{elem}")
        else:
            print(f"{elem}", end=' ')
            OUTF.write(f"{elem} ")
    print()
    OUTF.write('\n')
    print("Alphabet:", end=' ')
    OUTF.write("Alphabet: ")
    for elem in alphabet:
        print(f"{elem}", end="")
        OUTF.write(f"{elem}")
    print()
    OUTF.write('\n')
    for state in range(state_count):
        i = 0
        while i < len(alphabet):
            if i+1 == len(alphabet):
                print(f"{t_list_d[state][alphabet[i]]}", end="")
                OUTF.write(f"{t_list_d[state][alphabet[i]]}")

            else:
                print(f"{t_list_d[state][alphabet[i]]}", end=" ")
                OUTF.write(f"{t_list_d[state][alphabet[i]]} ")
            i = i + 1
        print()
        OUTF.write('\n')

def minimize_out(state_num, accepted_list, alphabet, list_of_dict, indistinguishable):
    """
    minimize_out() creates a new number of states using original state number minus
    indistinguishable pairs taking into account three or more pair combinations
    of states. Then states with the same transition after reading any character
    from the alphabet will become a single state. State combinations with three or more
    states will be merged and overwritten with the transitions the occurs the most per
    those states. The number deducted from the original state count will be deducted from
    each element in the accepted states and each element in the transisions.
    """
    indist_scount = 0
    list_of_states = []
    push_accepting = []
    convert_indist = {elem[0]:elem[1] for elem in indistinguishable}
    indist_scount = state_num - len(convert_indist)
    for state in range(state_num):
        if state in convert_indist:
            list_of_dict[state] = list_of_dict[convert_indist[state]]
    visited = []
    for state in range(state_num):
        if str(state) not in accepted_list:
            if list_of_dict[state] not in visited:
                list_of_states.append(list_of_dict[state])
                LOGF.write(f"NEW: Transitions at state {state} : {list_of_dict[state]}\n")
                visited.append(list_of_dict[state])
            else:
                LOGF.write(f"Transitions at state {state} : {list_of_dict[state]}\n")
        else:
            list_of_states.append(list_of_dict[state])
            LOGF.write(f"ACCEPTING STATES: ")
            LOGF.write(f"Transitions at state {state} : {list_of_dict[state]}\n")

    LOGF.write(f"\nNew State Transitions:\n")
    for state in range(indist_scount):
        for elem in alphabet:
            value = int(list_of_states[state].get(elem))
            if value >= len(convert_indist):
                value = value - len(convert_indist)
            list_of_states[state][elem] = value
        LOGF.write(f"Transitions at state {state} : {list_of_states[state]}\n")

    for elem in accepted_list:
        if int(elem) >= len(convert_indist):
            new_elem = int(elem) - len(convert_indist)
            LOGF.write(f"NEW ACCEPTING STATE: {new_elem}\n")
            push_accepting.append(str(new_elem))
        else:
            push_accepting.append(elem)
    printnewdfa(indist_scount, push_accepting, alphabet, list_of_states)

def chartprint(chart_list):
    """
    chartprint() is custom 'poor mans' formatting of a 2D list into a matrix
    for either standard out or the log file.
    """
    i = 0
    j = 0
    LOGF.write("    ")
    for row in chart_list:
        LOGF.write(f"{str(j)}    ")
        j = j + 1
    LOGF.write("\n")
    for row in chart_list:
        LOGF.write(f"{i} {row}\n")
        i = i + 1
    LOGF.write("\n")

def minimize(state_num, accepted_list, alphabet, list_of_dict, chart_list):
    """
    minimize() utilizes the table-of-distinguishable-states method to successfully
    minimize a dfa. The algorithm takes a pair of states p and q where p != q, reads
    a single character from the alphabet. If reading the character transitions
    either (not both) states into a final state then that pair is distinguishable.
    """

    indistinguishable = []

    for state_one in range(state_num):
        for state_two in range(state_num):
            if state_one != state_two:
                for elem in alphabet:
                    LOGF.write(f"TEST : [{state_one}, {state_two}]  ")
                    LOGF.write(f"WITH {elem}  ")
                    next_one = list_of_dict[state_one][elem]
                    next_two = list_of_dict[state_two][elem]
                    LOGF.write(f" {state_one} --> {next_one}  ")
                    LOGF.write(f" {state_two} --> {next_two}\n")
                    if str(next_one) in accepted_list and str(next_two) not in accepted_list:
                        LOGF.write(f"FLAG : [{state_one}, {state_two}] WITH {elem}   "
                                   f"{state_one} --> {next_one}   "
                                   f"{state_two} --> {next_two}\n\n")
                        chart_list[state_one][state_two] = 'X'
                        chart_list[state_two][state_one] = 'X'
                        chartprint(chart_list)
                    if str(next_one) not in accepted_list and str(next_two) in accepted_list:
                        LOGF.write(f"FLAG : [{state_one}, {state_two}] WITH {elem}   "
                                   f"{state_one} --> {next_one}   "
                                   f"{state_two} --> {next_two}\n\n")
                        chart_list[state_one][state_two] = 'X'
                        chart_list[state_two][state_one] = 'X'
                        chartprint(chart_list)

    i = 0
    while i < state_num:
        j = 0
        while j < state_num:
            if chart_list[i][j] == '_' and chart_list[j][i] == '_' and i != j:
                if str(i) not in accepted_list and str(j) not in accepted_list:
                    indistinguishable.append([i, j])
            j = j +1
        i = i + 1

    result = []
    for elem in indistinguishable:
        if elem not in result and elem.reverse() not in result:
            result.append(elem)
            LOGF.write(f"INDISTINGUISHABLE: {elem}\n")
            print(f"INDISTINGUISHABLE: {elem}")
    if result:
        LOGF.write(f"INPUT DFA IS NOT MINIMIZED\n\n")
        print("\nINPUT DFA IS NOT MINIMIZED\n")
        print("NEW MINIMIZED DFA:")
        minimize_out(state_num, accepted_list, alphabet, list_of_dict, result)
    else:
        LOGF.write(f"INPUT DFA IS ALREADY MINIMIZED\n\n")
        print(f"INPUT DFA IS MINIMIZED DFA")

def makeminchart(state_num, accepted_list, alphabet, tran_list):
    """
    makeminchart() makes the '2D array' for the minimization algorithm.
    Such as Array[states][states], filling at first with blanks or '.'
    then distinguishing final states. This function also creates a
    list of dictionaries for transitions at each state.
    """
    list_of_dict = []
    push_dict = {}
    for state in range(state_num):
        i = 0
        LOGF.write("MIN: ")
        while i < len(alphabet):
            LOGF.write(f"At {state} reading {alphabet[i]} -> {tran_list[state][i]}  ")
            push_dict[alphabet[i]] = tran_list[state][i]
            i = i + 1
        LOGF.write('\n')
        if push_dict:
            push_dict_copy = push_dict.copy()
            list_of_dict.append(push_dict_copy)
            push_dict = {}

    chart_list = [['_'] * state_num for state in range(state_num)]
    chartprint(chart_list)

    i = 0
    while i < state_num:
        j = 0
        while j < state_num:
            if str(i) in accepted_list and str(j) not in accepted_list:
                chart_list[i][j] = 'X'
                chart_list[j][i] = 'X'
            if str(j) in accepted_list and str(i) not in accepted_list:
                chart_list[i][j] = 'X'
                chart_list[j][i] = 'X'
            j = j + 1
        i = i + 1

    chartprint(chart_list)

    minimize(state_num, accepted_list, alphabet, list_of_dict, chart_list)

def main():
    """
    main() reads the files, parses the information into usable formats,
    and calls on one function to start the minimization.
    """
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

    states = int(states.rsplit(":", 1)[1])
    acc_states = (acc_states.rsplit(':', 1)[1]).lstrip().rstrip()
    acc_list = acc_states.split(' ')
    alpha = (alpha.rsplit(':', 1)[1]).lstrip().rstrip()

    LOGF.write(f"MIN: NUMBER OF STATES: {states}\n")
    LOGF.write(f"MIN: ACCEPTING STATES: {acc_states}\n")
    LOGF.write(f"MIN: ALPHABET: {alpha}\n")
    tr_list = []
    for line in transit.split('\n'):
        if line not in '' and line not in ' ':
            tr_list += [line.split(' ')]

    makeminchart(states, acc_list, alpha, tr_list)

if __name__ == "__main__":
    # os.system('./minimize.txt')
    if len(sys.argv[1:]) != 1:
        print("Please refer to the following for correct program arguments:")
        print(f"> {sys.argv[0]} 'DFA_description text file'")
        sys.exit()
    if os.path.exists("minimize_dfa_log.txt"):
        os.remove("minimize_dfa_log.txt")
    LOGF = open("minimize_dfa_log.txt", "w")
    print("Minimize logfile and outputfile created!", end='\n''\n')
    LOGF.write("MINIMIZE DFA LOGFILE\n\n")
    if os.path.exists("minimize_dfa_out.txt"):
        os.remove("minimize_dfa_out.txt")
    OUTF = open("minimize_dfa_out.txt", "w")
    OUTF.write("MINIMIZE DFA OUTPUT\n\n")
    main()
