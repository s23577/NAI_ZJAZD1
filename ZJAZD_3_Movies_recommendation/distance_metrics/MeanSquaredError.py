import numpy as np

'''
    Calculate the similarity between two users based on the Mean Squared Error (MSE) metric.

    Parameters:
        dataset (dict): A dictionary containing movie ratings from various users.
        user1 (str): Name of the first user.
        user2 (str): Name of the second user (for compare purpose).
    
    Returns:
        similarity_score (numpy.float64): Pearson correlation coefficient between users (-1 to 1, where 1 means full similarity).
'''


def mean_squared_error_score(dataset, chosen_user, user):
    # Create a dictionary to store movies common to both users
    common_movies = {}

    # Identify common movies between the chosen user and the compared user
    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            common_movies[movie] = 1

    # If there are no common movies, return a similarity score of 0
    if len(common_movies) == 0:
        return 0

    # Calculate the absolute differences in ratings for common movies
    diff = []
    count = 0

    # Iterate through movies rated by the chosen user that are also rated by the compared user
    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            # Calculate the absolute difference in ratings for common movies
            diff.append(np.abs(dataset[chosen_user][movie] - dataset[user][movie]))
            count += 1

    # Calculate the Mean Squared Error (MSE) similarity score between users
    return 1 / (1 + ((1/count) * np.sum(diff)))
