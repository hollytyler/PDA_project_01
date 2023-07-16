family = {"dad": 57, "mum": 55, "brother": 32, "sister": 25, "me": 27}

def get_age(person):
    return person["brother"]

print(get_age(family))


# A Dictionary is a collection pairing between keys and associated values.
# The keys act as a label for the given value and can be used to call said 
# value if needed.

# In ths function I wante to list the age of the person within the "family"
# Dictionary. Since their ages were their only associated value I had the 
# function call the key "brother" so it could print the value of the key which
# is the age 32.