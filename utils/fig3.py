import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

def fig3(placeholder, options):
    df = pd.read_excel('data.xlsx', sheet_name = 'Confectionery - Revenue - Unpiv')

    # options = placeholder.multiselect(
    #     "Select a year",
    #     ['Past', 'Today', 'Future'],
    #     ['Today'],
    #     key='fig3'
    # )
    df['Year'] = df['Year'].astype(str)
    selected_df = df[df['Year'].isin(options)]

    all_selected_df_rev = selected_df.groupby(['Confectionery', 'Year'])['YoY Revenue Change (%)'].mean().reset_index()
    # all_selected_df_rev['status'] = pd.Categorical(all_selected_df_rev['status'], categories=['past', 'today', 'future'], ordered=True)
    all_selected_df_rev = all_selected_df_rev[all_selected_df_rev['Confectionery'] != 'Total']
    # color_discrete_map = {
    #     'past': '#F0CF65',
    #     'today': '#93B5C6',
    #     'future': '#BD4F6C'
    # }

    fig = px.bar(
        all_selected_df_rev,
        x='Confectionery',
        y='YoY Revenue Change (%)',
        color='Year',
        barmode='group',
        title='% Percentage Revenue Change by Confectionery Type and Year',
        labels={'YoY Revenue Change (%)': 'Yearly Revenue Change (%)', 'Confectionery': 'Confectionery Type'},
        # category_orders={'status': ['past', 'today', 'future']},
        # color_discrete_map=color_discrete_map
    )
    return fig