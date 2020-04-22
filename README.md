# README For CSCE_355 Programming Assignment

__Completed Programs:__ Simulating a DFA, Minimizing a DFA, Text Search

__Synopsis:__

 Each program is written in Python 3 (Python 3.7.5). Each program will output to both standard out as well as 
 a created output file. Each program will also create and log to a log file. The format of these files would look like so:
 "simulate_dfa_log.txt" or "simulate_dfa_out.txt"

__pylint information:__  
pylint --version  

pylint 2.4.4  
astroid 2.3.3  
Python 3.7.5 (default, Nov 20 2019, 09:21:52)  
[GCC 9.2.1 20191008]  

## DFA Simulation Python3 Program

Program Description:
    This program takes input of a DFA description and a text file of strings for the DFA to read. 
    The program will output to BOTH standard out and an output file each input string and if it accepts or 
    rejects the string. The program will also create a log file for readable loop tracing throughout
    the simulation.

Execution:
    To execute the python 3 program, run the executable bash script along with the arguments like so:  
    ```
    ./simulator.txt 'dfa_description.txt' 'input_strings.txt'
    ```

pylint OUTPUT:

------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00


## DFA Minimization Python3 Program 

Program Description:

Execution:
    To execute the python 3 program, run the executable bash script (within the 'minimize' directory) along with 
    the arguments like so:  
    ```
     ./minimizer.txt 'dfa_description.txt'
    ```

pylint OUTPUT:

************* Module minimize_dfa
minimize_dfa.py:52:0: R0912: Too many branches (13/12) (too-many-branches)
minimize_dfa.py:122:0: R0912: Too many branches (14/12) (too-many-branches)

-------------------------------------------------------------------
Your code has been rated at 9.90/10 (previous run: 10.00/10, -0.10)

## Text Search  Python3 Program

Program Description:  

Execution:  

pylint OUTPUT:  

