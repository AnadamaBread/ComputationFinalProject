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
def main():
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


if __name__ == "__main__":
    main()