import random
import string

from State import State


class FSA:
    def __init__(self, state_transitions=None):
        self.states = []
        self.alphabet = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ")
        self.fin_states = [8, 11, 13, 14, 15]
        for i in range(len(state_transitions)):
            self.states.append(State(i, state_transitions[i]))

    def get_random_transition(self, transition):
        if transition in ["http", "s", ":","-"]:
            return transition
        elif transition in ["\/", "\."]:
            return transition[1:]
        elif transition == ".":
            return random.choice(self.alphabet)
        elif transition == "\w":
            return random.choice(list(string.ascii_letters + string.digits))
        elif transition == "[-\w]":
            return random.choice(list(string.ascii_letters + string.digits + "-"))

    def check(self, url: str):
        current_state = 0
        if len(url) < 4:
            print("There is nothing to check!")
            return
        elif len(url) > 1000:
            print("The url address is way too long!")
            return
        else:
            for c in url[3:]:
                # print("We are now on " + str(current_state) + " state!")
                if current_state == 0:
                    current_state = self.states[current_state].get_next_state(url[0:4])
                else:
                    current_state = self.states[current_state].get_next_state(c)
                # print("We get to " + str(current_state) + " state!")
                if current_state == -1:
                    print("The string does not match the FSA!")
                    return
        if current_state in self.fin_states:
            print("Seems like no error occurred!\nThe string does match the FSA!")
        else:
            print("The string does not match the FSA!")

    def generate(self):
        generated_string = ""
        current_state = 0
        finish = True
        # print("Current state is " + str(current_state) + ";\nCurrent generated_string is " +
        #      generated_string + ";\nIs it finish? " + str(finish))
        while finish:
            key, current_state = self.states[current_state].get_random_next_state()
            generated_string += self.get_random_transition(key)
            if current_state in self.fin_states:
                finish = random.choice(list({True, False}))
        print("Current state is " + str(current_state) + ";\nCurrent generated_string is " +
              generated_string + ";\nIs it finish? " + str(not finish))