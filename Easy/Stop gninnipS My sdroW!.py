#Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

#Examples:

#"Hey fellow warriors"  --> "Hey wollef sroirraw" 
#"This is a test        --> "This is a test" 
#"This is another test" --> "This is rehtona test"

# Solution 

def spin_words(sentence):
    ret = []
    splitSentence = sentence.split()
    for word in range(len(splitSentence)):
        if len(splitSentence[word]) > 4:
            ret.append(splitSentence[word][::-1])
        else:
            ret.append(splitSentence[word])
        if word != len(splitSentence)-1:
            ret.append(" ")
    return ''.join(ret)

# import codewars_test as test
# from solution import spin_words

# @test.describe("Stop gninnipS My sdroW!")
# def fixed_tests():
#     @test.it("Single word")
#     def _():
#         test.assert_equals(spin_words("Welcome"), "emocleW")
#         test.assert_equals(spin_words("to"), "to")
#         test.assert_equals(spin_words("CodeWars"), "sraWedoC")

#     @test.it("Multiple words")
#     def _():
#         test.assert_equals(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
#         test.assert_equals(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")

