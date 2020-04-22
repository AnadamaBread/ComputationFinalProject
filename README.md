# README For CSCE_355 Programming Assignment  
Programmed and Documented by Luis Baez

__Completed Programs:__ Simulating a DFA, Minimizing a DFA, Text Search

__Other Programs:__ Complement of a DFA

__Synopsis:__  
 Each program is written in Python 3 (Python 3.7.5) and is housed in it's own subdirectory within this directory. For Example, the program for simulating a DFA is inside the directory 'simulate'. Each completed program will output to both standard out as well as a created output file. Each completed program will also create and log to a log file. The format of these files would look like so:
 "simulate_dfa_log.txt" or "simulate_dfa_out.txt". The completed programs include: simulating a DFA, minimizing a DFA, and text search. The other included program is complement of a DFA, without intersection. (See more under "DFA Complement Python3 Program"). 

 __Usage:__  
 Under each program section within this readme there is a sub-section titled "Execution". 
 This will have one or two ways on how to launch the programs. I recommend changing into the sub-directory of the program you wish to execute, this README is written in anticipation for said method. Each "Execution" will include examples of how to use arguments with the programs, there are also files in this directory titled "DFA01.txt" DFA02.txt" and "DFA0L.txt", these are DFA Description files that you are welcome to use to test the programs. There are input files for simulate and text search within their respected directories. To USE these DFA Description test files as arguments navigate into the directory of the program you want to test with and use '../' to use a file in the previous directory. For example to run simulate on one of the supplied DFA Descriptions and the supplied input text file(in the "simulate" directory):

    ./simulator.txt ../DFA01.txt someinput.txt
OR  

    python3 simulate_dfa.py ../DFA01.txt someinput.txt

The text search program also has a file for a single string input named "searchthing.txt" within it's program's directory. (See "Text Search Python3 Program" for more details) 

__bash scripts:__  
The build/run files for these python3 programs are in the form of bash scripts for unix. Since python doesn't utilize any building commands for compilation, bash scripts were made to ensure thorough execution of the python programs. Each program has its own executable text file within it's directory that runs the python command (python3), the python3 program itself, and any arguments you give it("$@").  

__pylint information:__  
pylint --version  

pylint 2.4.4  
astroid 2.3.3  
Python 3.7.5 (default, Nov 20 2019, 09:21:52)  
[GCC 9.2.1 20191008]  

## DFA Simulation Python3 Program
### Sub-Directory: "simulate"
### Program Description:  
This program takes input of a DFA description and a text file of strings for the DFA to read. The program will output to BOTH standard out and an output file each input string and if it accepts or rejects the string. The program will also create a log file for readable loop tracing throughout the simulation.

### Execution:  
To execute the python3 program, run the executable bash script (within the 'simulate' directory) along the arguments like so (without single quotes '' ):  
    
    ./simulator.txt 'dfa_description.txt' 'input_strings.txt'

OR, Using python3 command (without single quotes '' ):

    python3 simulate_dfa.py 'dfa_description.txt' 'input_strings.txt'


    

### pylint OUTPUT:
  
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00

  
## DFA Minimization Python3 Program 
### Sub-Directory: "minimize"
### Program Description:
This program takes input of a single DFA description text file. The program
    will output to BOTH standard out and an output file any indistinguishable state pairs, if the DFA is minimized or not, and then a description of the minimized DFA if the DFA is not already minimized. THe program will also create a log file where a table-of-distinguishable state pairs is drawn and edited for each iteration of reading the DFA description. 

### Execution:
To execute the python3 program, run the executable bash script (within the 'minimize' directory) along with the arguments like so (without single quotes '' ):  
    
     ./minimizer.txt 'dfa_description.txt'

OR, Using python3 command (without single quotes '' ):

    python3 minimize_dfa.py 'dfa_description.txt'
    

### pylint OUTPUT:

************* Module minimize_dfa  
minimize_dfa.py:52:0: R0912: Too many branches (13/12) (too-many-branches)  
minimize_dfa.py:122:0: R0912: Too many branches (14/12) (too-many-branches)  
  
Your code has been rated at 9.90/10 (previous run: 10.00/10, -0.10)

## Text Search Python3 Program
### Sub-Directory: "text_search"
### Program Description:  
The program takes a single input of a text file containing a string in which a DFA will be built. Said DFA will accept any string were the input string is a substring of that string. The program will output to BOTH standard out and an output file the description of a DFA. The program will also create a log file for readable loop tracing.  
       
### Execution:  
To execute the python3 program, run the executable bash script (within the text_search directory) along with the arguments like so (without single quotes '' ):

    ./searcher.txt 'input_string.txt'

OR, Using python3 command (without single quotes '' ):

    python3 text_search.py 'input_string.txt'

Within this programs directory there is a text file called "searchthing.txt" which contains a single string used to test this program. Feel free to use it with the examples above. 

### pylint OUTPUT:  
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

## DFA Complement Python3 Program 
__(No Intersection)__
### Sub-Directory: "complement"

### Program Description:
This program will take in a DFA description text file as input and output the DFA description of its complement. The output will ONLY go to standard out and there will be no log file.

### Execution:
To execute this python3 program, run the executable bash script (within the complement directory) along with the arguments like so (without single quotes ''):  

    ./complimenter.txt 'dfa_description.txt'

OR, Using python3 command (without single quotes '' ):

    python3 complement.py 'dfa_description.txt'

### pylint OUTPUT:  
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)