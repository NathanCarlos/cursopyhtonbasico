data = [1, 2, 1, 3, 3, 1, 4, 2]
import numpy as np
import matplotlib.pyplot as plt

def describe_data(data):
    print 'Mean:', np.mean(data)
    print 'Standard deviation:', np.std(data)
    print 'Minimum:', np.min(data)
    print 'Maximum:', np.max(data)
    plt.hist(data, bins=20)
    plt.title('Grafico de Teste')
    plt.show()

describe_data(data)