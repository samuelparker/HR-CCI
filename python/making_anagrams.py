a = "asfinaweagparonpszdovn"
b = "argvpoznvrsporngvpisraavr"

def number_needed(a,b):
  diff = {}
  strings = [a,b]
  for string in strings:
    for char in string:
      if (a.count(char) != b.count(char)) & ((char in diff) == False):
        diff[char] = abs(a.count(char) - b.count(char))

  return sum(diff.values())

print(number_needed(a,b))