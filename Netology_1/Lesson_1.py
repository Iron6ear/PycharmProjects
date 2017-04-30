euro_cost = 28.5
residence_cost = 50
residence_limit = 90
sсhengen_constraint = 180

first_time_arriving = 5
first_time_leave = 17

second_time_arriving = 25
second_time_leave = 50

third_time_arriving = 75
third_time_leave = 180

total_time_in_es = (first_time_leave - first_time_arriving + 1) + (second_time_leave - second_time_arriving + 1) + \
                   (third_time_leave - third_time_arriving + 1)

total_expenses = residence_cost * total_time_in_es

print('Days in EU:', total_time_in_es)
print('One EUR cost', euro_cost, 'GRN')
print('Cost:', total_expenses, 'Euro', 'or', total_expenses * euro_cost, 'GRN')

if total_time_in_es > 77:
    print('A trip to Italy for free!!!')

if total_time_in_es > residence_limit:
    print('Limit is exceeded')
    print('Please select a different date')
else:
    print('Do not worry, you have time to visit the EU')

month_accumulate_salary = 5
oleg_salary = [1000,1200,1000,1120,700]
olga_salary = [900,1100,1300,600]
oleg_budget = sum(oleg_salary)
olga_average_salary = sum(olga_salary)/len(olga_salary)
olga_budget = olga_average_salary * month_accumulate_salary

common_budget = oleg_budget + olga_budget

if total_expenses < common_budget:
    print('Whi go!!!')
else:
    print(':(')