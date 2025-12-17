import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


data=pd.read_csv("WineQT.csv")
print(data.shape)
print(data.head())
print(data.describe())
print(data.columns)
print(data.isna().sum())
print("unique values ",data["quality"].unique())
data.drop_duplicates(inplace=True)
print(data[data.duplicated()]) #not repeated


# Wine quality classes frequancy
sns.countplot(x= data['quality'])
plt.xlabel('Wine quality')
plt.ylabel('Frequancy')
plt.title('Wine quality classes')
plt.show()

#correlation
print(data.corr())
plt.figure(figsize=(10,10))
sns.heatmap(data.corr(),annot=True)
plt.show()

print(data.groupby("quality").mean())

print(data.groupby("quality")["fixed acidity"].mean())
#Relation between volatile acidity vs quality
sns.lineplot(x=data["volatile acidity"],y=data["quality"],color="b")
plt.show()

#Relation between citric acid vs quality
plot = plt.figure(figsize= (5,5))
sns.barplot(x=data["quality"] ,y= data["citric acid"])
plt.title('citric acid vs quality')

data.quality.value_counts().plot(kind="bar")
plt.show()

sns.histplot(data["pH"])
#sns.pairplot(data,markers=["--"])
#plt.show()

sns.scatterplot(x=data["pH"],y=data["alcohol"],hue=data["quality"])
plt.show()


columns=data.columns

fig,ax=plt.subplots(4,4,figsize=(16,15))
ax=ax.flatten()
for i,column in enumerate(columns):
   sns.kdeplot(data=data,hue="quality",x=column,ax=ax[i])


ax[i].set_title(f"{column} distribution")
ax[i].set_xlabel(None)

for i in range(i+1,len(ax)):
    ax[i].axis("off")

plt.show()










