from custom_classes import Calculator

calc = Calculator()
step1 = calc.add(10,5)
step2 = calc.multiply(step1,3)
final_result = calc.divide(step2, 3)
print(final_result)
