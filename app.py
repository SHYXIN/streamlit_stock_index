import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


Stock_Market = {
'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],             
'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
'EconomicGrowth_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]        
 }

df = pd.DataFrame(Stock_Market,columns = ['Year','Month','EconomicGrowth_Rate','Unemployment_Rate','Stock_Index_Price'])

x = df[['EconomicGrowth_Rate','Unemployment_Rate']]
y = df['Stock_Index_Price']

lr = linear_model.LinearRegression()
lr.fit(x,y)


st.title("使用线性回归进行股指预测")

st.text(" ")
st.text(" ")
st.text(" ")

st.image('stockindex.jpeg',width=700)

st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

st.subheader("股指与经济增长率的关系")

st.text(" ")
st.text(" ")
st.text(" ")

# 设置中文字体和负号正常显示
plt.rcParams['font.family'] =['SimSun', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(9,6))
plt.xlabel("经济增长率", fontsize=20)
plt.ylabel("股指", fontsize=20)
plt.scatter(df['EconomicGrowth_Rate'],df['Stock_Index_Price'],color='g')
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse',False)
st.pyplot()


st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

st.subheader("股指与失业率的关系")

st.text(" ")
st.text(" ")
st.text(" ")

plt.figure(figsize=(9,6))
plt.xlabel("失业率", fontsize=20)
plt.ylabel("股指", fontsize=20)
plt.scatter(df['Unemployment_Rate'],df['Stock_Index_Price'],color='g')
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse',False)
st.pyplot()

st.text(" ")
st.text(" ")
st.text(" ")

i = st.number_input("请输入经济增长率")
st.text(" ")
st.text(" ")
u = st.number_input("请输入失业率")
st.text(" ")
st.text(" ")

if st.button("预测股指"):
    st.subheader("预测的股指为")
    st.text(lr.predict([[i,u]]))
















