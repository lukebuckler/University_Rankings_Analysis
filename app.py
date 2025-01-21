# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Global University Rankings Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Add custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stPlotlyChart {
        background-color: white;
        border-radius: 5px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# Load and prepare data
@st.cache_data
def load_data():
    df = pd.read_csv('top universities.csv')
    return df

# Create visualizations
def create_world_map(df):
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']
    
    fig = px.choropleth(
        country_counts,
        locations='Country',
        locationmode='country names',
        color='Count',
        hover_name='Country',
        color_continuous_scale='Viridis',
        title='Global Distribution of Top Universities'
    )
    
    fig.update_layout(
        title_x=0.5,
        geo=dict(showframe=False),
        height=500
    )
    
    return fig

def create_top_countries_chart(df, num_countries):
    top_countries = df['Country'].value_counts().head(num_countries)
    
    fig = px.bar(
        x=top_countries.values,
        y=top_countries.index,
        orientation='h',
        title=f'Top {num_countries} Countries by Number of Universities',
        labels={'x': 'Number of Universities', 'y': 'Country'}
    )
    
    fig.update_layout(height=500)
    return fig

def create_ranking_distribution(df):
    fig = px.histogram(
        df,
        x='Global Rank',
        nbins=50,
        title='Distribution of Global Rankings',
        labels={'Global Rank': 'Global Rank', 'count': 'Number of Universities'}
    )
    
    fig.update_layout(height=400)
    return fig

def create_excellence_clusters(df):
    df['Ranking_Cluster'] = pd.cut(
        df['Global Rank'],
        bins=[0, 100, 500, 1000, 5000, float('inf')],
        labels=['Elite (1-100)', 'Premier (101-500)', 
               'Distinguished (501-1000)',
               'Notable (1001-5000)', 'Emerging (5000+)']
    )
    
    cluster_counts = df['Ranking_Cluster'].value_counts()
    
    fig = px.bar(
        x=cluster_counts.index,
        y=cluster_counts.values,
        title='Distribution of Universities Across Excellence Clusters',
        labels={'x': 'Excellence Cluster', 'y': 'Number of Universities'}
    )
    
    fig.update_layout(
        xaxis_tickangle=45,
        height=400
    )
    
    return fig

def create_top_cities_chart(df, num_cities):
    top_cities = df['City'].value_counts().head(num_cities)
    
    fig = px.bar(
        x=top_cities.index,
        y=top_cities.values,
        title=f'Top {num_cities} Cities by Number of Universities',
        labels={'x': 'City', 'y': 'Number of Universities'}
    )
    
    fig.update_layout(
        xaxis_tickangle=45,
        height=400
    )
    
    return fig

# Main dashboard
def main():
    # Load data
    df = load_data()
    
    # Header
    st.title("🎓 Global University Rankings Dashboard")
    st.markdown("---")
    
    # Sidebar filters
    st.sidebar.header("Filters")
    
    # Country filter
    selected_countries = st.sidebar.multiselect(
        "Select Countries",
        options=sorted(df['Country'].unique()),
        default=[]
    )
    
    # Rank range filter
    rank_range = st.sidebar.slider(
        "Select Rank Range",
        min_value=int(df['Global Rank'].min()),
        max_value=int(df['Global Rank'].max()),
        value=(1, 1000)
    )
    
    # Number of countries/cities to display
    num_entries = st.sidebar.slider(
        "Number of entries to display",
        min_value=5,
        max_value=20,
        value=10
    )
    
    # Filter data based on selections
    filtered_df = df.copy()
    if selected_countries:
        filtered_df = filtered_df[filtered_df['Country'].isin(selected_countries)]
    filtered_df = filtered_df[
        (filtered_df['Global Rank'] >= rank_range[0]) &
        (filtered_df['Global Rank'] <= rank_range[1])
    ]
    
    # Display key metrics
    st.header("📊 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Universities", len(filtered_df))
    with col2:
        st.metric("Countries", len(filtered_df['Country'].unique()))
    with col3:
        st.metric("Cities", len(filtered_df['City'].unique()))
    with col4:
        st.metric("Average Rank", int(filtered_df['Global Rank'].mean()))
    
    # World map
    st.header("🌍 Geographic Distribution")
    st.plotly_chart(create_world_map(filtered_df), use_container_width=True)
    
    # Top countries and cities
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🏆 Top Countries")
        st.plotly_chart(create_top_countries_chart(filtered_df, num_entries), use_container_width=True)
    
    with col2:
        st.header("🌆 Top Cities")
        st.plotly_chart(create_top_cities_chart(filtered_df, num_entries), use_container_width=True)
    
    # Rankings analysis
    st.header("📈 Rankings Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Ranking Distribution")
        st.plotly_chart(create_ranking_distribution(filtered_df), use_container_width=True)
    
    with col2:
        st.subheader("Excellence Clusters")
        st.plotly_chart(create_excellence_clusters(filtered_df), use_container_width=True)
    
    # Detailed data view
    st.header("📋 Detailed Data View")
    if st.checkbox("Show Raw Data"):
        st.dataframe(filtered_df)

if __name__ == "__main__":
    main()
