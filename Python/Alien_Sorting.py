# Author: Pavan Kumar Paluri
# Alien Sorting 
list_text = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]
input_list = ["dd r",  "n a h", "d e a", "dd", "ng a h"]
# Sort the input_list based on list_text
def func(st):
  list_str = st.split(" ")

  list_ret= []
  for character in list_str:
    if character in list_text:
      list_ret.append(list_text.index(character))
  print("str:"+st)
  print("list:"+str(list_ret))
  return list_ret 

input_list = sorted(input_list, key=func)
print(input_list)
