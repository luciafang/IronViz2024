import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

def fig1(placeholder):
    df = pd.read_excel('data.xlsx', sheet_name = 'Confectionery - Revenue - Unpiv')
    df['Year'] = df['Year'].astype(str)
    with st.sidebar:
        options = st.multiselect(
            "Select a year",
            ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029'],
            ['2023', '2024', '2025'],
            key='fig1'
        )

    selected_df = df[df['Year'].isin(options)]

    all_selected_df_rev = selected_df.groupby(['Confectionery', 'Year'])['Revenue in Billions ($USD)'].mean().reset_index()
    all_selected_df_rev = all_selected_df_rev[all_selected_df_rev['Confectionery'] != 'Total']


    fig = px.bar(
        all_selected_df_rev,
        x='Confectionery',
        y='Revenue in Billions ($USD)',
        color='Year',
        barmode='group',
        title='Revenue by Confectionery Type and Year',
        labels={'Revenue in Billions ($USD)': 'Revenue (Billions $USD)', 'Confectionery': 'Confectionery Type'},
        # category_orders={'status': ['past', 'today', 'future']},
        # color_discrete_map=color_discrete_map
    )
    return fig, options