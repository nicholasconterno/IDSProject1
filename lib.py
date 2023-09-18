import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def load_data(url):
    df = pd.read_csv(url, skiprows=range(1, 32))  # Adjust the range as needed
    return df

def get_summary_statistics(df):
    return df.describe()

def get_mean(df, column_name):
    return df[column_name].mean()

def get_median(df, column_name):
    return df[column_name].median()

def get_stdev(df, column_name):
    return df[column_name].std()



def plot_histogram_save(df, column_name, filename='histogram.png'):
    # Using seaborn styles
    sns.set_style("whitegrid")
    
    # Create the histogram
    plt.figure(figsize=(10, 6))  # Set figure size for larger plot
    sns.histplot(df[column_name], kde=True, color="dodgerblue", bins=30)
    # KDE shows density curve
    plt.title(f'Histogram of {column_name}', fontsize=18)
    plt.xlabel(column_name, fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    # Save the figure
    plt.tight_layout()  # This ensures that the labels don't get cut off
    plt.savefig(filename)
    plt.close()  # Close the figure to free up memory
    return filename
