def solve_puzzle(puzzle_array, index=0, visited=None):
    """Returns True (False) if a given board is (is not) solveable"""
    if visited is None:
        visited = set()
    # 1) Base case: have you found a valid solution?
    if len(puzzle_array) - 1 == index:
        return True
    # 2) Find all valid next-steps
    step = puzzle_array[index] + index
    negstep = index - puzzle_array[index]
    length = len(puzzle_array)
    # Normalize the steps to stay within the puzzle bounds
    step = step % length
    negstep = negstep % length
    if step not in visited and negstep not in visited:
        visited.add(step)
        visited.add(negstep)
        return solve_puzzle(puzzle_array, step, visited) or solve_puzzle(puzzle_array, negstep, visited)
    elif step not in visited:
        visited.add(step)
        return solve_puzzle(puzzle_array, step, visited)
    elif negstep not in visited:
        visited.add(negstep)
        return solve_puzzle(puzzle_array, negstep, visited)
    else:
        return False
    # 3) Recursively explore next-steps, returning True if any valid solution is found
  
