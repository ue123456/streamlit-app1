import streamlit as st
import numpy as np
import pickle

# 加载模型
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("老年人呼吸系统疾病就诊预测工具")
st.markdown("根据滞后2周的气象条件，预测就诊人数。")

# 输入界面
avg_temp = st.slider("平均气温 (℃)", -5.0, 40.0, 10.0, 0.1)
rh = st.slider("相对湿度 (%)", 10.0, 100.0, 70.0, 0.5)

if st.button("预测就诊人数"):
    X_input = np.array([[avg_temp, rh]])
    pred = model.predict(X_input)[0]
    st.success(f"预计老年人呼吸系统疾病就诊人数为：{int(pred)} 人")

st.caption("本工具仅用于科研及趋势预测参考，不作为临床诊断依据。")
