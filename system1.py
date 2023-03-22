import altair as alt
import pandas as pd
import streamlit as st

#   数据集路径
earthquake_data = pd.read_csv('Significant Earthquake Dataset 1900-2023.csv')

# 加载数据
earthquake_data = pd.read_csv('Significant Earthquake Dataset 1900-2023.csv')

# 由于无法访问您的数据，我们将创建一个虚拟数据集
earthquake_data = pd.read_csv('Significant Earthquake Dataset 1900-2023.csv')

# 预处理数据集
earthquake_data['Year'] = pd.to_datetime(earthquake_data['Time']).dt.year.astype(int)

# 定义应用布局
st.title("Earthquakes Analysis")

decade_start = st.sidebar.slider("Decade Start", min_value=earthquake_data['Year'].min(), max_value=earthquake_data['Year'].max()-9, step=10)
magnitude_greater_than_6 = st.sidebar.checkbox("Magnitude Greater Than 6")
depth_greater_than_100 = st.sidebar.checkbox("Depth Greater Than 100")

decade_end = decade_start + 9
filtered_data = earthquake_data[(earthquake_data['Year'] >= decade_start) & (earthquake_data['Year'] <= decade_end)]

if magnitude_greater_than_6:
    filtered_data = filtered_data[filtered_data['Mag'] > 6]

if depth_greater_than_100:
    filtered_data = filtered_data[filtered_data['Depth'] > 100]

# 条形图
bar_chart = alt.Chart(filtered_data).mark_bar().encode(
    alt.X("Year:O", title="Year"),
    alt.Y("count(ID):Q", title="Number of Earthquakes"),
    tooltip=["Year:O", "count(ID):Q"]
).properties(
    title=f"Number of Significant Earthquakes per Year ({decade_start}-{decade_end})",
    width=600,
    height=300
)

# 散点图
scatter_plot = alt.Chart(filtered_data).mark_circle().encode(
    alt.X("Depth:Q", title="Depth (km)", scale=alt.Scale(zero=False)),
    alt.Y("Mag:Q", title="Magnitude", scale=alt.Scale(zero=False)),
    color="Year:O",
    tooltip=["Depth:Q", "Mag:Q", "Year:O"]
).properties(
    title=f"Earthquake Depth vs. Magnitude ({decade_start}-{decade_end})",
    width=600,
    height=300
).interactive()

st.altair_chart(bar_chart & scatter_plot)
