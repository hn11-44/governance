import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    data = pd.read_csv('governance_df.csv')
    return data

# Load data
data = load_data()

st.title('Global Governance Dashboard')

# Dropdown menu for year selection
years = data['Year'].unique()
selected_year = st.selectbox('Select Indicator', sorted(years))


# Dropdown menu for variable selection
variables = ['Voice and Accountability', 'Political Stability', 'Regulatory Quality', 'Rule of Law', 'Effectiveness', 'Control of Corruption', 'Internet Penetration', 'Women in Parliament', 'Female to Male Labor Ratio']
selected_variable = st.selectbox('Select Indicator', variables)

# Filter data for the selected year and country
filtered_data = data[(data['Year'] == selected_year)]

# Create a choropleth map for the selected variable
fig_map = px.choropleth(filtered_data,
                        locations="Country",
                        locationmode="country names",
                        color=selected_variable,
                        hover_name="Country",
                        hover_data={"Year": False, selected_variable: True},
                        color_continuous_scale="Blues",
                        title=f"Global {selected_variable}")
st.plotly_chart(fig_map, use_container_width=True)

# Horizontal bar chart for the selected variable
top_countries = filtered_data.nlargest(10, selected_variable)
fig_bar = px.bar(top_countries,
                 x=selected_variable,
                 y='Country',
                 orientation='h',
                 color=selected_variable,
                 color_continuous_scale="Blues",
                 title=f"Top Countries by {selected_variable}")
fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'})
st.plotly_chart(fig_bar, use_container_width=True)
