import streamlit as st
import logic
import os
import json
from datetime import datetime
from zoneinfo import ZoneInfo

# items = []

# login requirement
if not st.session_state.get("logged_in", False):
    st.error("Please login first!")
    st.switch_page("main.py")
    st.stop()

st.title("Stock Take Page")

# intialize json data
if not os.path.exists("stock.json"):
    intial_data = logic.initialize_json()
    with open("stock.json", "w") as f:
        json.dump(intial_data, f, indent=4)

# User able to add or remove item in data by button "Add" and "Remove"
new_item = st.text_input("Add Or Remove Item")
col5, col6, col7 = st.columns([1, 1, 5])
with col5:
    add = st.button("Add", use_container_width=True)
with col6:
    remove = st.button("Remove", use_container_width=True)
if add:
    logic.add_item(new_item)
if remove:
    logic.remove_item(new_item)

# read all the item in json file
with open("stock.json", "r") as f:
    d = json.load(f)
    items = list(d["7"]["inventory"].keys())

# update session
st.subheader("Update")
col1, col2, col3, col4 = st.columns([1, 4, 2, 1])
with col1:
    floor = st.selectbox("Floor", options= logic.floors)
with col2:
    item = st.selectbox("Stock", options=items)
with col3:        
    stockLevel = st.selectbox("Stock Level in %", options= logic.quantity)
with col4:
    st.markdown("")
    st.markdown("")
    update = st.button("Update")
if update:
    currTime = datetime.now(ZoneInfo("America/Halifax")).strftime("%D, %H:%M:%S")
    logic.update_stock(floor, item, stockLevel, currTime)
