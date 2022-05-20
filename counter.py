# initializing string
given_text = "A computer is a programmable electronic device that accepts raw data as an input and processes it with set of instructions to produce the result as output"

# printing original text
# print("The original string is : " + given_text)

# using split() to count words in the text
res = len(given_text.split())

# printing result
print("The number of words are : " + str(res))
