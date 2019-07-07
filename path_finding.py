import helper
import priority_queue


class PathFinder:
    def __init__(self, movement_cost, heuristic_cost, is_valid_move):
        """
        Initializes the path finder with relevant functions. Helps reduce the number of
        parameters in a function.

        Args:
            movement_cost: real movement cost, logically equivalent to h(n)
            heuristic_cost: assumed movement cost, logically equivalent to g(n)
            is_valid_move: takes a point and returns whether it is a valid position or not,
                and is used in the a* algorithm to element potential points

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
        """

        self.movement_cost = movement_cost
        self.heuristic_cost = heuristic_cost
        self.is_valid_move = is_valid_move

    def find_path(self, *args):
        """
        Takes start and end point and returns a list of points indicating path in the forward direction

        Args:
            *args: arguments required by generic_a_star function

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
        """

        store = self.generic_a_star(*args)
        if not store:  # if store is empty return empty path
            return []

        path = []
        path_itr = args[2]  # 3rd argument contains end point

        # iteration stops when path reaches start point or a point with no parent
        while path_itr in store:
            (_, parent) = store[path_itr]

            if path_itr == parent:
                break
            else:
                path.append(path_itr)
                path_itr = parent

        return list(reversed(path))

    def find_step(self, *args):
        """
        Takes start and end point and returns next step in the forward direction

        Args:
            *args: arguments required by generic_a_star function

        Return:
            (int, int): List of points to take to reach end in the forward direction
        """

        return self.find_path(*args)[0]

    def repair_path(self, moves, prev_path, m_steps):
        """
        Takes an existing path and performs repair/recomputation upto m steps ahead

        Args:
            moves: list of allowed moves at each point
            prev_path: previously calculated path where head of list indicates current position
            m_steps: number of steps ahead, to repair

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
        """

        start = moves[0]
        end_index = m_steps if m_steps < len(prev_path) else -1
        end = prev_path[end_index]

        repaired_path = self.find_path(moves, start, end)

        # extend path when end point is not same as end of previous path
        if end_index != -1:
            return repaired_path.extend(prev_path[end_index:-1])
        else:
            return repaired_path

    def generic_a_star(self, moves, start, end):
        """
        Performs an a* search on the map with the given set of moves
        queue implementation stores the state which consists of
        current position and estimated cost to end point. Based on
        the estimated cost the queue is sorted. The store is indexed
        on position and stores actual cost of reaching the point
        along with parent point.

        Note: end should be a valid point on the map

        Args:
            moves: list of allowed moves at each point
            start: x and y coordinates of start point
            end: x and y coordinates of end point

        Returns:
            store: contains the all the states encountered with links to parent states
                it can be used to generate the path and the next step
        """

        def total_cost(cur_pos, next_pos, end):
            return self.movement_cost(cur_pos, next_pos) + self.heuristic_cost(next_pos, end)

        queue = priority_queue.PriorityQueue()
        queue.push((self.heuristic_cost(start, end), start))
        store = {start: (0, start)}

        while not queue.is_empty():
            (_, cur_pos) = queue.pop()
            (cur_score, _) = store[cur_pos]
            if cur_pos == end:
                return store  # return store on reaching end

            next_moves = [helper.add_tuple_elements(cur_pos, move) for move in moves]
            valid_moves = [move for move in next_moves if self.is_valid_move(move)]
            possible_state = [(total_cost(cur_pos, move, end), move) for move in valid_moves]
            valid_state = [(next_score, next_pos) for (next_score, next_pos) in possible_state
                           if next_score <= cur_score + self.heuristic_cost(cur_pos, end)]
            update_state = [state for state in valid_state if state[1] not in store]
            for (next_score, next_pos) in update_state:
                store[next_pos] = (cur_score + self.movement_cost(cur_pos, next_pos), cur_pos)
                queue.push((next_score, next_pos))

        return {}
