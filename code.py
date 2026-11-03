import os
import time
import streamlit as st
from PIL import Image


def main():
    st.set_page_config(page_title="mano", page_icon="🎯", layout="wide")

    st.title("🎯 mano")
    st.header("곧 :blue[10만]!")
    st.header("korea best sniper")
    st.header("올린 영상: 약 110개")

    placeholder = st.empty()
    for n in range(0, 1000, 10):
        placeholder.header(f"명장면: {n}")
        time.sleep(0.01)
    placeholder.header("명장면: 999+")

    st.link_button(
        "마노님 커뮤니티",
        "https://www.youtube.com/@%EB%A7%88%EB%85%B8%EC%9D%98%EB%A1%9C%EB%B8%94%EB%A1%9D%EC%8A%A4/community",
        type="primary",
    )
    st.divider()

    if st.button("응원"):
        st.balloons()

    if os.path.exists("channels4_profile.png"):
        profile = Image.open("channels4_profile.png")
        st.image(profile, caption="마노님 프로필", width=300)

    st.subheader("명장면 모음")

    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        st.caption("영상 1")
        st.video("https://www.youtube.com/watch?v=GTp74UZcDpE")
    with c2:
        st.caption("영상 2")
        st.video("https://www.youtube.com/watch?v=yFhTDOUkGos")
    with c3:
        st.caption("영상 3")
        st.video("https://www.youtube.com/watch?v=pr_XZBqUOOg")

    st.write("")

    c4, c5, c6 = st.columns(3, gap="large")
    with c4:
        st.caption("영상 4")
        st.video("https://www.youtube.com/watch?v=7lEmDZD8kH8")
    with c5:
        st.caption("영상 5")
        st.video("https://www.youtube.com/watch?v=ZowXyGt2508")
    with c6:
        st.caption("영상 6")
        st.video("https://www.youtube.com/watch?v=gUhxr192zes", start_time=8)

    st.divider()
    st.subheader("응원 한마디")
    word = st.text_input("마노님께 하고 싶은 말을 적고 엔터를 눌러주세요")
    if word:
        st.subheader(word)


main()
