import seaborn as sns
import matplotlib.pyplot as plt

data = [1, 2, 1, 3, 3, 1, 4, 2]

plt.hist(data, bins=8)
plt.xlabel('Number of days')
plt.title('Distribution of classroom visits in the first week ' + 
          'for students who do not pass the subway project')

plt.hist(data, bins=8)
plt.xlabel('Number of days')
plt.title('Distribution of classroom visits in the first week ' + 
          'for students who pass the subway project')


plt.show()