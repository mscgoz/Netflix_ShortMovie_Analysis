import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read the dataset
df = pd.read_csv("netflix_data.csv")
#   check: print(df.head())

# select only the movies
df_movies = df[df["type"] == "Movie"]
#   check: print(df_movies.head())

# select only these "title", "country", "genre", "release_year" , "duration"
df_movies = df_movies[["title", "country", "genre", "release_year", "duration"]]
# check: print(df_movies.columns)

# select only the duration less than 60m
df_movies_short = df_movies[df_movies["duration"] < 60]
# check: print(df_movies_short.head())

# assign colors to ("Children", "Documentaries", "Stand-Up", and "Other" for everything else).
colors = []

for index, row in df_movies.iterrows():

    if row["genre"] == "Children":
        colors.append("pink")
    elif row["genre"] == "Documentaries":
        colors.append("brown")
    elif row["genre"] == "Stand-Up":
        colors.append("red")
    else:
        colors.append("black")

# check: print(colors)

# create a scatter plot for movie duration by release year using the colors list to color the points

plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

plt.scatter(df_movies["release_year"],df_movies["duration"], c = colors)

# check plt.show()

# Solution: It is not clear to make an assumption on the films based on this analysis.