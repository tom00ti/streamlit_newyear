import streamlit as st
from PIL import Image

st.title(' 謹賀新年　from Papa ')
st.caption('これは　web　年賀状です。')
st.subheader('メッセージ')
st.text('あけましておめでとうございます。今年はＥｒｉちゃんにとって良い年であるよう、祈っています。')

code = """

import streamlit as st

st.title('この年賀状は、streamlitで作成しています。')

"""

st.code(code, language='python')