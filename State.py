import random
import re


class State:
    def __init__(self, position, state_transitions: dict[str, int]):
        self.position = position
        self.state_transitions = state_transitions

    def get_next_state(self, url):
        for state in self.state_transitions.keys():
            if re.match(state, url):
                # print(str(state) + " matches the " + str(url) + " url part!")
                return self.state_transitions[state]
        return -1

    def get_random_next_state(self):
        return random.choice(list(self.state_transitions.items()))
