var1, var2 = ' +123 ', '    78,77'
num1, num2 = (float(var1.lstrip().rstrip().replace(',', '.').replace(' ', '')),
              float(var2.lstrip().rstrip().replace(',', '.').replace(' ', '')))
print(f'Sum of two numbers: {num1:g} + {num2:g} = {num1 + num2:g} \n'
      f'Difference of two numbers: {num1:g} - {num2:g} = {num1 - num2:g}')