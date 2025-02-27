import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


data_path = r"C:\Users\chere\OneDrive\Desktop\IPLDEAE\eae_ipld_project\data\netflix_titles.csv"

movies_df = pd.read_csv(data_path)

min_year = movies_df['release_year'].min()
max_year = movies_df['release_year'].max()

movies_df

f"Min year: {min_year}, Max year: {max_year}"


num_missing_directors = len(movies_df[pd.isna(movies_df['director'])]['show_id'].unique().tolist())

f"Number of missing directors: {num_missing_directors}"


movies_df['country'] = movies_df['country'].fillna('Unknown')
countries = []
for i in movies_df['country'].unique().tolist():
    count = i.split(',')
    for c in count:
        if (c.strip() not in countries) & (c.strip() != 'Unknown') & (c.strip() != ''):
            countries.append(c.strip())

n_countries = len(countries)

f"There are {n_countries} different countries in the data"


movies_df['title char count'] = movies_df['title'].apply(lambda x: len(x) if pd.notna(x) else None)

avg_title_length = movies_df['title char count'].mean()

f"The average title length is {avg_title_length} characters"


year = 2005

movies_df['country_list'] = movies_df['country'].apply(lambda x: [i.strip() for i in x.split(',') if i])

modified_df = movies_df[(movies_df['release_year'] == year) & (movies_df['country'] != 'Unknown')].explode('country_list')

modified_df = modified_df.groupby(by = 'country_list')['show_id'].nunique().reset_index().sort_values(by = 'show_id', ascending = False)

top_10_countries = modified_df[['country_list', 'show_id']].reset_index(drop = True).iloc[:10]

top_10_countries

fig = plt.figure(figsize=(8, 8))
plt.pie(top_10_countries['show_id'], labels=top_10_countries['country_list'], autopct="%.2f%%")
plt.title(f"Top 10 Countries in {year}")

st.pyplot(fig)

movie_length = movies_df[movies_df['type'] == 'Movie']
movie_length['duration'] = movie_length['duration'].apply(lambda x: int(x.strip().split(' ')[0]))
movies_avg_duration_per_year = movie_length.groupby(by = 'release_year')['duration'].mean().reset_index()

fig = plt.figure(figsize=(9, 6))

plt.plot(movies_avg_duration_per_year['release_year'], movies_avg_duration_per_year['duration'], marker = 'o')

plt.title("Average Duration of Movies Across Years")

st.pyplot(fig)