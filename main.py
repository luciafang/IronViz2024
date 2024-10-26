import streamlit as st

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
st.title('CMU')



left, right = st.columns(2)
fig1, options1 = fig1(left)
fig2, options2 = fig2(right)
left.plotly_chart(fig1, use_container_width=True)
right.plotly_chart(fig2, use_container_width=True)
left.plotly_chart(fig3(left, options1), use_container_width=True)
# right.plotly_chart(fig4(right, options2), use_container_width=True)

