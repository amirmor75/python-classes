
[1,5,2,6]
(1,2,3)
# new data structure! dictionary!


empty_dictionary = {}
empty_dictionary["brand"]="Ford"

thisdict = {
  "שם": "תנועה שפתית קולית או מילולית שמקושרת לעצם או יצור חי",
  "אופניים": "כלי תחבורה דו גלגלי לא ממונע",
  "שנה": 'סתם הגדרה לשנה'
}
print(thisdict)

thisdict = {
  'key':'value',
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(thisdict)
# get value using a certian key 
thisdict['year']
# set a new value to an existing key, or a new key 
thisdict['year'] = 'new_value'
thisdict['wheels_number'] = 4
print(thisdict)
# print(thisdict['value'])

##########################################################
print(thisdict.keys())
thisdict.update({})
value_of_year_kay = thisdict.pop('year')




# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.






# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Example
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)






# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
    
print(len(thisdict))







# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}