import sympy as sp

#defining variables
a, theta = sp.symbols('a theta')


lorentzian = (a / sp.pi) * (1 / (1 + (a**2 * theta**2)))

# defining what the integrand is for the 2nd moment
integrand = theta**2 * lorentzian

# calculating the 2nd moment symbolically, -sp.oo, sp.oo = negative infinity and inifinity as lower and upper bound
variance = sp.integrate(integrand, (theta, -sp.oo, sp.oo))


print(f"Symbolic Variance (Second Moment): {variance}")


simplified_variance = sp.simplify(variance)
print(f"Simplified Variance: {simplified_variance}")

# Display the symbolic variance formula in LaTeX format
latex_variance = sp.latex(simplified_variance)
print(f"Latex: {latex_variance}")