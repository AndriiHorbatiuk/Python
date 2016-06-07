N = None
i = None
Result = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


N = float(text_prompt('Enter the number: '))
if N < 0:
  print('No negative values please')
else:
  i = 0
  Result = 1
  for count in range(N):
    i = i + 1
    Result = Result * i
  print(Result)
  print (count)