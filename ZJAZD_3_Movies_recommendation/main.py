"""
==================================================
Movies or series recommendation engine
==================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

To run the program, install the following Python packages (if required):
pip3 install NumPy
pip3 install argparse

This program uses a movie or series recommendation engine based on collaborative filtering. It provides personalized
recommendations for users by analyzing their movie preferences and comparing them with other users in the dataset.

Please ensure that your movie data is stored in a JSON file ('movieData.json') with the following format:
{
    "user1": {"movie1": rating1, "movie2": rating2, ...},
    "user2": {"movie1": rating1, "movie2": rating2, ...},
    ...
}

The choice of JSON format allows for a flexible and structured representation of movie ratings data.



"""

import json

from recommentation_engine.RecommendationEngine import get_recommendations
from parser_tool.ArgsParser import create_arg_parser

'''
     Displays movie recommendations for a given user.

     :param user: Username.
     :param movies: List of recommended movies.
     :param scoreType: The type of score used for recommendations (e.g. "Euclidean", "Pearson", "MSE").
 '''
def print_recommendations(user, movies, scoreType):
    # Print movie recommendations for the specified user
    print("\nMovie recommendations for " + user + ":")
    # Print the type of score used for recommendations
    print("\n" + scoreType)

    # Print the most recommended movies for the user
    print("\nThe most recommended for " + user + ":")
    for i, movie in enumerate(movies[:5]):
        print(f"{i + 1}. {movie}")

    # Print movies that are definitely not recommended for the user
    print("\nDefinitely not recommended for " + user + ":")
    for i, movie in enumerate(reversed(movies[-5:])):
        print(f"{i + 1}. {movie}")


if __name__ == '__main__':
    # Parse command line arguments to get user and score type
    args = create_arg_parser().parse_args()
    user = args.user
    score_type = args.score_type

    # Load movie ratings data from a JSON file
    ratings_file = 'resources/movieData.json'
    with open(ratings_file, 'r') as file:
        data = json.loads(file.read())

    # Get movie recommendations based on the specified score type
    if score_type == 'Euclidean':
        movies = get_recommendations(data, user, "euclidean")
        print_recommendations(user, movies, score_type)
    elif score_type == 'Pearson':
        movies = get_recommendations(data, user, "pearson")
        print_recommendations(user, movies, score_type)
    elif score_type == 'MSE':
        movies = get_recommendations(data, user, "mse")
        print_recommendations(user, movies, score_type)
    else:
        # Raise an error for an incorrect score type
        TypeError('Wrong score type: ' + score_type + '.')
