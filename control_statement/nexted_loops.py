# for iterating_var in sequence:
#    for iterating_var in sequence:
#       statements(s)
#       statements(s)

# while expression:
#    while expression:
#       statement(s)
#    statement(s)

for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print ("{:3d}".format(k), end=' ')
   print()