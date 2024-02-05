#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:24:10 2024

@author: grantoctober
"""

import pandas as pd

# file = pandas.read_csv("/Users/grantoctober/Downloads/movie_dataset.csv")

movies_db = pd.read_csv("movie_dataset.csv")

#Question 1: Highest rated movie

highest_rated_index = movies_db["Rating"].idxmax()

# Get the details of the highest-rated movie
highest_rated_movie = movies_db.loc[highest_rated_index, 'Title']
highest_rating = movies_db.loc[highest_rated_index, 'Rating']

print(f"The highest-rated movie is '{highest_rated_movie}' with a rating of {highest_rating}.")


#Question 2: average revenue of all movies in the dataset 

mean_revenue = movies_db["Revenue (Millions)"].mean()

print(mean_revenue)



#Question 3: average revenue of movies from 2015 to 2017 in the dataset

revenue_mean = movies_db[(movies_db['Year'] >= 2015) & (movies_db['Year'] <= 2017)]

average_revenue = revenue_mean["Revenue (Millions)"].mean()

print(average_revenue)


#Question 4: count of movies were released in the year 2016

count_movies_2016 = (movies_db["Year"] == 2016).sum()


print(count_movies_2016)


#Question 5: count of movies directed by Christopher Nolan                  

cn_movies_count = movies_db[movies_db["Director"] == "Christopher Nolan"].shape[0]

print(f"The number of movies directed by Christopher Nolan is: {cn_movies_count}")


#Question 6: count of movies in the dataset have a rating of at least 8.0?

high_rating_movies_count = movies_db[movies_db["Rating"] >= 8.0].shape[0]

print(f"The number of movies with a rating of at least 8.0 is: {high_rating_movies_count}")

#Question 7: the median rating of movies directed by Christopher Nolan?

cnmr = movies_db[(movies_db["Director"] == "Christopher Nolan") ]

median_rating_cn = cnmr["Rating"].median()

print(median_rating_cn)


#Question 8: display the year with the highest average rating?

average_rating_by_year = movies_db.groupby("Year")["Rating"].mean()

year_highest_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(f"Year with the highest average rating: {year_highest_rating}")

#Question 9: the percentage increase in number of movies made between 2006 and 2016

movies_2006_count = (movies_db["Year"] == 2006).sum()
movies_2016_count = (movies_db["Year"] == 2016).sum()


# Calculate the percentage increase
percentage_increase = ((movies_2016_count - movies_2006_count) / movies_2006_count) * 100

print(f"Number of movies in 2006: {movies_2006_count}")
print(f"Number of movies in 2016: {movies_2016_count}")
print(f"Percentage increase in the number of movies from 2006 to 2016: {percentage_increase:.2f}%")


#Question 10: name the most common actor in all the movies

# Split the actor names and create a list of all actors
all_actors = movies_db["Actors"].str.split(", ").explode()

# Count the occurrences of each actor
actor_counts = all_actors.value_counts()

# Find the most common actor
most_common_actor = actor_counts.idxmax()
most_common_actor_count = actor_counts.max()

print(f"The most common actor in all movies is: {most_common_actor} (appeared in {most_common_actor_count} movies)")


#Question 11: how many unique genres are there in the movies_db dataset

# Split the genre names and create a list of all genres
all_genres = movies_db["Genre"].str.split(", ").explode()

# Count the number of unique genres
unique_genres_count = all_genres.nunique()

print(f"The number of unique genres in the dataset is: {unique_genres_count}")


#Question 12
# Calculate the correlation between 'Revenue' and 'Rating'
correlation_revenue_rating = movies_db['Revenue (Millions)'].corr(movies_db['Rating'])

print(f"Correlation between Revenue and Rating: {correlation_revenue_rating}")

#Correlation between Revenue and Rating: 0.21765389419105996