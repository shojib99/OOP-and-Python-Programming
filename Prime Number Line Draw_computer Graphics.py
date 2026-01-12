import matplotlib.pyplot as plt

x = [1, 2, 5, 13]
y = [3, 8, 7, 19]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_x = []
prime_y = []

for i in range(len(x)):
    if is_prime(x[i]) and is_prime(y[i]):
        prime_x.append(x[i])
        prime_y.append(y[i])

plt.plot(
    prime_x,
    prime_y,
    marker="*",     
    linestyle="-",
    linewidth=3,
    markersize=20
)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Draw")
plt.grid()
plt.show()
