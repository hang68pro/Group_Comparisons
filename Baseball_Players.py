# Group comparisons 
# Reading data and summary statistics
import pandas as pd
mlb = pd.read_csv('/Users/hangtran/Desktop/Group_Comparisons/Group_Comparisons/mlb.csv')
print(mlb.head())
print('Shape',mlb.shape)
print(mlb.describe())

# Plotting 
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
ax1.boxplot([mlb['height']])
ax1.set_ylabel('Height (Inches)')
ax1.set_xlabel('MLB Player Heights')
plt.xticks([1], ['Full Population'])
plt.show()
# Minimum value ~67, max value ~83, median ~74 and outliers

# Random samples
sample1 = mlb.sample(n = 30, random_state=8675309)
sample2 = mlb.sample(n = 30, random_state= 1729)
sample3 = [71, 72, 73, 74, 74, 76, 75, 75, 75, 76, 75, 77, 76, 75, 77, 76, 75, 76, 76, 75, 75, 81, 77, 75, 77, 75, 77, 77, 75, 75]
import numpy as np
fig1, ax1 = plt.subplots()
ax1.boxplot([mlb['height'], sample1['height'], sample2['height'], np.array(sample3)])
ax1.set_ylabel('Height (Inches)')
plt.title('MLB Player Heights')
plt.xticks([1, 2, 3, 4], ['Full Population', 'Sample 1', 'Sample 2', 'Sample 3'])
plt.show()
print('Sample 1 mean player height', np.mean(sample1['height']))

# Differences between sample data
alldifferences = []
for i in range(1000):
    newsample1 = mlb.sample(n = 30, random_state=i*2)
    newsample2 = mlb.sample(n = 30, random_state=i*2 + 1)
    alldifferences.append(newsample1['height'].mean() - newsample2['height'].mean())
print(alldifferences[0:10])

import seaborn as sns
sns.set()
ax = sns.displot(alldifferences).set_titles('Differences Between Sample Means')
plt.xlabel('Difference Between Means (Inches)')
plt.ylabel('Relative Frequency')
plt.show()
# sample1 and sample2 difference of 0.6 
# sample1 and sample3 difference of 1.6

# How many of our differences have magnitude greater than or equal to 1.6 or 0.6
largedifferences = [diff for diff in alldifferences if abs(diff) >= 1.6]
print(len(largedifferences))
smallldifferences = [diff for diff in alldifferences if abs(diff) >= 0.6]
print(len(smallldifferences))
# p-values (8/1000) and (314/1000) 

# Hypothesis Testing t-test
# H0: sample1 and sample2 random samples from same population
# H1: sample1 and sample2 are not random samples from same population
import scipy.stats
scipy.stats.ttest_ind(sample1['height'], sample2['height'])
# p-value = 0.282 > alpha = 0.05 so no evidence to reject the null hypothesis
# t-test above parametric
# sample mean bell curve
# variances of the groups identical
# two groups independent

# Nonparametric test Mann-Whitney U test (Wilcoxon rank test)
# population mean not bell curve
scipy.stats.mannwhitneyu(sample1['height'], sample2['height'])
# p-value = 0.389

