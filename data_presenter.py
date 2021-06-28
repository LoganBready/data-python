from matplotlib import pyplot as plt


open_file = open('CupcakeInvoices.csv')

for data in open_file:
  print(data)

for line in open_file:
    cupcake = line.split(',')
    print(cupcake[2])

for line in open_file:
    cupcake = line.split(',')
    total = (int(cupcake[3]) * float(cupcake[4]))
    print(total)

total = 0

for row in open_file:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))

print(round(total, 2))

