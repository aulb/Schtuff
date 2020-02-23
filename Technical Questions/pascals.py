#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1

# f(4) = [1, 3, 3, 1]

# f(m) [...m elements]

from collections import deque
def get_n_pascal_row(n):
  if n < 1: return []
  
  previous_result = deque([1])
  counter = 1
  
  while counter < n:
    previous_result.appendleft(0)
    previous_result.append(0)
    
    current_result = deque([])
    
    for i in range(len(previous_result) - 1):
      current_result.append(previous_result[i] + previous_result[i + 1])
      
    previous_result = current_result
    counter += 1
    
  return previous_result

if __name__ == '__main__':
  print(list(get_n_pascal_row(4)))
  assert get_n_pascal_row(4) == [1,3,3,1]
