import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from currency_converter import CurrencyConverter as cc

cs=cc()
df=pd.read_csv('insurance.csv')  #import insurance.csv file from the repository first for this to work

def data_split(data,ratio):
    np.random.seed(42)
    shuffle=np.random.permutation(len(data))
    testsize=int(len(data)*ratio)
    train_ind=shuffle[testsize:]
    test_ind=shuffle[:testsize]
    return data.iloc[train_ind],data.iloc[test_ind]
train,test=data_split(df,0.2)
X_train=train[['age','sex','bmi','children','smoker','region']].to_numpy()
Y_train=train[['charges']].to_numpy()
X_test=test[['age','sex','bmi','children','smoker','region']].to_numpy()
Y_test=test[['charges']].to_numpy()

clf=LinearRegression()
clf.fit(X_train,Y_train)
age=float(input('Age:'))
Gender=input('F or M:')
if Gender.lower()=='f':
    s=0
elif Gender.lower()=='m':
    s=1
else:
    s=1
h=float(input('Height(in cm):'))
w=float(input('Weight(kg):'))
bmi=w*10000/h**2
chil=int(input('No of children:'))
sm=input('Are you a smoker(y/n):')
if sm.lower()=='y':
    tt=1
elif sm.lower()=='n':
    tt=0
else:
    tt=0
print("Enter your region of living:")
print("Type 0 if you are from southwest")
print("Type 1 if you are from southeast")
print("Type 2 if you are from northwest")
print("Type 3 if you are from northeast")
reg=int(input('Choice:'))
ans=[age,s,bmi,chil,tt,reg]

ss=clf.predict([ans])
PS=cs.convert(ss[0][0].round(3),'USD','INR')
print('Insurance is:', PS, 'Indian Rupees')
