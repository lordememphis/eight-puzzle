from collections import deque
from state import State


class Puzzle:
    def __init__(self, initial_state):
        self.initial = initial_state
        self.final = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.sol_node = State
        self.board_len = 0
        self.board_side = 0
        self.traversed_nodes = 0
        self.max_search_depth = 0
        self.max_frontier_size = 0
        self.moves = list()
        self.costs = set()

    def solution(self):
        explored, queue = set(), deque([State(self.initial, None, None, 0, 0, 0)])

        while queue:

            node = queue.popleft()

            explored.add(node.map)

            if node.state == self.sol_node:
                self.sol_node = node
                return queue

            neighbors = self.traverse(node)

            for neighbor in neighbors:
                if neighbor.map not in explored:
                    queue.append(neighbor)
                    explored.add(neighbor.map)

                    if neighbor.depth > self.max_search_depth:
                        self.max_search_depth += 1

            if len(queue) > self.max_frontier_size:
                self.max_frontier_size = len(queue)

        return ['no solution']

    def traverse(self, node):
        self.traversed_nodes += 1

        neighbors = list()

        neighbors.append(State(self.move_cell(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move_cell(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move_cell(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move_cell(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))

        nodes = [neighbor for neighbor in neighbors if neighbor.state]

        return nodes

    def move_cell(self, state, position):
        new_state = state[:]

        index = new_state.index(0)

        if position == 1:  # Up

            if index not in range(0, self.board_side):

                temp = new_state[index - self.board_side]
                new_state[index - self.board_side] = new_state[index]
                new_state[index] = temp

                return new_state
            else:
                return None

        if position == 2:  # Down

            if index not in range(self.board_len - self.board_side, self.board_len):

                temp = new_state[index + self.board_side]
                new_state[index + self.board_side] = new_state[index]
                new_state[index] = temp

                return new_state
            else:
                return None

        if position == 3:  # Left

            if index not in range(0, self.board_len, self.board_side):

                temp = new_state[index - 1]
                new_state[index - 1] = new_state[index]
                new_state[index] = temp

                return new_state
            else:
                return None

        if position == 4:  # Right

            if index not in range(self.board_side - 1, self.board_len, self.board_side):

                temp = new_state[index + 1]
                new_state[index + 1] = new_state[index]
                new_state[index] = temp

                return new_state
            else:
                return None

    def pts(self):
        current_node = self.sol_node

        while self.initial != current_node.state:

            if current_node.move_cell == 1:
                movement = 'Up'
            elif current_node.move_cell == 2:
                movement = 'Down'
            elif current_node.move_cell == 3:
                movement = 'Left'
            else:
                movement = 'Right'

            self.moves.insert(0, movement)
            current_node = current_node.parent

        return self.moves
