import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('spotify_tracks.csv')

# Let's take a look at the dataset
print(data.head())
print(data.info())
print(data.describe())

# We want to know how many songs are there for each language
language_count = data['language'].value_counts()
print(language_count)

# Let's clean the data by removing all songs with unknown languages
data_cln = data[data['language'] != 'Unknown']

# Now we want to recommend songs for each language
    # Sort the data set by language
group_by_language = data_cln.groupby('language')
print(data_cln.head())

# Plot the number of songs per language
plt.figure(figsize=(12, 6))
language_count = data_cln['language'].value_counts()
plt.bar(language_count.index, language_count.values, color='purple')
plt.title('Number of Songs per Language')
plt.xlabel('Language')
plt.ylabel('Number of Songs')
plt.xticks(rotation=45)  # Rotating the x-axis labels for better readability
plt.tight_layout()
plt.show()


# Show the most popular songs for a specific language
def popular_songs(language, n=5):
    songs_in_language = data_cln[data_cln['language'] == language]
    return songs_in_language.sort_values('popularity', ascending=False).head(n)[['track_name', 'artist_name', 'popularity']]

# Loop through all languages and show the most popular songs
def main():
    unique_languages = data_cln['language'].unique()

    for language in unique_languages:
        print(f"\nTop {5} Popular Songs in {language}:")
        top_songs = popular_songs(language, n=5)
        print(top_songs)


# Call main function
if __name__ == "__main__":
    main()








