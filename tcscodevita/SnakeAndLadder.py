from collections import deque

def parse_board(board):
    parsed_board = [line.split() for line in board]
    return [[parse_square(square) for square in row] for row in parsed_board]

def parse_square(square):
    if square == "Start":
        return "Start"
    if square == "End":
        return "End"
    if square.startswith("S("):
        return -int(square[2:-1])
    if square.startswith("L("):
        return int(square[2:-1])
    return int(square)

def possible_to_reach_end(board, die_inputs):
    board = parse_board(board)
    start, end = 1, 100
    visited = [False] * 101
    visited[start] = True
    queue = deque([(start, 0, 0, 0)])  

    while queue:
        position, snakes, ladders, moves = queue.popleft()

        if position == end:
            return f"Possible {snakes} {ladders}"

        for die in die_inputs:
            for _ in range(die):  
                new_position = position + 1
                if 1 <= new_position <= 100 and not visited[new_position]:
                    visited[new_position] = True
                    next_square = board[new_position - 1]  
                    if next_square == "Start":
                        next_square = 1
                    if next_square == "End":
                        next_square = 100
                    if isinstance(next_square, int):
                        if next_square < 0:
                            if next_square < -1:  
                                queue.append((new_position, snakes + 1, ladders, moves + 1))
                            else:  
                                queue.append((abs(next_square), snakes, ladders + 1, moves + 1))
                        else:
                            queue.append((next_square, snakes, ladders, moves + 1))

    return f"Not possible {snakes} {ladders}"

# Input
board = [
    "End 99 S(2) 97 96 95 94 93 92 91",
    "81 82 83 84 85 86 87 88 89 90",
    "80 79 78 77 76 L(99) 74 73 72 71",
    "61 62 S(22) 64 65 66 67 68 69 70",
    "60 59 58 57 56 55 54 53 52 51",
    "41 42 43 44 L(68) 46 47 48 49 50",
    "40 39 S(6) 37 36 35 34 33 32 31",
    "21 22 23 24 25 26 27 28 29 30",
    "20 19 18 17 S(9) 15 14 13 12 11",
    "Start 2 3 4 5 6 7 8 9 10"
]

die_inputs = [5, 4, 2, 4, 1]

# Output
result = possible_to_reach_end(board, die_inputs)
print(result)
