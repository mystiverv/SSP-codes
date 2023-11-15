import sympy as sp

#variables
a, theta = sp.symbols('a theta')


gaussian = (a / sp.sqrt(sp.pi)) * sp.exp(-a**2 * theta**2)

#integrand for 2nd moment
integrand = theta**2 * gaussian

#calculating 2nd moment symbolically, -sp.oo, sp.oo = negative infinity and inifinity as lower and upper bound
variance = sp.integrate(integrand, (theta, -sp.oo, sp.oo))


print(f"Variance (Second Moment): {variance}")

simplified_variance = sp.simplify(variance)
print(f"simplified : {simplified_variance}")

# Display the symbolic variance formula in LaTeX format
latex_variance = sp.latex(simplified_variance)
print(f"Latex: {latex_variance}")