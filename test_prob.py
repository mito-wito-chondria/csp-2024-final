#importing the functions that will be tested
from prob import ten_wishes
from prob import fifty_fifty


def test_wish_probability():
    #testing for if the user put one wish
    result = ten_wishes(1)
    #then testing if the result is the same as the one from the function
    #just repeats for if the user picked 5, or 9 just to have a good variety 
    assert result == 'The probabilty of pulling a 4 star is a 11.11111111111111% chance!'
    result = ten_wishes(5)
    assert result == 'The probabilty of pulling a 4 star is a 20.0% chance!'
    result = ten_wishes(9)
    assert result == 'The probabilty of pulling a 4 star is a 100.0% chance!'

def test_fifty_fifty_probability():
    #tests for if the user picked won
    result = fifty_fifty('won')
    #tests to see if the result is the same
    assert result == 'you have a 25% chance of winning your next 50/50'
    #test for if the user lost their last 50/50
    result = fifty_fifty('lost')
    #test to see if the result is the same
    assert result == 'you have a 50% chance of winning your next 50/50'