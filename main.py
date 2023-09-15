from lib import load_data, get_mean, get_median,get_stdev, get_summary_statistics, plot_histogram_save

url = 'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'
df = load_data(url)

# Print summary statistics
print(get_summary_statistics(df))

md = df.to_markdown()
with open('generated_markdown.md','w') as f:
    f.write(md)
# Assuming the dataset has a column named 'rating' 
# (adjust column names based on the actual dataset columns)
print(f"Mean of 'Rotten Tomatoes %': {get_mean(df, 'Rotten Tomatoes %')}")
print(f"Median of 'Rotten Tomatoes %': {get_median(df, 'Rotten Tomatoes %')}")
print(f"Standard Deviation of 'Rotten Tomatoes %': {get_stdev(df, 'Rotten Tomatoes %')}")

# Plotting a histogram for 'rating'
fname= plot_histogram_save(df, 'Rotten Tomatoes %')