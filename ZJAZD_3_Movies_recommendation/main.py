import json

from recommentation_engine.RecommendationEngine import get_recommendations
from parser_tool.ArgsParser import create_arg_parser


def print_recommendations(user, movies, scoreType):
    print("\nMovie recommendations for " + user + ":")
    print("\n" + scoreType)

    print("\nThe most recommended for " + user + ":")
    for i, movie in enumerate(movies[:5]):
        print(f"{i + 1}. {movie}")
    print("\nDefinitely not recommended for " + user + ":")
    for i, movie in enumerate(reversed(movies[-5:])):
        print(f"{i + 1}. {movie}")


if __name__ == '__main__':
    args = create_arg_parser().parse_args()
    user = args.user
    score_type = args.score_type

    ratings_file = 'resources/movieData.json'
    with open(ratings_file, 'r') as file:
        data = json.loads(file.read())

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
        TypeError('Wrong score type: ' + score_type + '.')
