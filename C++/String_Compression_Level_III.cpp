// Level 3 String compression Problem
// Interview question
// Author: Pavan Kumar Paluri

#include <iostream>
#include <string>
#include <vector>
#include <climits>

using namespace std;

int string_compressor(string& input_str)
{
  // read write problem 
  int write  =0;
  int allocate = 0;
  
  for(int read = 0; read < input_str.size(); read++)
  {
    if(read == input_str.size() || input_str[read] != input_str[read+1])
    {
    input_str[write] = input_str[allocate];
    write++;

    // replace chars with numbers 
    if(read > allocate)
    {
      for(char c: to_string(read-allocate+1)){
        input_str[write] = c;
        write++;
      }
    }
    allocate = read+1;
    }
  }

  if(input_str.size() != write)
      input_str.erase(write, input_str.size()-1);
  return input_str.size();
}

int string_parser(string& inpt_str, int parse_length)
{
  int res_size;
  string new_str = inpt_str;
  int shortest_res = INT_MAX;
  for(int i=0; i<new_str.size()-parse_length+1 && parse_length<new_str.size(); i++)
  {
    inpt_str.erase(i, parse_length);
    res_size = string_compressor(inpt_str);
    if(res_size < shortest_res)
    {
      shortest_res = res_size;
    }
    // reset to default now:
    inpt_str = new_str;
  }
  return shortest_res;
}
int main(){
   string str = "ABBBCCDDCCC";
  // string str = "ABCDDDEFG";
  int k = 3;
  int result;
  result = string_parser(str, k);
  cout << result << endl;
  return 0;
}
