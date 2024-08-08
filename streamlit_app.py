import streamlit as st
import openai

# 设置API密钥
openai.api_key = 'sk-ab8lTXmVOuGeGiid01E43e8bB0Ac45D68641A381387d64C9'

# 页面标题
st.title("个性化数学学习材料生成器")

# 输入主题
topic = st.text_input("输入你感兴趣的数学主题：", "代数")

# 选择难度
difficulty = st.selectbox("选择难度等级：", ("初级", "中级", "高级"))

# 选择个性化偏好
focus = st.radio("你更关注以下哪方面？", ("概念解释", "例题演练"))

# 生成按钮
if st.button("生成学习材料"):
    # 根据用户输入生成学习材料
    prompt = f"为主题'{topic}'生成{difficulty}难度的数学学习材料，侧重于{focus}。"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    
    content = response.choices[0].text.strip()
    st.write("### 生成的学习材料：")
    st.write(content)
    
    # 生成互动问题
    st.write("### 试试回答以下问题：")
    questions = [
        {
            "question": f"关于{topic}，以下哪个陈述是正确的？",
            "answers": [
                {"answer": "选项A", "correct": False},
                {"answer": "选项B", "correct": True},
                {"answer": "选项C", "correct": False},
                {"answer": "选项D", "correct": False}
            ]
        }
    ]
    
    for q in questions:
        st.write(q["question"])
        for ans in q["answers"]:
            if st.button(ans["answer"]):
                if ans["correct"]:
                    st.success("正确!")
                else:
                    st.error("错误，再试试。")

# 跟踪学习进度
st.write("### 学习进度")
progress = st.progress(0)
