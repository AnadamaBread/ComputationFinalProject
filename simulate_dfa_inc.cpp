#include <iostream>
#include <fstream>
#include <ostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <stdio.h>


using namespace std;

int main(int argc, char *argv[]){

    if(argc != 3) {
        cout << "Please input the dfa description and dfa input text files" << endl;
    }
   // vector <string>dfa_lines;
    string dfa_lines = "";

    ifstream dfafile(argv[1]);

    if(dfafile.is_open() && dfafile.good()){
        
        string line = "";
        while (getline(dfafile, line)) {
            // cout << line << endl;
            dfa_lines += line + '\n';
        }
    }
    stringstream ss (dfa_lines);
    // for (auto const &i : dfa_lines){
    //     cout << i << endl;
    // }




}