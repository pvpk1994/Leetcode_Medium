'''
Coding Interview Question 

Problem Description:
-------------------
Given a positive integer N, find its maximal unique odd decomposition.
For example: All decompositions of 11
11 {1+2+3+5, 1+2+8, 1+3+7, 1+4+6, 1+10, 2+3+6, 2+4+5, 2+9, 3+8, 4+7, 5+6, 11}
Of all the above combinations, the function should return the unique maximal odd decompositon of 11 i.e., {1,3,7}

#Developed by Pavan Kumar Paluri

Solution:
'''
def max_decomposition(num: int)->list:
  summ = 0
  output_list =[]
  # odd max_decomposition
  if num ==1:
    return [1]
  for i in range(1, num, 2):
    # increment by 2 to make sure, it is always odd
    summ += i
    if summ <= num:
      output_list.append(i)
    elif summ > num:
      summ = summ - i
      break
  # print(output_list)
  # cal remaining
  # print(summ)
  remaining = num-summ
  if remaining%2 ==0:
    output_list[len(output_list)-1] += remaining
  elif remaining <= output_list[len(output_list)-1]:
    output_list[len(output_list)-1] += remaining+1
    output_list.pop(0)
  elif remaining > output_list[len(output_list)-1]:
    output_list.append(remaining)
    
  return output_list
  


if __name__ == "__main__":
  print(max_decomposition(7))
