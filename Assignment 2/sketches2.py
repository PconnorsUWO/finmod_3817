import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plotting
from matplotlib.patches import Circle, Rectangle

def plot_a_R2():
    # Sketch for (a) in ℝ²: Plot the line x+y=1
    x = np.linspace(-1, 2, 400)
    y = 1 - x
    plt.figure()
    plt.plot(x, y, label=r'$x+y=1$')
    # Mark the intercepts (1,0) and (0,1)
    plt.scatter([1, 0], [0, 1], color='red', zorder=5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sketch (a) in R²: $x+y=1$')
    plt.legend()
    plt.grid(True)
    plt.savefig("a_R2.png")
    plt.close()

def plot_a_R3():
    # Sketch for (a) in ℝ³: Plot the plane x+y=1.
    # The plane is given by {(x, y, z): x+y=1, z free}.
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Create a grid for x and z (free variable)
    x = np.linspace(-1, 2, 50)
    z = np.linspace(-1, 2, 50)
    X, Z = np.meshgrid(x, z)
    # For any (x, z), y = 1-x.
    Y = 1 - X
    ax.plot_surface(X, Y, Z, alpha=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Sketch (a) in R³: Plane $x+y=1$')
    plt.savefig("a_R3.png")
    plt.close()

def plot_b():
    # Sketch for (b): Half-spaces determined by the line 2x+y=4.
    # Equation: y = 4 - 2x.
    x = np.linspace(-2, 4, 400)
    y_line = 4 - 2*x
    plt.figure()
    # Shade the half-space where 2x+y >= 4 (using \geq instead of \ge)
    plt.fill_between(x, y_line, 10, color='blue', alpha=0.2, label=r'$2x+y \geq 4$')
    # Shade the half-space where 2x+y <= 4 (using \leq instead of \le)
    plt.fill_between(x, -10, y_line, color='green', alpha=0.2, label=r'$2x+y \leq 4$')
    # Plot the separating line
    plt.plot(x, y_line, 'k-', linewidth=2, label=r'$2x+y=4$')
    # Plot the points (1,0) and (0,5)
    plt.scatter([1, 0], [0, 5], color='red', zorder=5)
    plt.text(1, 0, ' (1,0)', fontsize=10, color='red')
    plt.text(0, 5, ' (0,5)', fontsize=10, color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sketch (b): Half-Spaces determined by $2x+y=4$')
    plt.xlim(-2, 4)
    plt.ylim(-10, 10)
    plt.legend()
    plt.grid(True)
    plt.savefig("b.png")
    plt.close()

def plot_c():
    # Sketch for (c): Separation of two sets by the line 2x+y=4.
    # Set A: Circle with center (0,0) and radius 0.5.
    # Set B: Circle with center (2,2) and radius 0.5.
    fig, ax = plt.subplots()
    circle_A = Circle((0, 0), 0.5, fill=False, edgecolor='blue', linewidth=2, label='Set A')
    circle_B = Circle((2, 2), 0.5, fill=False, edgecolor='red', linewidth=2, label='Set B')
    ax.add_patch(circle_A)
    ax.add_patch(circle_B)
    # Plot the line: y = 4 - 2x.
    x = np.linspace(-1, 4, 400)
    y_line = 4 - 2*x
    ax.plot(x, y_line, 'k-', linewidth=2, label=r'$2x+y=4$')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Sketch (c): Separation by $2x+y=4$')
    ax.set_xlim(-2, 5)
    ax.set_ylim(-2, 5)
    ax.legend()
    ax.grid(True)
    plt.savefig("c.png")
    plt.close()

def plot_e_tangent():
    # Sketch for (e) - Tangential Hyperplane example:
    # S is the unit disk and the line x=1 is a tangential hyperplane touching at (1,0).
    fig, ax = plt.subplots()
    circle = Circle((0, 0), 1, fill=False, edgecolor='blue', linewidth=2, label='Unit Disk')
    ax.add_patch(circle)
    # Plot the tangential line: x = 1.
    ax.plot([1, 1], [-1.5, 1.5], 'k-', linewidth=2, label=r'$x=1$')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Sketch (e) Tangential Hyperplane')
    ax.set_xlim(-1.5, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.legend()
    ax.grid(True)
    plt.savefig("e_tangent.png")
    plt.close()

def plot_e_supporting():
    # Sketch for (e) - Supporting Hyperplane (non-tangential) example:
    # S is the square [0,1]x[0,1] and the line x=1 supports S along its entire edge.
    fig, ax = plt.subplots()
    square = Rectangle((0, 0), 1, 1, fill=False, edgecolor='blue', linewidth=2, label='Square S')
    ax.add_patch(square)
    # Plot the vertical supporting line x=1.
    ax.plot([1, 1], [-0.5, 1.5], 'k-', linewidth=2, label=r'$x=1$')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Sketch (e) Supporting (non-tangential) Hyperplane')
    ax.set_xlim(-0.5, 2)
    ax.set_ylim(-0.5, 2)
    ax.legend()
    ax.grid(True)
    plt.savefig("e_supporting.png")
    plt.close()

def plot_f():
    # Sketch for (f): Set S = { (x,y): x in [0,π], y ≤ sin(x) }.
    # Plot the curve y = sin(x) for x in [0,π] and shade the region below.
    x = np.linspace(0, np.pi, 400)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'k-', linewidth=2, label=r'$y=\sin(x)$')
    # Shade the region y <= sin(x). Here we shade from a base value (e.g., -0.5) to the curve.
    ax.fill_between(x, y, -0.5, color='gray', alpha=0.3, label=r'Region: $y \leq \sin(x)$')
    # Mark the extreme points (the endpoints of the curve).
    ax.scatter([0, np.pi], [np.sin(0), np.sin(np.pi)], color='red', zorder=5, label='Extreme Points')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(r'Sketch (f): $\{(x,y): x\in[0,\pi], y \leq \sin(x)\}$')
    ax.set_xlim(0, np.pi)
    ax.set_ylim(-0.5, 1.5)
    ax.legend()
    ax.grid(True)
    plt.savefig("f.png")
    plt.close()


if __name__ == "__main__":
    plot_a_R2()
    plot_a_R3()
    plot_b()
    plot_c()
    plot_e_tangent()
    plot_e_supporting()
    plot_f()