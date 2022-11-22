import common
import dichtomy_method as dichtomy
import s_iteration_method as sm

epsilon = 10**-4
a = 0
b = 0.5
alpha = 1/5


print(f"Check sign change condition on segment [{a}, {b}] = {common.sign_change_condition(a, b)}\n\n")

print("==> Dichtomy method")

apriori_d = dichtomy.apriori_assessment(a, b, epsilon)
print(f'Apriori assessment: {apriori_d}')

x, iteration = dichtomy.method(a, b, epsilon)

print(f'X_{iteration} with epsilon {epsilon} = {x}\n')


print("==> Simple iteration method")

x1, iteration = sm.method(a, alpha, epsilon)

print(f'X_{iteration} with epsilon {epsilon} = {x1}\n')
