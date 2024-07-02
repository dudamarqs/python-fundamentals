salary = float(input('Informe o salário do funcionário: R$'))
if salary > 1250:
    new_salary = salary + (salary * (10/100))
if salary <= 1250:
    new_salary = salary + (salary * (50/100))
print('Novo salário do funcionário: R${:.2f}.'.format(new_salary))