import pandas as pd

# Sample data
data = {
    'TextColumn': [
        "This is a sentence",
        "Another sentence here",
        "Pandas is great for data analysis",
        "Short text",
        "Counting words in a column"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to count words in a string
def count_words(text):
    if isinstance(text, str):
        return len(text.split())
    return 0

# Apply the function to the specified column
df['WordCount'] = df['TextColumn'].apply(count_words)

# Display the DataFrame with the word counts
print(df)
