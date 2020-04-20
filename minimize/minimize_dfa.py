"""
Minimize a DFA given a description of a DFA. Output
to standard out using the table-of-distinguishable-states
to minimize. Ordering of states may differ compared to output.
"""
#
#
import sys
import os
#
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

def minimize_out(state_num, accepted_list, alphabet, list_of_dict, indistinguishable):
    """
    minimize_out() creates a new number of states using orignal state number minus
    indistinguishables pairs taking into account three or more pair combinations
    of states. Then states with the same transistion after reading any character
    from the alphabet will become a single state. State combinations with three or more
    states will be merged and overwritten with the transistions the occures the most per 
    those states. The number detucted from the original state count will be deducted from 
    each element in the accepted states and each element in the transisions. 
    """
    
    indist_scount = 0
    print(indistinguishable)
    for elem in indistinguishable:
        pass


#
def chartprint(chart_list):
    """
    chartprint() is custom 'poor mans' formatting of a 2D list into a matrix
    for either standard out or the log file.
    """
    i = 0
    j = 0
    print("    ", end="")
    for row in chart_list:
        print(j, end="    ")
        j = j + 1
    print("\n", end="")
    for row in chart_list:
        print(f"{i} {row}")
        i = i + 1
    print('\n')
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
    a single character from the alphabet. If reading the character transistions
    either (not both) states into a final state then that pair is distinguishable.
    """
    #
    indistinguishable = []
    #
    for state_one in range(state_num):
    #
        for state_two in range(state_num):
            if state_one != state_two:
            #
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
            #
    #
    i = 0
    while i < state_num:
        j = 0
        while j < state_num:
            if chart_list[i][j] == '_' and chart_list[j][i] == '_' and i != j:
                if str(i) not in accepted_list and str(j) not in accepted_list:
                    indistinguishable.append([i, j])
            j = j +1
        i = i + 1
    #
    result = []
    for elem in indistinguishable:
        if elem not in result and elem.reverse() not in result:
            result.append(elem)
            LOGF.write(f"INDISTINGUISHABLE: {elem}\n")
    if result:
        minimize_out(state_num, accepted_list, alphabet, list_of_dict, result)

    #
    # for elem in result:
    #     LOGF.write(f"INDISTINGUISHABLE: {elem}\n")
#
#

def makeminchart(state_num, accepted_list, alphabet, tran_list):
    """
    makeminchart() makes the '2D array' for the minimization algorithm.
    Such as Array[states][states], filling at first with blanks or '.'
    then distinguishing final states. This function also creates a
    list of dictinaries for transistions at each state.
    """
    print('\n')
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
    # print(list_of_dict)
    chart_list = [['_'] * state_num for state in range(state_num)]
    chartprint(chart_list)
    # print(chart_list)
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
    #
    chartprint(chart_list)
    #
    minimize(state_num, accepted_list, alphabet, list_of_dict, chart_list)
#
#
#

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
    #
    states = int(states.rsplit(":", 1)[1])
    acc_states = (acc_states.rsplit(':', 1)[1]).lstrip().rstrip()
    acc_list = acc_states.split(' ')
    alpha = (alpha.rsplit(':', 1)[1]).lstrip().rstrip()
    #
    print(f"Number of states: {states}\nAccepting States: {acc_list}\n")
    print(f"alphabet: {alpha}")
    LOGF.write(f"MIN: NUMBER OF STATES: {states}\n")
    LOGF.write(f"MIN: ACCEPTING STATES: {acc_states}\n")
    LOGF.write(f"MIN: ALPHABET: {alpha}\n")
    tr_list = []
    for line in transit.split('\n'):
        if line not in '' and line not in ' ':
            tr_list += [line.split(' ')]
    #
    print(tr_list)
    makeminchart(states, acc_list, alpha, tr_list)
#
#
#
if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        print("Please refer to the following for correct program arguments:")
        print(f"> {sys.argv[0]} 'DFA_description text file'")
        sys.exit()
    if os.path.exists("minimize_dfa_log.txt"):
        os.remove("minimize_dfa_log.txt")
    LOGF = open("minimize_dfa_log.txt", "w")
    LOGF.write("MINIMIZE DFA LOGFILE\n\n")
    main()
