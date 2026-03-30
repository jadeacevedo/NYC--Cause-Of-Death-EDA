from src.data_loader import fetch_data_from_api
from src.processor import create_dataframe, clean_dataframe
from src.analysis import generate_death_pivot, generate_death_rate_pivot
# Import the new visualization functions
from src.visualization import plot_top_causes_of_death, plot_deaths_by_sex, plot_disease_trends_over_time

def main():
    print("1. Fetching NYC OpenData API...")
    raw_data = fetch_data_from_api()
    
    print("2. Converting to DataFrame and cleaning...")
    df = create_dataframe(raw_data)
    df = clean_dataframe(df)
    
    print("3. Generating Pivot Tables...")
    pivot_deaths = generate_death_pivot(df)
    print("Pivot table generated successfully.")
    
    print("4. Generating Visualizations (saving to /output directory)...")
    # Generate the charts and save them as interactive HTML files
    plot_top_causes_of_death(df, save_offline=True)
    plot_deaths_by_sex(df, save_offline=True)
    
    # Look at the specific diseases highlighted in your notebook's conclusions
    diseases_to_track = ["Alzheimer", "Hypertension", "Parkinson"]
    plot_disease_trends_over_time(df, diseases_to_track, save_offline=True)
    
    print("\nAll tasks completed! Open the 'output' folder to view your interactive charts.")

if __name__ == "__main__":
    main()