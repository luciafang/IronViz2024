import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

def fig4(placeholder, options):
    df = pd.read_excel('data.xlsx', sheet_name = 'Confectionery - Revenue - Unpiv')

    # options = placeholder.multiselect(
    #     "Select a Confectionery Type",
    #     ['Chocolate Confectionery', 'Ice Cream', 'Preserved Pastry Goods & Cakes', 'Sugar Confectionery'],
    #     ['Chocolate Confectionery', 'Ice Cream', 'Preserved Pastry Goods & Cakes', 'Sugar Confectionery'],
    #     key='fig4'
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
        y='YoY Revenue Change (%)',
        color='Confectionery',
        title='Revenue Over Time by Confectionery Type',
        labels={'YoY Revenue Change (%)': 'Yearly Revenue Change (%)', 'Year': 'Year'},
        line_shape='linear',
        category_orders={'Confectionery': ['Chocolate Confectionery',
                                           'Ice Cream', 'Preserved Pastry Goods & Cakes', 'Sugar Confectionery' ] },
        color_discrete_map=color_discrete_map
    )
    return fig