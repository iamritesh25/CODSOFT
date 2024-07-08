import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movies_data = {
    'MovieID': [1, 2, 3, 4, 5],
    'MovieName': ['Marvel', 'The family man','Mirzapur', 'The kerala story', 'hera pheri'],
    'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy'],
    'Description': ['Action-packed movie.',
                    'A funny comedy with lots of laughs.',
                    'Thrilling action movie.',
                    'A drama with emotional moments.',
                    'A funny comedy with lots of laughs.']
}

ratings_data = {
    'UserID': [1, 1, 2, 2, 3],
    'MovieID': [1, 2, 3, 4, 5],
    'Rating': [5, 4, 3, 2, 4],
}

movies_df = pd.DataFrame(movies_data)
ratings_df = pd.DataFrame(ratings_data)

movie_ratings = pd.merge(ratings_df, movies_df, on='MovieID')


tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genre'])

cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)


def get_movie_recommendations(movie_name, rating_threshold=2.0):
    movie_index = movies_df.index[movies_df['MovieName'] == movie_name].tolist()[0]

    similar_movies = list(enumerate(cosine_similarity[movie_index]))
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

    high_rated_similar_movies = [
        (movies_df['MovieName'][i], movie_ratings['Rating'][movie_ratings['MovieID'] == i].mean())
        for i, _ in similar_movies if movie_ratings['Rating'][movie_ratings['MovieID'] == i].mean() > rating_threshold]

    high_rated_similar_movies = sorted(high_rated_similar_movies, key=lambda x: x[1], reverse=True)
    return high_rated_similar_movies


print("\nMovie Recommendation System")

movie_name = input("\nEnter the Movie Name from Movie data: ")
recommendations = get_movie_recommendations(movie_name)

print(f"\nTop Movie Recommendations for '{movie_name}' based on User Preferences Using Content-Based Filtering")
for movie, rating in recommendations:
    print(f"{movie} (Average Rating: {rating:.2f})")