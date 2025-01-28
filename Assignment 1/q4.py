import sympy as sp

def find_critical_points(func_expr, var_symbols):
    """
    Find the critical points of a multivariable function f(x, y) by setting
    partial derivatives equal to zero.

    Parameters:
    - func_expr (str): The function expression as a string, e.g. "x**2 + y**2".
    - var_symbols (tuple): A tuple of Sympy symbols, e.g. (x, y).

    Returns:
    - List of solution dictionaries representing the critical points.
      Each dict maps symbol -> value, e.g. {x: val1, y: val2}
    """
    f = sp.sympify(func_expr)
    partials = [sp.diff(f, v) for v in var_symbols]
    critical_points = sp.solve(partials, var_symbols, dict=True)
    return critical_points


def classify_critical_points(func_expr, var_symbols, critical_points):
    """
    Classify each critical point as local min, local max, or saddle point
    using the second derivative test.

    Parameters:
    - func_expr (str): The function expression as a string.
    - var_symbols (tuple): A tuple of Sympy symbols, e.g. (x, y).
    - critical_points (list): List of dictionaries from `find_critical_points`.

    Returns:
    - A dictionary with keys "local_minima", "local_maxima", "saddle_points", and "inconclusive".
      Each value is a list of dicts containing:
        {
          'Point': (x_val, y_val),
          'f(x,y)': f_value
        }
    """
    f = sp.sympify(func_expr)

    f_x = sp.diff(f, var_symbols[0])
    f_y = sp.diff(f, var_symbols[1])
    f_xx = sp.diff(f_x, var_symbols[0])
    f_xy = sp.diff(f_x, var_symbols[1])
    f_yy = sp.diff(f_y, var_symbols[1])

    local_minima = []
    local_maxima = []
    saddle_points = []
    inconclusive_points = []

    for point in critical_points:
        x_val = point[var_symbols[0]]
        y_val = point[var_symbols[1]]

        f_xx_val = f_xx.subs(point)
        f_xy_val = f_xy.subs(point)
        f_yy_val = f_yy.subs(point)

        D = f_xx_val * f_yy_val - (f_xy_val)**2

        f_val = f.subs(point).evalf()

        if D > 0:
            if f_xx_val > 0:
                local_minima.append({
                    'Point': (x_val.evalf(), y_val.evalf()),
                    'f(x,y)': f_val
                })
            else:
                local_maxima.append({
                    'Point': (x_val.evalf(), y_val.evalf()),
                    'f(x,y)': f_val
                })
        elif D < 0:
            saddle_points.append({
                'Point': (x_val.evalf(), y_val.evalf()),
                'f(x,y)': f_val
            })
        else:
            inconclusive_points.append({
                'Point': (x_val.evalf(), y_val.evalf()),
                'f(x,y)': f_val
            })

    return {
        "local_minima": local_minima,
        "local_maxima": local_maxima,
        "saddle_points": saddle_points,
        "inconclusive_points": inconclusive_points
    }


import sympy as sp

def check_boundedness(func_expr, var_symbols):
    """
    Check if a multivariate polynomial function is bounded below or above by
    examining its leading term and mixed term behavior.

    Parameters:
    - func_expr (str or sympy expression): The function expression.
    - var_symbols (tuple): A tuple of sympy symbols, e.g., (x, y).

    Returns:
    - (is_bounded_below, is_bounded_above) as a tuple of booleans.
      Returns (False, False) for non-polynomials or for functions that are unbounded.
    """
    try:
        f = sp.sympify(func_expr)
        poly = sp.Poly(f, var_symbols)


        terms = poly.terms()

        leading_term = max(terms, key=lambda t: sum(t[0]))
        degree = sum(leading_term[0])  # Total degree of the leading term
        leading_coeff = leading_term[1]  # Coefficient of the leading term

        # Analyze the mixed terms for unboundedness
        is_bounded_below = False
        is_bounded_above = False

        if degree % 2 == 0:  # Even degree
            if leading_coeff > 0:
                is_bounded_below = True
            elif leading_coeff < 0:
                is_bounded_above = True

        # Check mixed terms for unboundedness
        for term, coeff in terms:
            term_degree = sum(term)
            if term_degree < degree:  # Mixed term of lower degree
                # If any mixed term allows for positive and negative behavior, mark unbounded
                is_bounded_below = False
                is_bounded_above = False
                break

        return is_bounded_below, is_bounded_above

    except sp.PolynomialError:
        # Return (False, False) for non-polynomial inputs
        return (False, False)



def find_global_extrema(func_expr, var_symbols):
    """
    Find global minima and maxima if they exist by combining:
      1) Critical points
      2) Local classification
      3) Boundedness test

    Parameters:
    - func_expr (str): The function expression as a string.
    - var_symbols (tuple): (x, y).

    Returns:
    - Dictionary with keys:
        "Global Minima" -> list of dictionaries with points and function values
        "Global Maxima" -> list of dictionaries with points and function values
    """
    critical_points = find_critical_points(func_expr, var_symbols)
    if not critical_points:
        return {
            "Global Minima": [],
            "Global Maxima": []
        }

    classification = classify_critical_points(func_expr, var_symbols, critical_points)
    local_minima = classification["local_minima"]
    local_maxima = classification["local_maxima"]

    is_bounded_below, is_bounded_above = check_boundedness(func_expr, var_symbols)

    global_minima = []
    global_maxima = []

    if is_bounded_below and local_minima:
        min_f_val = min(item['f(x,y)'] for item in local_minima)
        global_minima = [item for item in local_minima if item['f(x,y)'] == min_f_val]

    if is_bounded_above and local_maxima:
        max_f_val = max(item['f(x,y)'] for item in local_maxima)
        global_maxima = [item for item in local_maxima if item['f(x,y)'] == max_f_val]

    return {
        "Global Minima": global_minima,
        "Global Maxima": global_maxima
    }

def print_and_format_findings(func_expr, var_symbols):
    """
    Format and print the findings for a given function, including critical points,
    classifications, boundedness, and extrema.

    Parameters:
    - func_expr (str or sympy expression): The function expression.
    - var_symbols (tuple): A tuple of sympy symbols, e.g., (x, y).
    """
    # Ensure func_expr is a sympy expression    
    print(f"Function: {sp.pretty(func_expr)}")
    print("="*60)
    
    # Find critical points
    critical_points = find_critical_points(func_expr, var_symbols)
    print("\nCritical Points:")
    if critical_points:
        for idx, point in enumerate(critical_points, start=1):
            formatted_point = ', '.join([f"{var}={sp.N(coord, 4)}" for var, coord in point.items()])
            print(f"  {idx}. ({formatted_point})")
    else:
        print("  None found.")
    
    # Classify critical points
    classification = classify_critical_points(func_expr, var_symbols, critical_points)
    print("\nClassification:")
    
    def print_classification(category, items):
        print(f"  {category.capitalize()}:")
        if items:
            for item in items:
                point = item.get('Point', ())
                f_value = item.get('f(x,y)', None)
                point_str = ", ".join([f"{coord:.4f}" for coord in point])
                if f_value is not None:
                    print(f"    - Point: ({point_str}), f(x,y): {f_value:.4f}")
                else:
                    print(f"    - Point: ({point_str})")
        else:
            print("    None")
    
    print_classification('local minima', classification.get('local_minima', []))
    print_classification('local maxima', classification.get('local_maxima', []))
    print_classification('saddle points', classification.get('saddle_points', []))
    print_classification('inconclusive points', classification.get('inconclusive_points', []))
    
    # Check boundedness
    boundedness = check_boundedness(func_expr, var_symbols)
    print("\nBoundedness:")
    print(f"  Bounded Below: {'Yes' if boundedness[0] else 'No'}")
    print(f"  Bounded Above: {'Yes' if boundedness[1] else 'No'}")
    
    # Find global extrema
    global_extrema = find_global_extrema(func_expr, var_symbols)
    print("\nGlobal Extrema:")
    if any(global_extrema.values()):
        for extrema_type, extrema_list in global_extrema.items():
            print(f"  {extrema_type.replace('_', ' ')}:")
            if extrema_list:
                for item in extrema_list:
                    point = item.get('Point', ())
                    f_value = item.get('f(x,y)', None)
                    point_str = ", ".join([f"{coord:.4f}" for coord in point])
                    if f_value is not None:
                        print(f"    - Point: ({point_str}), f(x,y): {f_value:.4f}")
                    else:
                        print(f"    - Point: ({point_str})")
            else:
                print("    None")
    else:
        print("  No global extrema found.")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    x, y = sp.symbols('x y')
    
    functions = [
        "x**4 + x**2 - 6*x*y + 3*y**2",            # Function a
        "x**2 - 6*x*y + 2*y**2 + 10*x + 2*y - 5",  # Function b
        "x*y**2 + x**3*y - x*y",                  # Function c
        "3*x**4 + 3*x**2*y - y**3"                # Function d
    ]


    for i in range(len(functions)):
        print_and_format_findings(functions[i], (x, y))