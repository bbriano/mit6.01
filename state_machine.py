#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

State = TypeVar("State")
Input = TypeVar("Input")
Output = TypeVar("Output")

# State Machine base class.
class SM(ABC, Generic[State, Input, Output]):
    def __init__(self):
        self.state = self.start_state()

    # Step updates machine state and returns the output value.
    def step(self, inp: Input) -> Output:
        s, o = self.transition(self.state, inp)
        self.state = s
        return o

    # Transduce feed inputs to the machine in order and returns a sequence of output.
    def transduce(self, inputs: [Input]) -> [Output]:
        return [self.step(inp) for inp in inputs]

    # Use to set initial state of state machine.
    @abstractmethod
    def start_state() -> State:
        pass

    # Transition returns the next state and output values.
    @abstractmethod
    def transition(state: State, inp: Input) -> (State, Output):
        pass

# Accumulator has initial state 0. It takes an integer as input
# to increment or decrement the state respectively.
# The nth output is the (n+1)th state.
class Accumulator(SM):
    def __init__(self):
        super().__init__()

    @staticmethod
    def start_state():
        return 0

    @staticmethod
    def transition(state, inp):
        return (state+inp, state+inp)

# UpDown has initial state 0. It takes "u" and "d" as input
# to increment and decrement the state respectively.
# The nth output is the (n+1)th state.
class UpDown(SM):
    def __init__(self):
        super().__init__()

    @staticmethod
    def start_state():
        return 0

    @staticmethod
    def transition(state, inp):
        if inp == "u":
            return (state+1, state+1)
        elif inp == "d":
            return (state-1, state-1)
        else:
            raise ValueError("undefined input: %s" % inp)

# Delay delays the input stream by one time step.
# The first output is specified by v0 in __init__.
class Delay(SM):
    def __init__(self, v0):
        self.init_value = v0
        super().__init__()

    def start_state(self):
        return self.init_value

    @staticmethod
    def transition(state, inp):
        return (inp, state)

# Average2 outputs the average of the last 2 input values.
class Average2(SM):
    def start_state(self):
        return 0

    @staticmethod
    def transition(state, inp):
        return (inp, (state+inp)/2)

# Sum3 outputs the sum of the last 3 input values.
class Sum3(SM):
    def start_state(self):
        return (0, 0)

    @staticmethod
    def transition(state, inp):
        return ((state[1], inp), state[0]+state[1]+inp)
