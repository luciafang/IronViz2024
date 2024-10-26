import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

def fig1(placeholder):
    df = pd.read_excel('data.xlsx', sheet_name = 'Confectionery - Revenue - Unpiv')
    df['Year'] = df['Year'].astype(str)
    # with placeholder.popover('Select a year'):
    options = placeholder.multiselect(
            "Select Years",
            ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029'],
            ['2023', '2024', '2025'],
            key='fig1'
        )


    selected_df = df[df['Year'].isin(options)]

    all_selected_df_rev = selected_df.groupby(['Confectionery', 'Year'])['Average Revenue per Capita ($USD)'].mean().reset_index()
    all_selected_df_rev = all_selected_df_rev[all_selected_df_rev['Confectionery'] != 'Total']


    fig = px.bar(
        all_selected_df_rev,
        x='Confectionery',
        y='Average Revenue per Capita ($USD)',
        color='Year',
        barmode='group',
        title='Average Revenue per Capita by Confectionery Type and Year',
        labels={'Average Revenue per Capita ($USD)': 'Average Spend per Person ($USD)',
                'Confectionery': 'Confectionery Type'},
        # category_orders={'status': ['past', 'today', 'future']},
        # color_discrete_map=color_discrete_map
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        legend_font_size=16,
        legend_title_font_size=16,
        xaxis=dict(tickfont=dict(size=16)),
        yaxis=dict(tickfont=dict(size=16)),
    )
    return fig, options