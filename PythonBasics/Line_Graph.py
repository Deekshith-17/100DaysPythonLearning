import matplotlib.pyplot as plt
X = list(range(1, 11))
Y=[i**2 for i in X]
plt.plot(X,Y,marker="o",label="Y=X^2")
plt.title(" Relationship Between X and Y(Y=X^2)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()

