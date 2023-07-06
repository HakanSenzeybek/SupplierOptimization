# A function to perform automatic differentiation.
from jax import grad
# A wrapped version of NumPy to use JAX primitives.
import jax.numpy as np
# A library for programmatic plot generation.
import matplotlib.pyplot as plt
# A library for data manipulation and analysis.
import pandas as pd

df = pd.read_csv('data/prices.csv')

print(df)

print(df.columns)

# Load the historical prices of supplier A and supplier B into variables prices_A and prices_B, respectively.
# Convert the price values into NumPy arrays with elements of type float32 using np.array function.
prices_A = np.array(df['price_supplier_a_dollars_per_item'], dtype=np.float32)
prices_B = np.array(df['price_supplier_b_dollars_per_item'], dtype=np.float32)
prices_A = np.array(df['price_supplier_a_dollars_per_item'], dtype=np.float32)
prices_B = np.array(df['price_supplier_b_dollars_per_item'], dtype=np.float32)

# Print some elements and mean values of the prices_A and prices_B arrays.
print("Some prices of supplier A:", prices_A[0:5])
print("Some prices of supplier B:", prices_B[0:5])
print("Average of the prices, supplier A:", np.mean(prices_A))
print("Average of the prices, supplier B:", np.mean(prices_B))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(prices_A, 'g', label="Supplier A")
plt.plot(prices_B, 'b', label="Supplier B")
plt.legend()

plt.show()


# Calculate f_of_omega, corresponding to the  𝑓𝑖(𝜔)=𝑝𝑖𝐴𝜔+𝑝𝑖𝐵(1−𝜔) Prices  {𝑝1𝐴,⋯,𝑝𝑘𝐴} and {𝑝1𝐵,⋯,𝑝𝑘𝐵}are saved in the arrays prices_A and prices_B.
# Thus, multiplying them by the scalars omega and 1 - omega and adding together the resulting arrays, you will get an array containing  {𝑓1(𝜔),⋯,𝑓𝑘(𝜔)}
# Then array f_of_omega can be taken to calculate L_of_omega, according to the expression:
# L_of_omega = (1/k) * ∑[i=1 to k] (f_i(𝜔) - f̄(𝜔))^2

def f_of_omega(omega):
    f = prices_A * omega + prices_B * (1 - omega)
    return f


def L_of_omega(omega):
    return 1 / len(f_of_omega(omega)) * np.sum((f_of_omega(omega) - np.mean(f_of_omega(omega))) ** 2)


print("L(omega = 0) =", L_of_omega(0))
print("L(omega = 0.2) =", L_of_omega(0.2))
print("L(omega = 0.8) =", L_of_omega(0.8))
print("L(omega = 1) =", L_of_omega(1))

# Analyzing the output above, it is evident that the values of the function 𝐿(𝜔) decrease as 𝜔 increases from 0 to 0.2, and then again from 0.8 to 1.
# However, there is an increase in 𝐿(𝜔) when 𝜔 equals 1.
# In order to determine the 𝜔 value that yields the minimum value of 𝐿(𝜔), a straightforward approach can be employed.
# Calculate the function values for each 𝜔 value in the range from 0 to 1 with a certain step size (e.g., 𝜔 = 0, 0.001, 0.002, ..., 1)
# and identify the minimum element in the resulting array.
# Please note that the function 𝐿(𝜔) was originally designed to work with a single value of 𝜔 rather than an array.
# Therefore, it is not necessary to modify the function to accept an array of 𝜔 values in this case.
# Instead, the values can be computed in the loop as the number of iterations will be limited.

# Parameter endpoint=True will allow ending point 1 to be included in the array.
# This is why it is better to take N = 1001, not N = 1000
N = 1001
omega_array = np.linspace(0, 1, N, endpoint=True)


# This is organised as a function only for grading purposes.
def L_of_omega_array(omega_array):
    N = len(omega_array)
    L_array = np.zeros(N)

    for i in range(N):
        ### START CODE HERE ### (~ 2 lines of code)
        L = L_of_omega(omega_array[i])
        L_array = L_array.at[i].set(L)
        ### END CODE HERE ###

    return L_array


L_array = L_of_omega_array(omega_array)

print("L(omega = 0) =", L_array[0])
print("L(omega = 1) =", L_array[N - 1])

# Now, to find the minimum point of the function 𝐿(𝜔), you can utilize the NumPy function argmin().
# Since there were 𝑁=1001 points considered in the interval [0, 1], the result obtained will be accurate to three decimal places:

i_opt = L_array.argmin()
omega_opt = omega_array[i_opt]
L_opt = L_array[i_opt]
print(f'omega_min = {omega_opt:.3f}\nL_of_omega_min = {L_opt:.7f}')


# This is organised as a function only for grading purposes.
def dLdOmega_of_omega_array(omega_array):
    N = len(omega_array)
    dLdOmega_array = np.zeros(N)

    for i in range(N):
        dLdOmega = grad(L_of_omega)(omega_array[i])
        dLdOmega_array = dLdOmega_array.at[i].set(dLdOmega)

    return dLdOmega_array


dLdOmega_array = dLdOmega_of_omega_array(omega_array)

print("dLdOmega(omega = 0) =", dLdOmega_array[0])
print("dLdOmega(omega = 1) =", dLdOmega_array[N - 1])

# To find the closest value of the derivative to 0, you can compute the absolute values of the derivative, ||𝑑𝐿/𝑑𝜔||,
# for each value of omega, and then find the minimum among them.

i_opt_2 = np.abs(dLdOmega_array).argmin()
omega_opt_2 = omega_array[i_opt_2]
dLdOmega_opt_2 = dLdOmega_array[i_opt_2]
print(f'omega_min = {omega_opt_2:.3f}\ndLdOmega_min = {dLdOmega_opt_2:.7f}')

# The result remains the same: 𝜔 = 0.702.
# Now, let's visualize the graphs of 𝐿(𝜔) and its derivative 𝑑𝐿/𝑑𝜔 to gain a better understanding.
# We can plot the function 𝐿(𝜔) to observe its minimum point and the derivative 𝑑𝐿/𝑑𝜔 to identify the point where its value is approximately 0.

# By plotting the graphs, we can visually confirm the minimum point of the function 𝐿(𝜔) at 𝜔 = 0.702
# and identify the corresponding point where the derivative is closest to 0.

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# Setting the axes at the origin.
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(omega_array, L_array, "black", label="$\mathcal{L}\\left(\omega\\right)$")
plt.plot(omega_array, dLdOmega_array, "orange", label="$\mathcal{L}\'\\left(\omega\\right)$")
plt.plot([omega_opt, omega_opt_2], [L_opt, dLdOmega_opt_2], 'ro', markersize=3)

plt.legend()

plt.show()
