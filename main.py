import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Tomatoes", "Mangoes", "Oranges", "Apples"]
myexplode = [0.2, 0, 0.4,  0.1]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 