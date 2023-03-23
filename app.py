import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import openai
openai.organization = "org-S5gH3WeHfvGZpVvdFmF1ErTu"
openai.api_key      = "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"

def Ask_ChatGPT(message):
    
    # 応答設定
    
    completion = openai.ChatCompletion.create(
                 model    = "gpt-3.5-turbo",     # モデルを選択
                 messages = [{
                            "role":"user",
                            "content":message,   # メッセージ 
                            }],
    
                 max_tokens  = 100,             # 生成する文章の最大単語数
                 n           = 1,                # いくつの返答を生成するか
                 stop        = None,             # 指定した単語が出現した場合、文章生成を打ち切る
                 temperature = 0.5,              # 出力する単語のランダム性（0から2の範囲） 0であれば毎回返答内容固定
    )
    
    # 応答
    response = completion.choices[0].message.content
    
    # 応答内容出力
    return response

# 質問内容
message = st.text_input('インプットボックス')

if st.button('質問する'):
    # ChatGPT起動
    res = Ask_ChatGPT(message)

    # 出力
    st.write(res)

else:
    st.write('Waiting')







