import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')
flights=sns.load_dataset('flights')

print(tips.head())
print(flights.head())
fp=flights.pivot_table(index='month',columns='year',values='passengers')
#print(sns.heatmap(fp))
#print(sns.heatmap(fp,cmap='magma'))
#print(sns.heatmap(fp,cmap='magma',linewidths=3))
print(sns.heatmap(fp,cmap='coolwarm',linewidths=3,linecolor='black'))
plt.tight_layout()
plt.show()









