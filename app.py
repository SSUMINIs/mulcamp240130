# -*- coding:utf-8 -*-

import streamlit as st
import seaborn as sns

def main():
    st.title("Hello World on Streamlit.io")
    st.write(st.__version__)

    df = sns.load_dataset('iris')
    st.write(df)

if __name__ == "__main__":
    main()