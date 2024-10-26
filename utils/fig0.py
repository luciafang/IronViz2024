import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

def fig0():
    df = pd.read_excel('data.xlsx', sheet_name = 'Confectionery - Revenue - Unpiv')
    df['Year'] = df['Year'].astype(str)
    df = df[df['Confectionery'] != 'Total']
    # st.write(df)

    # all_selected_df_rev = df.groupby(['Confectionery', 'Year'])['YoY Revenue Change (%)', 'Average Revenue per Capita ($USD)'].mean().reset_index()
    # all_selected_df_rev = all_selected_df_rev[all_selected_df_rev['Confectionery'] != 'Total']
    # st.write(all_selected_df_rev)


    cols = st.columns(len(df.Confectionery.unique()))
    for col, conf in zip(cols, df.Confectionery.unique()):
        conf_df = df[(df['Confectionery'] == conf) & (df['Year'] == str(datetime.datetime.now().year))]
        conf_df_prev = df[(df['Confectionery'] == conf) & (df['Year'] == str(datetime.datetime.now().year-1))]
        curr_per_person = conf_df['Average Revenue per Capita ($USD)'].values[0]
        prev_per_person = conf_df_prev['Average Revenue per Capita ($USD)'].values[0]
        col.metric(f"{conf}",
                   f"${curr_per_person}/person (2024)",
                   # f"{conf_df['YoY Revenue Change (%)'].values[0]}% from 2023")
                   f"{round((curr_per_person-prev_per_person)/prev_per_person*100, 2)}% from 2023")
        # col.metric("Wind", "9 mph", "-8%")
        # col.metric("Humidity", "86%", "4%")

    return