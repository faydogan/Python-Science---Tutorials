import re

# To examine regular expression (RegEx) operators goto
# https://docs.python.org/3/library/re.html
# To test your regex patterns goto
# https://regex101.com/

# Define some example strings to extract numbers from those
example_string_1 = "TransactionIDE34567 is failed. \
    TransactionIDF304567 is failed."
example_string_1_1 = "E034567 is failed."
example_string_2 = "You should by 1 banana, 2 apples, and 5 papayas"
example_string_3 = "My brithday is 11.07.1900"
example_string_int = "Total PO number is 341"
example_string_float = "Package weights 21.9"

# LET'S EXTRACT TRANSACTION ID FROM FIRST AND SECOND STRINGS
# re.seach() method (Search string for given pattern and return first object):
search_result = re.search("[A-Z]{1}\d{5,6}", example_string_1)
print(search_result) # Returns found object
search_result = re.search("aaaa", example_string_1)
print(search_result) # Returns None because no match found

# re.match() method (Only matches from start of a line for each line):
search_result = re.match("[A-Z]{1}\d{5,6}", example_string_1_1)
print(search_result) # Returns found object
search_result = re.match("aaaa", example_string_1_1)
print(search_result) # Returns None because no match found

# re.findall() method:
search_result = re.findall("[A-Z]{1}\d{5,6}", example_string_1)
print(search_result) # Returns found object
search_result = re.findall("aaaa", example_string_1)
print(search_result) # Returns None because no match found

# LET'S EXTRACT SHOPPING LIST FROM THIRD STRING
search_result = re.findall("\d{1,}\s{1}\w{1,30}", example_string_2)
print("My shopping list:", search_result)

# LET'S EXTRACT DATE FROM STRING
search_result = re.findall("\d{1,2}[.]\d{1,2}[.]\d{4}", example_string_3)
print("My date strings:", search_result)

# LET'S EXTRACT INTEGER AND FLOAT NUMBERS AND CONVERT THEM
search_result = re.findall("\d{1,}", example_string_int)
search_result = [int(num) for num in search_result]
print(
    "My int values:", search_result, "Check type", 
    type(search_result[0])
    )

search_result = re.findall("\d{1,}[.]\d{1,}", example_string_float)
search_result = [float(num) for num in search_result]
print(
    "My int values:", search_result, "Check type", 
    type(search_result[0])
    )