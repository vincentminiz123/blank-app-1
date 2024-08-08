# app.py

import streamlit as st
import openai

# 设置OpenAI API密钥
openai.api_key = "your_openai_api_key"

# 定义函数以生成个性化学习材料
def generate_learning_material(student_info, topic):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"为{student_info}的学生生成关于{topic}的数学学习材料，包含练习题和详细解答。",
        max_tokens=500
    )
    return response.choices[0].text.strip()

# 使用Streamlit创建用户界面
st.title("个性化数学学习材料生成器")

# 用户输入部分
student_info = st.text_input("请输入学生信息（例如年级、学习水平等）")
topic = st.text_input("请输入学习主题（例如代数、几何等）")

# 当用户点击按钮时，生成学习材料
if st.button("生成学习材料"):
    if student_info and topic:
        material = generate_learning_material(student_info, topic)
        st.write("生成的学习材料：")
        st.write(material)
    else:
        st.write("请提供学生信息和学习主题。")
