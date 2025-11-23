import numpy as np
import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_abline

# Load X and y from files
X = np.loadtxt("X.txt")
y = np.loadtxt("y.txt")

# Build design matrix
Xmat = np.column_stack((np.ones(len(X)), X))

# Compute coefficients via matrix formula
beta = np.linalg.inv(Xmat.T @ Xmat) @ (Xmat.T @ y)
a = beta[0]
b = beta[1]

print("Intercepto (a):", a)
print("Inclinação (b):", b)

# Plot
df = pd.DataFrame({"x": X, "y": y})
plot = (
    ggplot(df, aes("x", "y"))
    + geom_point()
    + geom_abline(intercept=a, slope=b)
)

plot.save("regressao.png")
print("Gráfico salvo como regressao.png")
