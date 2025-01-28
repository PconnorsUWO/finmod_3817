import numpy as np
import matplotlib.pyplot as plt

a = 0.9
lamda = 2

def U(x):
    """
    Piecewise utility function:
        U(x) = x^a             if x >= 0
               -lamda(-x)^a    if x < 0
    """
    return np.where(
        x >= 0,
        x**a,
        -lamda * ((-x)**a)
    )

def U_prime(x):
    """
    First derivative, piecewise:
       For x > 0: a x^(a-1)
       For x < 0: lamda*a*(-x)^(a-1)
    Note: x=0 is not defined (derivative blows up).
    """
    return np.where(
        x > 0,
        a * x**(a - 1),
        lamda * a * ((-x)**(a - 1))
    )

def U_doubleprime(x):
    """
    Second derivative, piecewise:
       For x > 0: a(a-1)*x^(a-2)
       For x < 0: -lamda*a*(a-1)*(-x)^(a-2)
    Note: x=0 is not defined (derivative blows up).
    """
    U2_pos = a * (a - 1) * x**(a - 2)           # x > 0
    U2_neg = -lamda * a * (a - 1) * ((-x)**(a - 2))  # x < 0
    U2 = np.zeros_like(x, dtype=float)
    U2.fill(np.nan) 
    mask_pos = (x > 0)
    mask_neg = (x < 0)

    U2[mask_pos] = U2_pos[mask_pos]
    U2[mask_neg] = U2_neg[mask_neg]
    return U2


x = np.linspace(-2, 2, 400) 

U_vals  = U(x)
U1_vals = U_prime(x)
U2_vals = U_doubleprime(x)



x_small_left  = -1e-8
x_small_right = 1e-8

U_left  = U(x_small_left)
U_right = U(x_small_right)

U1_left  = U_prime(x_small_left)
U1_right = U_prime(x_small_right)

print("=== Continuity at x=0 ===")
print(f" U(0) = {U(0)}")
print(f" U(x -> 0^-): U({x_small_left})  = {U_left}")
print(f" U(x -> 0^+): U({x_small_right}) = {U_right}")
print("We see both sides ~ 0, so the function is continuous at 0.\n")

print("=== Differentiability at x=0 ===")
print(f" U'(x -> 0^-): U'({x_small_left})  = {U1_left}")
print(f" U'(x -> 0^+): U'({x_small_right}) = {U1_right}")
print("Both sides blow up (very large numbers) => function not differentiable at 0.\n")

fig, axs = plt.subplots(3, 1, figsize=(7, 12), sharex=True)

axs[0].plot(x, U_vals, color='blue', label='U(x)')
axs[0].set_title('Utility Function U(x)')
axs[0].axvline(0, color='k', linestyle='--', linewidth=1)
axs[0].axhline(0, color='k', linestyle='--', linewidth=1)
axs[0].legend()
axs[0].grid(True)

axs[1].plot(x, U1_vals, color='green', label='U\'(x)')
axs[1].set_title('First Derivative U\'(x)')
axs[1].axvline(0, color='k', linestyle='--', linewidth=1)
axs[1].axhline(0, color='k', linestyle='--', linewidth=1)
axs[1].legend()
axs[1].grid(True)

axs[2].plot(x, U2_vals, color='red', label='U\'\'(x)')
axs[2].set_title('Second Derivative U\'\'(x)')
axs[2].axvline(0, color='k', linestyle='--', linewidth=1)
axs[2].axhline(0, color='k', linestyle='--', linewidth=1)
axs[2].legend()
axs[2].grid(True)

plt.savefig('q1.png')
