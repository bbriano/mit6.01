#!/usr/bin/env python3
from collections import deque

# ======================================================================
# My solution of problems from MIT 6.01 Lecture 2:
# https://www.youtube.com/watch?v=cQntMUMQyRw

# ----------------------------------------------------------------------
# Procedural

# Returns a smallest sequence of "inc" and "sqr" operations
# that when applied to initial results in goal.
# initial and goal are non-negative integers with initial <= goal.
def find_sequence_it(initial: int, goal: int) -> None:
    candidates = [[]]
    while True:
        tmp = []
        for c in candidates:
            end_inc = [*c, "inc"]
            if is_valid(initial, end_inc, goal):
                return end_inc
            tmp.append(end_inc)
            end_sqr = [*c, "sqr"]
            if is_valid(initial, end_sqr, goal):
                return end_sqr
            tmp.append(end_sqr)
        candidates = tmp

# Returns True if sequence of operation applied on initial
# value results in goal and False otherwise.
def is_valid(initial: int, sequence: list[str], goal: int) -> bool:
    for op in sequence:
        if op == "inc":
            initial += 1
        elif op == "sqr":
            initial *= initial
        else:
            raise ValueError("undefined operation: %s" % op)
    return initial == goal

# ----------------------------------------------------------------------
# Functional

# Returns a smallest sequence of "inc" and "sqr" operations
# that when applied to initial results in goal.
# initial and goal are non-negative integers with initial <= goal.
def find_sequence_rec(initial: int, goal: int) -> None:
    if initial == goal:
        return []
    inc = ["inc", *find_sequence_rec(initial+1, goal)]
    if initial > 1 and initial**2 <= goal:
        sqr = ["sqr", *find_sequence_rec(initial**2, goal)]
        if len(inc) < len(sqr):
            return inc
        else:
            return sqr
    return inc

# ----------------------------------------------------------------------
# Object-Oriented

class Node:
    def __init__(self, value: int, operation="", parent=None) -> None:
        self.value = value
        self.operation = operation
        self.parent = parent

# Returns a smallest sequence of "inc" and "sqr" operations
# that when applied to initial results in goal.
# initial and goal are non-negative integers with initial <= goal.
def find_sequence_oo(initial: int, goal: int) -> None:
    q = deque([Node(initial)])

    # On each level for each node, create "inc" and "sqr" child nodes
    # and halt if reached goal value.
    while q:
        n = q.popleft()
        if n.value == goal:
            node = n
            break
        q.append(Node(n.value+1, "inc", n))
        q.append(Node(n.value**2, "sqr", n))

    # Traverse upward from node constructing the operation sequence.
    res = []
    while node:
        res.append(node.operation)
        node = node.parent
    return list(reversed(res[:-1]))

# ----------------------------------------------------------------------
# Test

if __name__ == "__main__":
    print(find_sequence_it(1, 100))
    print(find_sequence_rec(1, 100))
    print(find_sequence_oo(1, 100))
