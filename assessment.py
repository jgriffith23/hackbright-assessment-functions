# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


"""The item_cost function calculates the total item cost, including tax.

    >>> item_cost("CA", 42.00)
    44.94

    >>> item_cost("FL", 42.00)
    44.1

    >>> item_cost("AZ", 42.00, .04)
    43.68
"""

def item_cost(state, initial_cost, tax=.05):

    #Check the state. If it's CA, set tax to .07.
    if state == "CA":
        tax = .07

    #Calculate total cost. 
    total_cost = initial_cost + initial_cost * tax

    #Round to two decimal places, since we're dealing with money, and return.
    return round(total_cost, 2)


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

"""The is_berry() function tells you whether your fruit is a berry or not.

    >>> is_berry("cherry")
    True

    >>> is_berry("strawberry")
    True

    >>> is_berry("blackberry")
    True

    >>> is_berry("watermelon")
    False

    >>> is_berry("BLackBerrY")
    True
"""

def is_berry(fruit):

    #First, convert the fruit name to all lowercase to account for typos.
    fruit = fruit.lower()

    #Check the fruit's name! If it fits our definition of a berry,
    #then return True. Otherwise, the answer is False.
    if (fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry"):
        return True
    else:
        return False


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

"""The shipping_cost() function tells how much you'll get charged for shipping.
   This is different for berries and non-berries.

   >>>shipping_cost("cherry")
   0

   >>>shipping_cost("Pineapple")
   5
"""

def shipping_cost(fruit):

    #We ship berries for free! Check whether the shipment is a berry.
    if is_berry(fruit) is True:
        return 0

    #If it's not a berry, we want to make money. Charge $5.
    elif is_berry(fruit) is False:
        return 5


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

"""The is_hometown() function will check to see if the town given is Lecanto.
   The hometown variable can be changed so others can reuse this code for their own hometown.

    >>>is_hometown("San Francisco)
    False

    >>>is_hometown("Lecanto")
    True
"""

def is_hometown(town_name):
    #Set your hometown.
    hometown = "Lecanto"

    #Check the given hometown. If it's yours, return True. Otherwise, the user
    #got it wrong. Return False!
    if town_name == hometown:
        return True

    else:
        return False

#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


"""The full_name() function generates a user's complete name, given their first and
   last names.

   >>> full_name("Jennifer", "Griffith-Delgado")
   Jennifer Griffith-Delgado

"""

def full_name(first_name, last_name):

    #Include a space between the two names, as is American English convention.
    return "{} {}".format(first_name, last_name)


#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

"""The hometown_greeting function() tells anyone from Lecanto that they're from
   the same place as me! If they're not from Lecanto, it asks for their hometown.

   >>>hometown_greeting("London", "Jackie", "Brown")
   Hi, Jackie Brown, where are you from?

   >>>hometown_greeting("Lecanto", "Jane", "Hacker")
   Hi, Jane Hacker, we're from the same place!

"""

def hometown_greeting(hometown, first_name, last_name):

    #Start the greeting. This part won't change, so we can store it on its own.
    greeting_string = "Hi, {} {}, "

    #Change the end of the greeting based on where the person is from.
    if is_hometown(hometown) is True:
        greeting_string += "we're from the same place!"
    else:
        greeting_string += "where are you from?"


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

"""The increment() function lets you create a customizable adding function. 

   The default is to add 1 to any number passed, but by passing different arguments to 
   increment(), you can tell your custom function to increment by any number you like.

   >>> addten = increment(10)
   >>> addten(20)
   30

   >>> addfour = increment(4)
   >>> addfour("carrot")
   You must pass a number. Please try again.

"""

def increment(x=1):

    #Ask the user to try a different input if they use a string or any other non-numeric
    #type. This will prevent errors that can arise if they use a string to create the adder
    #and then try a number later, or vice versa.
    if (isinstance(x, int) != True) and (isinstance(x, float) != True):
        print "You must pass a number. Please try again."
        return

    #Create the custom adding function.
    def add(y):
        try: 
            return x + y
        except TypeError:
            print "You muts pass a number. Please try again."
            return
    return add

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)
print "1"
addfive(5)
print "2"
addfive(20)
print "3"
addfive("carrot")

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

"""The add_number_to_list() function simply places a passed number at the end of a
   passed list.

   >>> nums = [1,2,3]
   >>> add_number_to_list(42, nums)
   >>> nums
   [1, 2, 3, 43]

   >>> add_number_to_list("23", nums)
   The first argument is not a number. Please try again.
"""

def add_number_to_list(number, number_list):
    if (isinstance(number, float) != True) or (isinstance(number, int) != True):
        print "The first argument is not a number. Please try again."
        return
    return number_list.append(number)

#####################################################################

#----------------------Tests (Added by JG)--------------------------#

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED!"
    print