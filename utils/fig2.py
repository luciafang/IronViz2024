import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

def fig2(placeholder):
    df = pd.read_excel('data.xlsx', sheet_name = 'Confectionery - Revenue - Unpiv')
    options = placeholder.radio(
        "Select a Confectionery Type",
        ['Chocolate Confectionery', 'Ice Cream', 'Preserved Pastry Goods & Cakes', 'Sugar Confectionery'],
        index=3,
        horizontal=True,
        key='fig2'
    )
    # options = placeholder.ratio(
    #     "Select a Confectionery Type",
    #     ['Chocolate Confectionery', 'Ice Cream', 'Preserved Pastry Goods & Cakes', 'Sugar Confectionery'],
    #     ['Chocolate Confectionery', 'Ice Cream', 'Preserved Pastry Goods & Cakes', 'Sugar Confectionery'],
    #     key = 'fig2'
    # )

    selected_df = df[df['Confectionery'] == options]

    color_discrete_map = {
        'Chocolate Confectionery': '#BD4F6C',
        'Ice Cream': '#F0CF65',
        'Preserved Pastry Goods & Cakes': '#93B5C6',
        'Sugar Confectionery': '#89CD69'
    }

    fig = px.line(
        selected_df,
        x='Year',
        y='Average Revenue per Capita ($USD)',
        color='Confectionery',
        title='Average Revenue per Capita Forecast by Confectionery Type',
        labels={'Average Revenue per Capita ($USD)': 'Average Spend per Person ($USD)', 'Year': 'Year'},
        line_shape='linear',
        category_orders={'Confectionery': ['Chocolate Confectionery', 'Ice Cream', 'Preserved Pastry Goods & Cakes',
                                           'Sugar Confectionery']},
        color_discrete_map=color_discrete_map
    )

    fig.update_traces(mode='lines+markers', line=dict(width=3), marker=dict(size=12))
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