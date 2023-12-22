import streamlit as st
import pandas as pd
import random

# Define the path to your CSV file (assuming it's in the same directory as your code)
csv_file_path = "file.csv"

# Load the CSV file
@st.cache_data
def load_data():
    data = pd.read_csv(csv_file_path, delimiter=";")
    return data

st.title("IQRA")
st.markdown("Visit my website at [www.lintanggilang.site](https://www.lintanggilang.site)")

data = load_data()
n_rows = data.shape[0]

if "selected_indices" not in st.session_state:
    st.session_state.selected_indices = []

if "current_index" not in st.session_state:
    st.session_state.current_index = None

if st.button("Reset"):
    st.session_state.selected_indices = list(range(n_rows))
    st.session_state.current_index = None

if st.button("Next"):
    selected_indices = st.session_state.selected_indices
    n_rows = len(selected_indices)
    if n_rows == 0:
        st.write("Semua baris telah ditampilkan. Klik Reset untuk memulai lagi.")
    else:
        random_index = random.choice(selected_indices)
        st.session_state.current_index = random_index
        selected_indices.remove(random_index)

if st.session_state.current_index is not None:
    st.write(f"{n_rows}")
    current_index = st.session_state.current_index
    st.write(f"{data['Question'][current_index]}")
    st.markdown(f'<div style="font-size: 20px; font-weight: bold;">{data["English"][current_index]}</div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(f"{data['bahasa'][current_index]}")

