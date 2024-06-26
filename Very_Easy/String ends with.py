# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    if len(ending) <= len(text):
        if text[-len(ending)] == ending[0] and text[-1] == ending[-1] and ending in text:
            return True
    return False