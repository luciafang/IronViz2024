import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns

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

    husl_color_map = {
        '2018': '#FF6F61',  # Coral
        '2019': '#6B5B93',  # Purple
        '2020': '#88B04B',  # Green
        '2021': '#F7CAC9',  # Light Pink
        '2022': '#92A8D1',  # Light Blue
        '2023': '#955251',  # Burgundy
        '2024': '#B4B400',  # Olive
        '2025': '#E3C9C8',  # Light Gray
        '2026': '#FFB400',  # Yellow
        '2027': '#D35400',  # Orange
        '2028': '#4B8BBE',  # Blue
        '2029': '#AAB9A6',  # Sage Green
    }

    fig = px.bar(
        all_selected_df_rev,
        x='Confectionery',
        y='Average Revenue per Capita ($USD)',
        color='Year',
        barmode='group',
        title='Average Revenue per Capita by Confectionery Type and Year',
        labels={'Average Revenue per Capita ($USD)': 'Average Spend per Person ($USD)',
                'Confectionery': 'Confectionery Type'},
        color_discrete_map=husl_color_map  # Apply the color mapping
    )
    color_discrete_map = {
        'Chocolate Confectionery': '#BD4F6C',
        'Ice Cream': '#F0CF65',
        'Preserved Pastry Goods & Cakes': '#89CD69',
        'Sugar Confectionery': '#93B5C6'
    }
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        legend_font_size=16,
        legend_title_font_size=16,
        xaxis_title='',
        xaxis=dict(
            tickfont=dict(size=16),
            tickvals=all_selected_df_rev['Confectionery'],  # Set the tick values to your x-axis categories
            ticktext=[
                f"<span style='color:{color_discrete_map[c]}';>{c}</span>" for c in all_selected_df_rev['Confectionery']
            ]  # Color the tick labels using HTML span
        ),
        yaxis=dict(tickfont=dict(size=16)),
    )
    return fig, options