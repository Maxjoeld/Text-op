import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif len(get_close_matches(word, data.keys())) > 0:
    yn= input("Did you mean %s instead ? Enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])
    if yn == "Y":
      return data[get_close_matches(word, data.keys())[0]]
    elif y == "N":
      return "The wordord doesn't exist. Please double check"
    else:
      return"We didn't understand your entry."
  else:
    return "The word does not exist in the library."
  return data[word]

word = input("Enter word: ")

output = translate(word)
# added this to remove entire word from array 

if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)

