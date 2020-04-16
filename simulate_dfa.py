import sys
###############################################################
# makedict(alphabet, number of states):
#
#   This functions fills a list of dictionaries for the DFA 
#     simulation. Each index of the list will contain a 
#     dictionary for the state corresponding to the index. 
#     i.e list.at(1) = transitions for state 1. 
#
#
###############################################################

def makedict(tr,a,s):

    global the_dict_list
    if 'the_dict' not in globals():
        the_dict_list = [] 
    
    ss_trans = {} # Empty dictionary for the transitions of each state
    for x in range(0, s):
        i = 0
        j = 0
        while i < len(a) + 1:
            j = i
            if tr[j] == ' ':
                # continue
                j = j + 1
            if tr[j] == '\n':
                break
            if tr[j] != ' ' and tr[j] != '\n':
                print(f"At state {x} reading {a[i]} go to {tr[j]}")
            i = i + 1

    # x = 0
    # while x < s:
    #     i = 0
    #     while i < len(a) + 1:
    #         for elem in tr:
    #             if elem != ' ' and elem != '\n':
    #                 print(f"At state {x} reading {a[i]} go to {elem}")
    #             if elem == ' ': 
    #             # Logic here : the # of spaces in transitions of description will never exceed # of characters in the alphabet
    #                 # print(f"At state {x} reading {a[i+1]} go to {elem}")
    #                 continue
    #             if elem == '\n':
    #                 break
    #         else:
    #             # i += 1
    #             continue
               
    #         break
            
    #     else:
    #         x += 1
    #         continue
            
    #     break

    # print(f"Transitions of state:{x} is {ss_trans[x]} ")
        
    




def main():
    _states ='' # number of states
    acc_states ='' # accepting states
    alpha ='' # alphabet
    tr='' # transitions
    with open(sys.argv[1]) as file_object:
        lines = file_object.readlines()
    for line in lines:
        if _states == '':
            _states = line
        elif acc_states == '':
            acc_states = line
        elif alpha == '':
            alpha = line

        else:
            tr = tr + line.rstrip() + '\n'
    
    _states = _states.rsplit(':',1)[1]
    _states = int(_states)
    acc_states = acc_states.rsplit(':',1)[1]
    acc_states = int(acc_states)
    
    alpha = (alpha.rsplit(':',1)[1]).lstrip()
    
    # print(_states)
    # print(acc_states)
    # print(alpha)
    # print(tr)
    makedict(tr,alpha, _states)


if __name__ == "__main__":
    main()


