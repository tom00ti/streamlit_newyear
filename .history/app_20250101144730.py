import streamlit as st
from PIL import Image

st.title(' 謹賀新年 from Papa ')
st.caption('これは、Eriちゃんと、Mamaに向けた web 年賀状です。')
st.subheader('メッセージ')
st.text('あけましておめでとうございます。今年も、えりちゃんとママにとって良い年であるよう、祈っています。')

# 画像

image = Image.open('Dragon_and_father.webp')
st.image(image, width = 500)

st.video('https://www.youtube.com/watch?v=DUrFgz1ZA58')



# オートリロードせず、ボタンが押されたときだけリロードする。
#with st.form(key='message_form'):
    # テキストボックス
#    message = st.text_input('メッセージがあれば入力してください')
    # セレクトボックス
    age_category = st.selectbox(
        '送信する人',
        ('Eri', 'Mama')
    )

    # ボタン
#    submit_btn = st.form_submit_button('送信')
#    cancel_btn = st.form_submit_button('キャンセル')

#   submit_btn = st.button('送信')
#   cancel_btn = st.button('キャンセル')
"""
    if submit_btn :
        st.text(f'メッセージが送信されました！ "{message}"')
        st.text(f'送信者： {age_category}')
"""
        
#print(f'submit_btn: {submit_btn}')
#print(f'cancelt_btn: {cancel_btn}')
#print(message)


code = """

import streamlit as st

st.title('この年賀状は、streamlitで作成しています。')

"""

st.code(code, language='python')

