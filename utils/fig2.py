import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns

def fig2(placeholder):
    df = pd.read_excel('data.xlsx', sheet_name = 'Confectionery - Revenue - Unpiv')
    options = placeholder.radio(
        "Select a Confectionery Type",
        ['Chocolate Confectionery', 'Ice Cream', 'Preserved Pastry Goods & Cakes', 'Sugar Confectionery'],
        index=2,
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
        'Preserved Pastry Goods & Cakes': '#89CD69',
        'Sugar Confectionery': '#93B5C6'
    }

    fig = px.line(
        selected_df,
        x='Year',
        y='Average Revenue per Capita ($USD)',
        color='Confectionery',
        # title= f'Average Dollar Spend per Person History and Forecast by {options}',
        labels={'Average Revenue per Capita ($USD)': 'Average Spend/Person ($USD)', 'Year': 'Year'},
        line_shape='linear',
        category_orders={'Confectionery': ['Chocolate Confectionery', 'Ice Cream', 'Preserved Pastry Goods & Cakes',
                                           'Sugar Confectionery']},
        color_discrete_map=color_discrete_map
    )

    fig.update_traces(mode='lines+markers', line=dict(width=3), marker=dict(size=12))
    fig.update_layout(
        title=dict( text= f'Average Spent per Person Over Years: {options}',
                    font=dict( size=14,
                               color='black',
                               family='Arial',
                               weight='normal')),
        xaxis_title_font_size=12,
        yaxis_title_font_size=12,
        legend_font_size=12,
        legend_title_font_size=12,
        xaxis=dict(tickfont=dict(size=12), tickangle=45),
        yaxis=dict(tickfont=dict(size=12)),
    )
    return fig, options