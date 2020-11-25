# B is the relative benefit per weight of items
# for i in item
#     Bi = Pi/Wi
# Sort B from the largest to the samllest
# for item in B
#     for knap in knapsacks
#         if item can be put into knap
#             put the item into knap
# output the result
#
# Calculate the rest space of knapsacks
# for space in Restspace
#     for i in item
#         if there is enough space to put item
#             put i into the knapsack
#             put the result into neighborhood
# if there is no space to put any item
#     begin rotate
#     put the item into neighborhood
# next solution = the best solution in neighborhood
# if next solution < the current solution
#     break
#
# Sort the neighborhood according total value
# for solution in neighborhood
#     if solution is not tabu
#         next solution = solution
#         break
# put the next solution in tabu list

P = [10, 12, 15, 8, 7, 14, 16, 2, 6, 13, 15, 9, 7]
W = [5, 8, 7, 6, 4, 5, 8, 1, 3, 4, 6, 3, 3]
Knapsacks = [15, 10, 5]