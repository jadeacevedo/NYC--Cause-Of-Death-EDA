import plotly.express as px
import os

def ensure_output_dir(directory="output"):
    """Creates an output directory for saving plots if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def plot_top_causes_of_death(df, save_offline=False):
    """
    Creates a bar chart showing the top 10 leading causes of death overall.
    """
    # Group by cause and sum the deaths
    top_causes = df.groupby('cause')['deaths'].sum().reset_index()
    top_causes = top_causes.sort_values(by='deaths', ascending=False).head(10)

    fig = px.bar(
        top_causes, 
        x='deaths', 
        y='cause', 
        orientation='h',
        title='Top 10 Leading Causes of Death in NYC (2007 - Present)',
        labels={'deaths': 'Total Deaths', 'cause': 'Cause of Death'},
        color='deaths',
        color_continuous_scale='Reds'
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    
    if save_offline:
        ensure_output_dir()
        fig.write_html("output/top_10_causes.html")
        print("Saved plot to output/top_10_causes.html")
    else:
        fig.show()

def plot_deaths_by_sex(df, save_offline=False):
    """
    Creates a grouped bar chart comparing deaths by sex for the top 5 causes.
    """
    # Find top 5 causes first
    top_5_causes = df.groupby('cause')['deaths'].sum().nlargest(5).index
    
    # Filter dataframe to only these top 5 causes
    filtered_df = df[df['cause'].isin(top_5_causes)]
    
    # Group by cause and sex
    grouped = filtered_df.groupby(['cause', 'sex'])['deaths'].sum().reset_index()

    fig = px.bar(
        grouped, 
        x='cause', 
        y='deaths', 
        color='sex',
        barmode='group',
        title='Top 5 Causes of Death in NYC by Sex',
        labels={'deaths': 'Total Deaths', 'cause': 'Cause of Death', 'sex': 'Sex'}
    )
    
    if save_offline:
        ensure_output_dir()
        fig.write_html("output/deaths_by_sex.html")
        print("Saved plot to output/deaths_by_sex.html")
    else:
        fig.show()

def plot_disease_trends_over_time(df, diseases, save_offline=False):
    """
    Creates a line chart tracking specific diseases over the years 
    (e.g., Alzheimer's, Hypertension as mentioned in your notebook).
    """
    # Filter for the specific diseases
    filtered_df = df[df['cause'].str.contains('|'.join(diseases), case=False, na=False)]
    
    # Group by year and cause
    trends = filtered_df.groupby(['year', 'cause'])['deaths'].sum().reset_index()
    
    # Ensure year is treated as a string/category for clean x-axis plotting
    trends['year'] = trends['year'].astype(str)

    fig = px.line(
        trends, 
        x='year', 
        y='deaths', 
        color='cause',
        markers=True,
        title='Death Trends Over Time for Selected Diseases',
        labels={'deaths': 'Total Deaths', 'year': 'Year', 'cause': 'Disease'}
    )
    
    if save_offline:
        ensure_output_dir()
        fig.write_html("output/disease_trends.html")
        print("Saved plot to output/disease_trends.html")
    else:
        fig.show()