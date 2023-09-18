from lib import load_data, get_mean, get_median,get_stdev,\
get_summary_statistics, plot_histogram_save
import argparse
def main(mdPath, histogramPath):
    url = ('https://gist.githubusercontent.com/tiangechen/b68782efa49a16eda'
           'f07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv')
    df = load_data(url)

    # Print summary statistics
    print(get_summary_statistics(df))

    md = df.to_markdown()
    with open(mdPath,'w') as f:
        f.write(md)
    # Assuming the dataset has a column named 'rating' 
    # (adjust column names based on the actual dataset columns)
    print(f"Mean of 'Rotten Tomatoes %': {get_mean(df, 'Rotten Tomatoes %')}")
    print(f"Median of 'Rotten Tomatoes %': {get_median(df, 'Rotten Tomatoes %')}")
    stDev=get_stdev(df, 'Rotten Tomatoes %')
    print(f"Standard Deviation of 'Rotten Tomatoes %': {stDev}")

    # Plotting a histogram for 'rating'
    plot_histogram_save(df, 'Rotten Tomatoes %',filename=histogramPath)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    # Add arguments
    parser.add_argument("mdPath", help="Markdown Path")
    parser.add_argument("histPath", help="Histogram Path")
    
    # Parse arguments
    args = parser.parse_args()

    # Call the main function
    main(args.mdPath, args.histPath)