"""
text_search.py takes input of a file containing a text string. Reading this string, 
output a DFA description that accepts any string x if and only if the input string
is a substring of the string x. 
The Alphabet will always and only be the 26 character lower case alphabet:
abcdefghijklmnopqrstuvwxyz
"""
import sys
import os

def main():






if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        print("Please refer to the following for correct program arguments:")
        print(f"> {sys.argv[0]} 'text file containing input string'")
        sys.exit()
    main()