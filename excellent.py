import streamlit as st

st.set_page_config(layout="wide") # 페이지를 넓게 사용하도록 설정

st.title("✨ 우리 아이 영재교육원 준비 도우미 ✨")
st.write("안녕하세요, 팬더입니다! 우리 아이의 빛나는 재능을 위한 영재교육원 준비, 함께 알아봐요! 💖")

st.header("🔍 영재교육원이란?")
st.markdown("""
영재교육원은 특별한 재능과 잠재력을 가진 친구들이
자신의 능력을 더욱 키울 수 있도록 도와주는 교육기관이에요.
보통 초등학교 고학년이나 중학생을 대상으로 하지만,
어릴 때부터 재능을 발견하고 키워주는 것이 중요하답니다!
""")

st.header("📝 영재교육원 입학 과정 (일반적인 경우)")
st.markdown("""
영재교육원에 들어가려면 몇 가지 단계를 거쳐야 해요.
물론 교육원마다 조금씩 다를 수 있으니 참고만 해주세요! 😊

*   **1단계: 선생님 추천**
    *   학교 선생님이 우리 친구의 뛰어난 점을 관찰하고 추천서를 써주세요.
    *   평소에 수업 시간에 적극적으로 참여하고, 궁금한 것을 질문하는 모습이 중요하겠죠?

*   **2단계: 영재성 검사 또는 창의적 문제 해결력 평가**
    *   친구의 영재성과 생각하는 힘을 알아보는 시험을 봐요.
    *   문제를 풀면서 얼마나 새롭고 기발한 아이디어를 내는지,
        얼마나 깊이 있게 생각하는지 등을 평가한답니다!

*   **3단계: 심층 면접 또는 캠프**
    *   선생님들과 직접 만나서 이야기하거나,
        친구들과 함께 과제를 해결하는 캠프에 참여하기도 해요.
    *   이때는 친구의 열정과 잠재력을 보여주는 게 중요해요!
""")

st.header("💡 2학년 친구를 위한 준비 팁!")
st.info("""
지금 2학년이라면, 시험 준비보다는 재능을 발견하고 키워주는 데 집중해야 해요!

*   **다양한 경험:** 코딩, 과학 실험, 독서, 미술 등 여러 활동을 해보면서 어떤 분야에 흥미가 있는지 찾아봐요!
*   **호기심 키우기:** "왜?"라는 질문을 많이 하고, 스스로 답을 찾아보려고 노력하는 습관을 길러주세요.
*   **책과 친해지기:** 다양한 책을 읽으면서 상상력과 지식을 넓히는 건 정말 중요해요!
*   **관찰하고 탐구하기:** 주변의 모든 것을 그냥 지나치지 않고, 자세히 보고 궁금해하는 마음을 키워주세요.
""")

st.subheader("📚 추천 활동")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1516321497487-e288ad7ab135?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="코딩 배우기")
    st.write("논리적 사고력을 키우는 데 최고! ✨")

with col2:
    st.image("https://images.unsplash.com/photo-1532187635607-68b32729e84b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="과학 실험하기")
    st.write("세상의 원리를 탐구하는 즐거움! 🧪")

with col3:
    st.image("https://images.unsplash.com/photo-1521587765099-ef1967727bb3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="다양한 책 읽기")
    st.write("상상력과 지식을 넓히는 보물창고! 📖")

st.markdown("---")
st.write("궁금한 점이 있으면 언제든지 팬더에게 물어봐줘! 😊")
