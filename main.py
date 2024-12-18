import streamlit as st

from utils.fig0 import fig0
from utils.fig1 import fig1
from utils.fig2 import fig2
from utils.fig3 import fig3
from utils.fig4 import fig4

st.set_page_config(
    page_title="IronViz - LuciaFang",
    page_icon="🍭",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.header('Optimizing Confectionery Restocking using Forecasted Revenue in the US')
st.write('')
st.write('')
st.write('')

fig0()
st.write('')
st.write('')
st.write('')
left, right = st.columns(2)
left_container = left.container(border=True)
right_container = right.container(border=True)
fig1, options1 = fig1(right_container)
fig2, options2 = fig2(left_container)

left_container.plotly_chart(fig2, use_container_width=True)
right_container.plotly_chart(fig1, use_container_width=True)
# left.plotly_chart(fig3(left, options1), use_container_width=True)
# right_container.plotly_chart(fig4(right_container, options2), use_container_width=True)
if st.button("Reveal Actionable Insights"):
    with st.chat_message("user"):

        st.markdown('''
        - **Inventory Adjustment**: 
            - Increase stock for all products, especially for **Pastry**.<br>   <!-- Add space here -->
        - **Targeted Promotions**: 
            - Prioritize promotional efforts for **high-growth items** (Pastry and Chocolate Confectionery)
            - Deprioritize **Ice Cream** restock. 
            - Bundle items or offer discounts to maximize **revenue potential**
        ''', unsafe_allow_html=True)
