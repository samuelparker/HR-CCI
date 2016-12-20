m, n = 6, 4
magazine = 'give me one grand Today night'
ransom = 'give one grand today'

def ransom_note(magazine, ransom):
  magazine = magazine.split()
  ransom = ransom.split()
  if len(magazine) < len(ransom): return False

  for word in ransom:
    if word in magazine:
      magazine.pop(magazine.index(word))
    else:
      return False

  return True


answer = ransom_note(magazine, ransom)
if answer:
  print 'Yes'
else:
  print 'No'