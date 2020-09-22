# not solved (brute force not an option)
# def find_paths(grid_size, all_paths=0, current_path: list = None, pos=(0, 0)):
#     if pos == (0, 0):
#         new_path = [pos]
#         return find_paths(grid_size, 0, new_path.copy(), (0, 1)) + find_paths(grid_size, all_paths, new_path.copy(),
#                                                                               (1, 0))
#     elif pos == (grid_size, grid_size):
#         current_path.append(pos)
#         return all_paths + 1
#     else:
#         current_path.append(pos)
#         if pos[1] < grid_size:
#             all_paths = find_paths(grid_size, all_paths, current_path.copy(), (pos[0], pos[1] + 1))
#         if pos[0] < grid_size:
#             all_paths = find_paths(grid_size, all_paths, current_path.copy(), (pos[0] + 1, pos[1]))
#         return all_paths
#
#
# print(find_paths(20))

def fac(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


print(fac(40) // (fac(20) * fac(20)))
