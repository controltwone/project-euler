with open("triangle.txt", "r") as f:
  data = f.read()
  

triangle = [[int(word) for word in line.split()]for line in data.strip().split("\n")]

# print(triangle)




# def solution_from_botton_to_top():
  
#   for row in reversed(range(len(triangle)-1)):
#     row_ = triangle[row]
    
#     for col in range(len(row_)):
#       row_[col] += max(triangle[row+1][col], triangle[row+1][col+1]) 
      
#   return triangle[0][0]

# print(solution_from_botton_to_top())


def solution_from_botton_to_top():
  
  for row in reversed(range(len(triangle)-1)):
   
    
    for col in range(row+1):
      triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1]) 
      
  return triangle[0][0]

print(solution_from_botton_to_top())

