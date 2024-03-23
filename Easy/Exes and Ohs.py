# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. 
# The string can contain any char.
def xo(s):
    s = s.upper()
    return s.count("O") == s.count("X")