"""
Program written by Luis Baez.
text_search.py takes input of a file containing a text string. Reading this string,
output a DFA description that accepts any string x if and only if the input string
is a substring of the string x.
The Alphabet will always and only be the 26 character lower case alphabet:
abcdefghijklmnopqrstuvwxyz
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

def maketextdfa(in_string, alphabet):
    """
    maketextdfa() creates the DFA description using brute force and ignorance.
    There will be the one more state than the length of the in_string. State 0
    will always be the start state and if states 0 through n-1 where n is the
    final state, read anything else but the next required character, will return
    to the start state. Once at the final state, the DFA will stay at the final state.
    """
    states_num = len(in_string) + 1
    accepting_state = [int(len(in_string))]
    tr_list = []
    push_define = {}
    for state in range(states_num):
        LOGF.write(f"STATE: {state}\n")
        for letter in alphabet:
            if int(state) in accepting_state:
                push_define[letter] = str(state)
                LOGF.write(f"IN ACCEPTING STATE: {letter} stays at {state}, \n")
            else:
                if letter in in_string[state]:
                    LOGF.write(f"{letter} is FOUND in {in_string},  ")
                    push_define[letter] = str(state+1)
                    LOGF.write(f"state {state} will go to state {state+1}!\n")
                else:
                    LOGF.write(f"{letter} goes to state 0,\n")
                    push_define[letter] = '0'
        if push_define:
            push_define_copy = push_define.copy()
            tr_list.append(push_define_copy)
            push_define = {}
        LOGF.write('\n')
    printnewdfa(states_num, accepting_state, alphabet, tr_list)

def main():
    """
    main() reads the text string contained in the input file and
    sets the alphabet variable. The function passes these as parameters
    to the maketextdfa() function.
    """
    in_string = ''
    with open(sys.argv[1]) as file_object:
        lines = file_object.readlines()
    for line in lines:
        in_string = line.rstrip()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    maketextdfa(in_string, alphabet)

if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        print("Please refer to the following for correct program arguments:")
        print(f"> {sys.argv[0]} 'text file containing input string'")
        sys.exit()
    if os.path.exists("text_search_dfa_log.txt"):
        os.remove("text_search_dfa_log.txt")
    LOGF = open("text_search_dfa_log.txt", "w")
    LOGF.write("TEXT SEARCH DFA LOGFILE\n\n")
    if os.path.exists("text_search_dfa_out.txt"):
        os.remove("text_search_dfa_out.txt")
    OUTF = open("text_search_dfa_out.txt", "w")
    OUTF.write("TEXT SEARCH DFA OUTPUT FILE\n\n")
    main()
