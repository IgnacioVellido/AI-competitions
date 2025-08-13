# # Commander Lambda
# # Level 1 - Challenge 1

# def solution(x, y):
#     """Given two almost identical list return extra element.
#     Looking for efficiency, so there must be no sorting.
#     List contains integers, always one extra element
#     No need to check for empty lists
#     """
#     # Identify list with additional element
#     (longest, shortest) = (x,y) if len(x) > len(y) else (y,x)
    
#     # For element 'e' in shortest list
#     for e in shortest:
#         # Drop element 'e' in longest list
#         # As they are integers, there won't be precision errors
#         longest.remove(e)
    
#     # Remaining element is the solution
#     assert len(longest) == 1
    
#     return longest[0]

# x = [13,5,6,2,5]
# y = [5,2,5,13]
# print(solution(x,y))
# # assert solution(x,y) == 6

# x = [14,27,1,4,2,50,3,1]
# y = [2,4,-4,3,1,1,14,27,50]
# # assert solution(x,y) == -4
# print(solution(x,y))


# # Level 2 - Challenge 1

# # Const: Python 2.7, standard libraries, under 32000 characters

# def solution(src, dst):
#     """Assuming 8x8 chess-like board, give the minimum number
#     of steps from tile src to tile dst using knight L movements.
#     No need to check src/dst value.
    
#     It's the same as shortest distance in a graph, only in this
#     case the topology is different from the numbering. Solution
#     can be seen as moving through a tree like structure keeping
#     track of the depth level.
#     """
#     def to_row_col(node):
#         return node//8, node%8
    
#     def to_id(row,col):
#         return row*8 + col
        
#     def in_bounds(row,col):
#         return row >= 0 and row <8 and col >= 0 and col <8
    
#     def neighbors(node):
#         """Returns adjacent squares"""
#         # Available distances
#         distances = [
#             (2,1),
#             (2,-1),
#             (-2,1),
#             (-2,-1),
            
#             (1,2),
#             (-1,2),
#             (1,-2),
#             (-1,-2)
#         ]
            
#         row,col = to_row_col(node)
#         neighbors = []
        
#         # Calculate neighbors
#         for r,c in distances:
#             new_row = row + r
#             new_col = col + c
            
#             # Remove nodes out of bounds
#             if in_bounds(new_row, new_col):
#                 neighbors.append(to_id(new_row,new_col))
            
#         return neighbors
        
#     neigh = [src] # List of neighbors at current level
#     found = False
#     dist = 0
    
#     # Loop through neighbors until found
#     while not found:
#         if dst in neigh:
#             found = True
#         else:
#             # Not found, go one level down
#             dist += 1
            
#             # Get nodes at next depth
#             new_neigh = []
#             for node in neigh:
#                 new_neigh.extend(neighbors(node))
#             neigh = new_neigh
            
#     return dist

# print("--------")
# print(solution(0,1))
# print(solution(19,36))
# print(solution(0,63))
# print(solution(56,63)) # 5

# # [(2,1),(1,2)]
# # [+1,-1]

# # +2,+1 = 17
# # +2,-1 = 15
# # -2,+1 = -15
# # -2,-1 = 17

# # +1,+2 = 10
# # +1,-2 = 6
# # -1,+2 = -6
# # -1,-2 = 10


# # ------------------------------------
# # Level 2 - Challenge 2

# def solution(n, b):
#     """Find the length of the ending cycle for the given
#     algorithmn, that is, the number of elements that the
#     algorithm loops over.
    
#     Solution can be see as implementing the algorithm and
#     iterate while keepin track of past solutions. When an
#     id has already been generated, find the length of the
#     loop
#     """
#     def to_base_b(n,b):
#         """Get n as string in base b"""
#         if n == 0:
#             return 0
        
#         sol = ""
#         while n>0:
#             sol = str(n%b) + sol
#             n = n // b
        
#         return sol
    
#     # Define list of generated ids
#     ids = [n]
    
#     k = len(n) # n is a string, so we can get its length
    
#     # Loop
#     loop_found = False
#     current_id = n
#     while not loop_found:
#         # Define x and y as integers of length k
        
#         # Get digits of current_id as list
#         # (Can't use .copy() in Python 2.7)
#         x = [str(d) for d in current_id]
#         y = [str(d) for d in current_id]
        
#         # Sort
#         x.sort()
#         y.sort(reverse=True)
        
#         # Get back as strings
#         x = "".join(x)
#         y = "".join(y)
        
#         # Transform to base 10
#         x = int(x, base=b)
#         y = int(y, base=b)
        
#         # Define z
#         z = abs(x - y) # Non-negative
#         z = str(to_base_b(z,b))
        
#         # Pad z if necessary
#         pad = k - len(z)
#         z = '0'*pad + z
        
#         # Check if already in list
#         if z in ids:
#             loop_found = True
#         else: # Append and loop
#             ids.append(z)
#             current_id = z
        
#     # Loop found, get distance as the difference between
#     # the length of the list and the index of the element
#     dist = len(ids) - ids.index(z)
    
#     return dist



# print("--------")
# # a = "320"
# # a.sort()
# # a.sort(reverse=True)
# # print(a)
# print(solution('1211',10))
# print(solution('210022',3))

# # 210022 - 220012
# # -  (220012 - 210022)

# # - (2220)


# # n = "210022"
# # print(int(n[::-1]))
# # print("a"*0 + n)

# # x = [0,2,3,4]
# # x.

# # Refer code 
# # https://foobar.withgoogle.com/?eid=rc38l

# # THE smaller number indicate from which branch (m or f) is the parent
# # 5,4

# # (?,5) (9,?)
# # (4,5)

# # 9,5


# # (113,?) - NO
# # (?,55) - SI
# # 113, 55


# def solution(m, f):
#     """m and f are ints as strings. Process:
#     0. m=1 and f=1
#     1a. for each m -> + one f
#     1b. for each f -> + one m
#     2. Repeat until objective achieved
    
#     return number of cycles in the process
    
#     The solution can be seen as exploring 
#     a binary tree width-wise until finding the objective node,
#     returning the depth of the first solution
#     found or "impossible" otherwise

#     Because we start in 1,1 there is no case when both m and f
#     are even. Also, the same pair (m,f) can't be generated at different
#     levels, as this implies that both parents must be the same but inverted,
#     which cannot happen if don't explore one of the two main branches.

#     Given (x,y), and x>y (only at (1,1) does not happen)
#     Can be generated by either (1) (x,x+v) or (2) (y+w,y)
#     (1) implies y = x+v
#     (2) implies x = y+w

#     Because x>y
#     y+w > x+v
#     So w > v


#     We can substitute
#     x = x+v + w
#     0 = v+w

#     Which can only happen iff z=w=0

#     (7,5)
#     (5,2) or (2,5)

#     It is not needed to explore it as it is the same as the other but inverted


#     """
#     def is_solution(node, objective):
#         return ((node[0] == objective[0] and node[1] == objective[1]) or 
#                 (node[0] == objective[1] and node[1] == objective[0]))
        
#     def generate_outcomes(node, objective):
#         """Returns list of nodes
#         Two types of outcomes:
#         1. For each m generate new_f
#         2. For each f generate new_m
#         """
#         m = node[0]
#         f = node[1]
#         depth = node[2]
#         new = m+f
        
#         found = False
#         outcomes = []
        
#         # Keep within boundaries
#         if new > 10**50:
#             return outcomes, True
        
#         out1 = (m,new,depth+1)
#         out2 = (new,f,depth+1)

#         if is_solution(out1, objective) or is_solution(out2, objective):
#             return [out1,out2], True
        
#         # If an outcome already has a greater number of desired
#         # bombs, don't include it
#         if new <= objective[1]:
#             outcomes.append(out1)
#             # found = True if found or is_solution(out1)
            
#         if new <= objective[0]:
#             outcomes.append(out2)
        
#         return outcomes, False
        
        
        
#     solution_found = False
#     objective = (int(m), int(f))
#     current = (1,1,0)  # Adding first node (m,f,depth)

#     # Check base case
#     if is_solution(current, objective):
#         solution_found = True
    
#     # If both number of bombs is even, there is no solution???
#     if (objective[0]%2 == 0) and ((objective[1]%2 == 0)):
#         return "impossible"
    

#     # Both main branches are symmetrical, so we can only iterate over one
#     node_stack = [(1,2,1)]
    
#     # Width-first search
#     while len(node_stack) > 0 and not solution_found:
#         current = node_stack.pop(0) # Get element at the top
        
#         if is_solution(current, objective):
#             solution_found = True
#         else:
#             # Generate possible outcomes
#             outcomes, solution_found = generate_outcomes(current, objective)

#             if solution_found:
#                 current = outcomes[0]
            
#             # Put them at the end
#             node_stack.extend(outcomes)

#             # Depth-first
#             # for o in outcomes:
#             #     node_stack.insert(0, o)
    
#     if not solution_found:
#         depth = "impossible"
#     else:
#         depth = str(current[2])
    
#     return depth



# # Comprobar al generar
# # Explorar un lado es suficiente, el otro es el mismo

# from fractions import gcd

# def solution(m, f):
#     """This can be seen as looking upwards in a binary tree.
#     - (m,f) can't have both m and f even, as they start in (1,1)
#     - Can't also be m=f as one is passed from the father, and the other
#     is the sum of that number and other
    
#     So we can trace backwards from (m,f), substract the smallest from the biggest,
#     and repeat until (1,1) is reached or m or f is negative. The number of times
#     we repeat the cycle is the depth
#     """
#     m = int(m)
#     f = int(f)

#     print((m,f), "GCD:", gcd(m,f))

#     if gcd(m,f) != 1:
#         return "impossible"
    
#     solution_found = False
#     depth = 0

#     # Check for both even
    
#     while m>0 and f>0 and not solution_found:
#         print((m,f), "GCD:", gcd(m,f))
#         if (m,f) == (1,1):
#             solution_found = True
#         # elif m == 1:
#         #     solution_found = True
#         #     depth += f-1
#         elif f == 1:
#             solution_found = True
#             depth += m-1
#         # elif f == 2:
#         #     solution_found = True
#         #     depth += m / 2
#         else:
#             depth += 1
            
#             biggest, smallest = (m,f) if m>f else (f,m)
            
#             # No matter if we invert the tuple as both
#             # (m,f) and (f,m) are at the same depth. Both branches
#             # of the binary tree space are symmetrical
#             m = biggest - smallest
#             f = smallest
            
    
#     if solution_found:
#         return str(depth)
#     else:
#         return "impossible"

# from fractions import gcd

# def solution(m, f):
#     """This can be seen as looking upwards in a binary tree.
#     - In (m,f) both m and f can't be even at the same time, as they start in (1,1)
#     - Can't also have m=f as one is passed from the father, and the other
#     is the difference between the father and the other
    
#     So we can trace backwards from (m,f), substract the smallest from the biggest,
#     and repeat until (1,1) is reached or m or f is >= 0. The number of times
#     we repeat the cycle is the depth.
    
#     However, this algorithm is fast when both numbers are around the same size,
#     when they are not the process becomes slow as the depth increases.
    
#     Instead of going step by step we can speed up by moving many steps ahead,
#     if (m,f) and m>>f, then the parent will be ((m-f),f), and the next ((m-f-f),f),
#     and so on until f is bigger than the other number in the pair.
#     """
#     m = int(m)
#     f = int(f)
    
#     solution_found = False
#     depth = 0
    
#     # If the greatest common divisor is different from 1
#     # it has no solution
#     if gcd(m,f) != 1:
#         return "impossible"
    
#     # Loop
#     while m>=0 and f>=0 and not solution_found:
#         if (m,f) == (1,1): # Base case
#             solution_found = True
#         elif m == 0: # Reached the end
#             solution_found = True
#             depth -= 1 # We went one depth ahead
#         else:
#             biggest, smallest = (m,f) if m>f else (f,m)
            
#             # For a given pair, smallest will appear biggest//smallest times
#             repetitions = (biggest//smallest)
            
#             # No matter if we invert the tuple as both
#             # (m,f) and (f,m) are at the same depth. Both branches
#             # of the binary tree space are symmetrical
#             m = biggest - repetitions*smallest
#             f = smallest
            
#             depth += repetitions
            
    
#     if solution_found:
#         return str(depth)
#     else:
#         return "impossible"

# print("--------")
# print(solution('4','7')) # 4
# print(solution('2','1')) # 1
# print(solution('7','4')) # 4
# print(solution('1','2')) # 1
# print(solution('2001','1101'))
# print(solution('2000','1100000'))
# print(solution('1100000','2'))
# print(solution('1100000','1'))
# print(solution('1','1100000'))


# # print(solution('3','2'))
# # print(solution('6','4'))
# # print(solution('9','6'))
# # print(solution('12','8'))
# # print(solution('12','9'))

# # print(solution('2', '10000000000000000000000000000001'))

# # print(solution('100000000000000000000000000000000000000000000000000', '1000000000000000000000000000000000000000000000001'))

# # print(solution('2','1101'))
# # print(1101-((1101//901) * 901))
# # print(901-((901//200) * 200))
# # print(solution('901','1101'))
# # 900,1101
# # 201,900
# # 699,201
# # 201,498
# # 201,297
# # 96,201
# # 96,105
# # 9,96
# # 9,87
# # 9,78
# # 9,69
# # 9,60
# # 9,51
# # 9,42
# # 9,33
# # 9,24
# # 9,15
# # 9,6
# # 3,6
# # 3,3
# # 0

# # 1
# # 12340
# # print(solution('12340','12341'))
# # print(solution('11000','12341'))
# # print(solution('12341','11000'))
# # print(solution('1','1'))
# # print(solution('2','4'))
# # print(solution('4','2'))
# # print(solution('6','6'))
# # print(solution('1024','741'))
# # x = [2]
# # x.extend([])
# # print(x)
# # print((1,1) == (1,1))

# #     0
# #    1 2
# #  3 4 5 6
# # 7 8 9 10 11 12 13 14


# # 1,1
# # 1,2   2,1
# # 1,3  3,2   2,3  3,1
# # 1,4  4,3  3,5  5,2   2,5  5,3  3,4,  4,1
# # 1,5  5,4  4,7  7,3  3,8  8,5  5,7  7,2  
# # 1,6  6,5  5,9  9,4  4,11  11,7  7,10  10,3  3,11  11,8  5,12  12,7  7,9  9,2

# # Other branch is the same inverted

# # 2
# # 3
# # 4 5
# # 5 7 8 7
# # 6 9 11 10 11 13 12 9
# # 7 11 14 13 15 18 17 13 14 19 17 19 16 11

# # 2
# # 3
# # 4 5
# # 5 7 8
# # 6 9 10 11 12 13
# # 7 11 13 14 15 16 17 18 19


# # def solution(m, f):
# #     """m and f are ints as strings. Process:
# #     0. m=1 and f=1
# #     1a. for each m -> + one f
# #     1b. for each f -> + one m
# #     2. Repeat until objective achieved
    
# #     return number of cycles in the process
    
# #     The solution can be seen as exploring 
# #     a binary tree width-wise until finding the objective node,
# #     returning the depth of the first solution
# #     found or "impossible" otherwise
# #     """
# #     def is_solution(node, objective):
# #         """Inverted objective is at the same depth"""
# #         return (node[0] == objective[0] and node[1] == objective[1] or
# #                 node[0] == objective[1] and node[1] == objective[0])
        
# #     def generate_outcomes(node, objective):
# #         """Returns list of nodes and if solution found
# #         Two types of outcomes:
# #         1. For each m generate new_f
# #         2. For each f generate new_m
# #         """
# #         m = node[0]
# #         f = node[1]
# #         depth = node[2]
# #         new = m+f
        
# #         outcomes = []
        
# #         # Keep within boundaries
# #         if new > 10**50:
# #             return outcomes, False
        
# #         out1 = (m,new,depth+1)
# #         out2 = (new,f,depth+1)
        
# #         # Check for solution
# #         if is_solution(out1,objective) or is_solution(out2,objective):
# #             return [out1,out2], True
        
# #         # If an outcome already has a greater number of desired
# #         # bombs, don't include it
# #         if new <= objective[1]:
# #             outcomes.append(out1)
            
# #         if new <= objective[0]:
# #             outcomes.append(out2)
        
# #         return outcomes, False
        
        
    
# #     solution_found = False
# #     objective = (int(m), int(f))
# #     current = (1,1,0)
    
# #     # Check base case
# #     if is_solution(current,objective):
# #         solution_found = True
    
# #     # If both number of bombs is even, there is no solution (see docstring)
# #     if (objective[0]%2 == 0) and (objective[1]%2 == 0):
# #         return "impossible"
    
# #     # Both main branches are symmetrical, so we need to iterate only over one
# #     node_stack = [(1,2,1)] # Adding first node (m,f,depth)
    
# #     # Loop
# #     while len(node_stack) > 0 and not solution_found:
# #         current = node_stack.pop(0) # Get element at the top
        
# #         if is_solution(current, objective):
# #             solution_found = True
# #         else:
# #             # Generate possible outcomes
# #             outcomes, solution_found = generate_outcomes(current, objective)
            
# #             # Found solution, take depth from outcomes and terminate
# #             if solution_found:
# #                 current = outcomes[0]
            
# #             # Put them at the end (width-first)
# #             # node_stack.extend(outcomes)
            
# #             # Put them at the beggining (depth-first)
# #             # As we only iterate through one of the main branches
# #             # if there is solution is only generated once, and this ends
# #             # up being faster for large numbers
# #             for o in outcomes:
# #                 node_stack.insert(0,o)
    
# #     if not solution_found:
# #         depth = "impossible"
# #     else:
# #         depth = str(current[2])
    
# #     return depth


# Level 3 - Challenge 2

# def solution(l):
#     """Given list of ints return the number of lucky triples.
#     A lucky triple is a tuple where the first element divides the second,
#     and the second the third.
#     Numbers in the triple do not need to be one next to the other.
    
#     Examples values are ordered, but description does not indicates so.
#     Integers can appear multiple times.
#     A triple is ordering independent
    
#     O(n^2 + n) solution is to store in a matrix who divides who and then
#     check. Memory wise is n^2
#       1 2 3 4 5 6
#     1   t t t t t
#     2     f t f t
#     3       f f f
#     4         f f
#     5           f
#     6           
    
#       1 1 2 3 4 5 6
#     1   t t t t t t
#     1     t t t t t
#     2       f t f t
#     3         f f f
#     4           f f
#     5             f
#     6             
    
#       1 1 1
#     1   t t
#     1     t
#     1      
#     """
#     triples = 0
    
#     if len(l) < 3: # Base case
#         return triples
        
#     multiples = [] # For each element in l the number of multiples
#                    # in the remaining part of the list
    
#     # Create table
#     integers = []
#     for pos, i in enumerate(l): # Last row is empty
#         integers.append([])
#         multiples.append(0)
#         for j in l[pos+1:]:
#             if j%i==0:
#                 integers[pos].append(True)
#                 multiples[pos] += 1
#             else:
#                 integers[pos].append(False)
                
#     for pos_r, row in enumerate(integers):
#         # First column is not included, so we start at 1
#         for pos_c, element in enumerate(row, 1):
#             if element:
#                 # Add the number of multiples in that row
#                 triples += multiples[pos_r+pos_c]
                
    
#     return triples

# print(solution([1,1,1]))
# print(solution([1,2,3,4,5,6]))
# print(solution([1]*2000))


# Level 3 - Challenge 3
# Give feedback, matrix is simplified
"""
In level 3 challenge 3 the problem description indicates that the input matrix
"represents how many times that state has gone to the next state", meaning that
is the frequency of experiments. However, the example matrix is simplified, as
it shows instead the unit-frequency??
"""

"""
[
  [0,2,1,0,0], = [0,14,7,0,0]
  [0,0,0,3,4], = [0,0,0,3,4]
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0]

  - times through that state
  3 -> *7 = 14+7 = 21
  7 -> *2 = 6+8 = 14
  0
  0
  0

  terminals then 7+6+8=21
  probabilities 7,6,8  z
]

# [7,6,8,21]

1.sum total of experiments on each row (= sum col)
2. find index terminals (sum == 0)
3. for j in m[i,j] where m[i,j] != 0: # If an experiment is 2,1 prop-> multiply by 2 the row
  3.1 multiply m[j] * m[i,j]
  4.1 multiply m[i] * sum[j]

# Sum does not change, already calculated
4. for j in m[i,j] where m[i,j] != 0: # Update the state before with new values

5. for ind in terminals:
  5.1 sum column m[:,ind] = prop[j] (j starts at zero, append)

6. sum prop list = denominator

7. return [prop, denominator]

-------------

1. sum=[3,7,0,0,0]
2. ter=[2,3,4]
3.
[0,2,1,0,0],
[0,0,0,6,8], x2
[0,0,0,0,0], x1
[0,0,0,0,0],
[0,0,0,0,0]

[0,14,7,0,0], x7
[0,0,0,6,8],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]

5. prop=[7,6,8]
6. denominator=7+6+8=21
7. return [7,6,8,21]

-----------

# These are probabilities, not frequencies, or else would mean that s0
# has gone to s1 1 times but s1 has gone to s0 4 times
# Other option is that s0 is not the initial, but the descriptions says otherwise
# More likely options is they are simplified
[
  [0,1,0,0,0,1], = [0,9,0,0,0,9],
  [4,0,0,3,2,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0]

  - times through that state
  2 -> *9 = 18
  9
  0
  0
  0
  0

  terminals then 0+9+3+2=14 resulting states
  probabilities 0,3,2,9,  14
]

1. sum=[2,9,0,0,0,0]
2. ter=[2,3,4,5]
3.

[0,1,0,0,0,1],
[4,0,0,3,2,0], x1
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0] x1

[0,9,0,0,0,9], x9
[4,0,0,3,2,0], 
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]

5. prop=[0,3,2,9]
6. denominator=0+3+2+9=14
7. return [0,3,2,9,14]

--------------

[0,1,1,0,0,1],3
[4,0,0,3,2,0],9
[2,0,0,0,5,0],7
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0] 

1. sum=[3,9,7,0,0,0] mcm(21)
2. ter=[3,4,5]

0: 1,2,5
1: 0,3,4
2: 0,4

3: 1
4: 1,2
5: 0

3.

[ 0,63,63, 0, 0,63],143 x21 
[28, 0, 0,21,14, 0],63 x7
[18, 0, 0, 0,45, 0],63 x9
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0] x1

prop=[21,14+45=59,63]
denm = 143

return [21,59,63,143]



[0,1,0,0,0,1],2
[4,0,0,3,2,0],9
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]

[0,9,0,0,0,9],9
[4,0,0,3,2,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]

prop[3,2,9]
denm 14


[0,2,1,0,0],3
[0,0,0,3,4],7
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]

[0,14,7,0,0],x7
[0,0,0,6,8],x2
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]

[7,6,8,21]

1. sums
2. padre -> hijos (se puede descomponer, aka. ir de uno en uno y el valor final es el mismo)
  1. mcm(sums[padre], sums[hijos])
  2. multiply padre * (mcm/sums[padre])
  3. multiply cada hijo * (mcm/sums[hijo])







[0,1,2,0,0,1],4
[4,0,0,3,2,0],9
[0,1,0,0,0,4],5
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]

# mcm(padre[i], sum[i])
0: mcm(1, 9), mcm(2, 5), mcm(1, 0) = 9, 10, 0
1: mcm(4, 4), mcm(3, 0), mcm(2, 0) = 4, 0, 0
2: mcm(1, 9), mcm(4, 0)            = 9, 0

# mcm(mcm(padre[i], sum[i]), mcm(los que apuntan a padre)
0: mcm(9,10,4) = 180
1: mcm(4, 9) = 36
2: mcm(9,10) = 90

[ 0,180,360, 0, 0,180],720  x180
[144, 0, 0,108,72,  0],324  x36
[ 0, 90, 0,  0, 0,360],450  x90
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]


108,72,180+360=540,  720


mcd(180,36,90) = 9 -> 20,4,10

[ 0,20,40, 0, 0,20],80  x20
[16, 0, 0,12,8,  0],324  x4
[ 0, 10, 0,  0, 0,40],450  x10
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]

12,8,20+40=60, 80

-----

[0,1,0,0,0,1],2
[4,0,0,3,2,0],9
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]

0: mcm(1,9), mcm(1,0)           = 9, 0
1: mcm(4,2), mcm(3,0), mcm(2,0) = 4, 0, 0

0: mcm(9, 4) = 36
1: mcm(4, 2) = 4

mcd(36,4) = 4 -> 9,1

[0,9,0,0,0,9],18 x9
[4,0,0,3,2,0],9 x1
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]

0,3,2,9,18

----

[0,2,1,0,0],3
[0,0,0,3,4],7
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]

0: mcm(2,7), mcm(1,0) = 14, 0
1: mcm(3,0), mcm(4,0) = 0, 0

# A lo mejor es suma
0: mcm(14)    = 14   -> mcm(los del paso anterior, valor tabla que apunta a el)
1: mcm(0, 2) = 2

mcd(14,2) = 2 -> 7,1


[0,14,7,0,0],
[0,0,0,3,4],7
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]


----

Can loop to itself
Denominator in simplest form
Always path to terminal state

#  check transitions to other non-terminals or base

4
0-1-0

3
0-1-3

2
0-1-4

1
0-5

[0,3,2,9,14]
p(2) = 0/14
p(3) = 3/14
p(4) = 2/14
p(5) = 9/14

----

[0,1,0,0,0,1],2
[4,0,0,3,2,0],9
[0,0,0,0,0,0],0
[0,0,0,0,0,0],0
[0,0,0,0,0,0],0
[0,0,0,0,0,0],0

p(0) = 1 (Origen)
p(1|0) = 1/2
p(5|0) = 1/2
p(0|1) = 4/9
p(3|1) = 3/9
p(4|1) = 2/9

p(3|0) = p(1|0) + p(3|1) - p(-3|1)

p(2) = p(2|0) = 0 (No hay valores en esa columna)

p(1) = p(1|0) 1/2 + 4/9  = 17/18??
     = p(3) / p(3|1) = 3/14 / 3/9 = 9/14
     = p(1|0) + ??   = 1/2 + 1/7

p(3)
p(3) = p(3|1) * p(1) / p(1|3) 17/54?
p(3|0) * p(0) / p(0|3)
p(3|1) * p(1) = 

p(4)
p(5)
"""

import fractions

from fractions import gcd

# https://math.stackexchange.com/questions/2337832/given-a-probability-matrix-find-probability-that-person-at-zero-index-can-go-to

# https://math.stackexchange.com/questions/4515740/how-to-find-probability-of-ending-up-in-a-row-of-a-stochastic-matrix

# THEY DON'T SAY YOU SHOULDN'T LOOK ONLINE
#  However, I couldn't come up with an algorithmic method to get the result, as my best approach was:
#   1. Find each row denominator (sum elements in row)
#   2. For each non-terminal
#     2.1. Each non-zero item who points to another non-terminal must have the number of the denominator of such child
#   I found a solution in math.stackexchange who refers to the corrent answer, which I coded below.

# def solution(m):
#   """
#   I understood this problem is the same as finding the probability of reaching a node in a Markov chain.
#   """
#   def mcm(l):
#     return gcd(l) * math.prod(l)

#   res = []

#   # Find row sums (row denominator)
#   sums = [sum(row) for row in m]
#   print(sums)

#   x = {}
#   for i, row in enumerate(m):
#     x[i] = []
#     for j, prop in enumerate(row):
#       if prop != 0:
#         a = mcm([prop, sums[j]])
#         print(a)

#   print(x)

#   return res

# https://stackoverflow.com/questions/10508021/matrix-multiplication-in-pure-python

import fractions

def solution(m):
    """
    I understood this problem as the same as finding the probability of reaching a
    node in a Markov chain, which is referred in the literature as "absorbing
    markov chains" probabilities.
    
    The steps to solve this problem are:
    0. Work with fractions to simplify operations
    1. Move all terminal states to the back rows of the matrix (canonicalization)
    2. Decompose non-terminal states in matrix Q and R
    3. Extract N matrix as (Q_identity - Q)^-1
    4. Extract N_R matrix as NxR
    5. Get common denominator, reorder back and return
    """
    def row_is_terminal(row, state_id):
        """Because states can loop to itself but still be terminal.
        True if no outputs from that given state"""
        return sum(row[:state_id]) == 0 and sum(row[state_id+1:]) == 0

    def to_fractions(m):
        """Move matrix elements to Fraction"""
        new_m = []
        for i, row in enumerate(m):
            new_m.append([])
            denominator = sum(row)
            denominator = denominator if denominator != 0 else 1
            for numerator in row:
                new_m[i].append(fractions.Fraction(numerator, denominator))

        return new_m

  # ----------------------------------------------------------------------------

    def matsubt(a,b):
        """Subtraction of matrix a and b"""
        return [[a - b for a,b in zip(row_a, row_b)] for row_a, row_b in zip(a,b)]

    def matmult(a,b):
        zip_b = zip(*b)
        return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
                for col_b in zip_b] for row_a in a]

    # Matrix inverse functions from: stackoverflow question 32114054
    def transpose_matrix(m):
        return map(list,zip(*m))

    def get_matrix_minor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def get_matrix_determinant(m):
        # Base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*get_matrix_determinant(get_matrix_minor(m,0,c))
        return determinant

    def get_matrix_inverse(m):
        determinant = get_matrix_determinant(m)
        # Special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                  [-1*m[1][0]/determinant, m[0][0]/determinant]]

        # Find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactor_row = []
            for c in range(len(m)):
                minor = get_matrix_minor(m,r,c)
                cofactor_row.append(((-1)**(r+c)) * get_matrix_determinant(minor))
            cofactors.append(cofactor_row)

        cofactors = transpose_matrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors

    # ----------------------------------------------------------------------------

    def lcm(a,b):
        """Least common multiple"""
        return abs(a*b) // fractions.gcd(a,b)

    def list_lcm(l):
        """Least commom multiple in a list"""
        if len(l) == 1:
            return l[0]

        res = lcm(l[0],l[1])
        for e in l[2:]:
            res = lcm(res, e)

        return res

    def swap(x, i, j):
        """Swap elements in x"""
        tmp = x[j]
        x[j] = x[i]
        x[i] = tmp

    def swap_rows(m, i, j):
        """Swap rows in m"""
        swap(m,i,j) # swap row
        
        for row in m: # swap columns
            swap(row, i, j)

    # ----------------------------------------------------------------------------

    # Base cases:
    # - one state (always ends in there) -> solution=[1,1]
    # - two states, two options:
    #    1. state0 terminal, state1 unreachable -> solution=[1,1]
    #    2. state1 terminal, state0 non-terminal -> solution=[1,1]
    if len(m) == 1 or len(m) == 2:
        return [1,1]

    # Find terminal states
    terminals = []
    for i, row in enumerate(m):
        terminals.append(row_is_terminal(row, i))
    
    n_term = sum(terminals) # How many terminal states we have
    n_noterm = len(m) - n_term
    
    # 0. Move matrix elements to fractions
    m = to_fractions(m)
    
    # 1. Reorder matrix to canonicalized form (terminal states at the end)
    swaps = []
    for i in range(len(m)):
        # If terminal and there is some non-terminal behind
        if terminals[i] and sum(terminals[i+1:]) < (len(m)-i-1):
            # Find next non-terminal and swap
            j = i
            found = False
            while not found and j < len(m):
                j += 1
                if not terminals[j]:
                    swaps.append((i,j)) # Save swap
                    swap(terminals, i,j)
                    swap_rows(m, i, j)
                    found = True
      
    # 2. Q and R matrix. Both together are the non-terminal rows of the matrix
    q = [] # size (n_noterm,n_noterm)
    for i in range(n_noterm):
        q.append(m[i][:n_noterm])
    
    r = [] # size (n_noterm,n_term)
    for i in range(n_noterm):
        r.append(m[i][n_noterm:])
    
    q_identity = [] # Identity matrix of size (n_noterm,n_noterm)
    for i in range(n_noterm):
        q_identity.append([0] * n_noterm)
        q_identity[i][i] = 1
    
    # 3. Get N matrix as (Q_identity - Q)^-1
    n = get_matrix_inverse(matsubt(q_identity, q))
    
    # 4. Get N_R matrix
    n_r = matmult(n,r)
    
    # 5. Get common denominator
    denominators = [f.denominator for f in n_r[0]]
    common_denominator = list_lcm(denominators)
    
    # Get numerators
    res = []
    for n in n_r[0]:
        res.append(
          n.numerator * (common_denominator / n.denominator)
        )
    
    # Reorder probabilities back
    x = [-1] * n_noterm # Add non terminals back (can't use zero)
    x.extend(res) # Extend with terminals
    for s in swaps[::-1]: # Swap (from last swap to first)
      swap(x, s[0], s[1])
      
    res = [i for i in x if i != -1] # Remove non-terminals again
    
    # Append commom denominator
    res.append(common_denominator)
    
    return res

# ----------------------------
"""
3,8 fails
si base 0 y 1 fuera: 3,8,9
si base 0 fuera: 3,8
si base 1 fuera: 
"""

m = [[0]]
print(solution(m)) # 1, 1

m = [[0,1],[0,0]]
print(solution(m)) # 1, 1

m = [[1,0],[0,0]]
print(solution(m)) # 1, 1

# m = [
#   [0,2,1,0,0],
#   [0,0,0,3,4],
#   [0,0,0,0,0],
#   [0,0,0,0,0],
#   [0,0,0,0,0]
# ]
# print(solution(m)) # 7,6,8,  21

m = [
  [0,1,2,0,0],
  [0,0,0,0,0],
  [0,0,0,3,4],
  [0,0,0,0,0],
  [0,0,0,0,0]
]
print(solution(m)) # 7,6,8,  21

m = [
  [0,0,1,2,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,3,0,0,4],
  [0,0,0,0,0]
]
print(solution(m)) # 6,7,8,  21

m = [
  [0,0,2,1,0],
  [0,0,0,0,0],
  [0,3,0,0,4],
  [0,0,0,0,0],
  [0,0,0,0,0]
]
print(solution(m)) # 6,7,8,  21

# m = [[0,2,1,0,0],
#   [0,0,0,3,4],
#   [0,0,1,0,0],
#   [0,0,0,1,0],
#   [0,0,0,0,1]
# ]
# print(solution(m)) # 7,6,8,  21

m = [[0,1,0,0,0,1],
  [4,0,0,3,2,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0]
]
print(solution(m)) # 0,3,2,9  14

m = [
  [0,0,1,0,0,1],
  [0,0,0,0,0,0],
  [4,0,0,3,2,0],
  [0,0,0,0,0,0],
  [0,1,0,0,0,1],
  [0,0,0,0,0,0]
]
print(solution(m)) # 0,3,2,9  14


# m = [[0,1,1,0,0,1],
#   [4,0,0,3,2,0],
#   [2,0,0,0,5,0],
#   [0,0,0,0,0,0],
#   [0,0,0,0,0,0],
#   [0,0,0,0,0,0]
# ]
# print(solution(m)) #?

# m = [
# [0,1,2,0,0,1],
# [4,0,0,3,2,0],
# [0,1,0,0,0,4],
# [0,0,0,0,0,0],
# [0,0,0,0,0,0],
# [0,0,0,0,0,0]]
# print(solution(m)) # 12,8,60,  80


Level 4 - Challenge 1

"""
Infinite directions
If corner (0,0), (x_dim,y_dim), (0,y_dim), (x_dim,0) invert 
If wall invert one direction

"""

x y x
x t x

