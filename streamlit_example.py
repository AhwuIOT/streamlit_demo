import time

import streamlit as st

import numpy as np
import pandas as pd

st.title('Streamlit 入門')

st.write("建立表格")
df = pd.DataFrame({
    'column1': [1, 2, 3, 4],
    'column2': [10, 20, 30, 40]},
    index=['row1', 'row2', 'row3', 'row4'])

df

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(df)

map_data = pd.DataFrame(
    # np.random.randn(1000, 2) / [50, 50] + [22.6, 120.4],
    [[25.04421767267317, 121.41974104375117]],     columns=['lat', 'lon'])
map_data
st.map(map_data)

if st.button('Click me'):
    st.text('按啥呢?')

option = st.sidebar.selectbox(
    '喜歡什麼水果?',
    ['蘋果', '香蕉', '橘子'])
st.sidebar.text("你的選擇是{}".format(option))