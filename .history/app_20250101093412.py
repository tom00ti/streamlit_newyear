import streamlit as st
st.title('サプーアプリ')
st.caption('これはサプーの動画テストアプリです')
st.subheader('自己紹介')
st.text('pythonに関する情報をYoutube上で発信している、サプーさんのプラクティスコードです。')

code = """

import streamlit as st

st.title('サプーアプリ')

"""

st.code(code, language='python')