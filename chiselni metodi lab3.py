import numpy as np

def equations(x, y, z):
    return np.array([
        2 * x**2 - y**2 + z + 0.5,
        x**2 + 2 * y**2 - z - 1.94,
        x + 2 * y + 3 * z**2 - 2.23
    ])

def error_function(x, y, z):
    return np.sum(equations(x, y, z)**2)

def gradient(x, y, z):
    f1 = 2 * x**2 - y**2 + z + 0.5
    f2 = x**2 + 2 * y**2 - z - 1.94
    f3 = x + 2 * y + 3 * z**2 - 2.23
    
    grad_x = 2 * f1 * (4 * x) + 2 * f2 * (2 * x) + 2 * f3 * (1)
    grad_y = 2 * f1 * (-2 * y) + 2 * f2 * (4 * y) + 2 * f3 * (2)
    grad_z = 2 * f1 * (1) + 2 * f2 * (-1) + 2 * f3 * (6 * z)
    
    return np.array([grad_x, grad_y, grad_z])

x = float(input("Введіть початкове значення x: "))
y = float(input("Введіть початкове значення y: "))
z = float(input("Введіть початкове значення z: "))
lambd = 0.001  
accuracy = float(input("Введіть точність: "))
max_iterations = 1000000

operation_count = 0

for i in range(max_iterations):
    grad = gradient(x, y, z)
    grad_norm = np.linalg.norm(grad)

    x -= lambd * grad[0]
    y -= lambd * grad[1]
    z -= lambd * grad[2]

    operation_count += 1

    if grad_norm < accuracy :
        break

print("Розв'язок системи рівнянь:")
print(f"x = {x}, y = {y}, z = {z}")
print(f"Кількість операцій: {operation_count}")
