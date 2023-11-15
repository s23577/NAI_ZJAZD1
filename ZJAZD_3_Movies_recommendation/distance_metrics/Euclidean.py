import numpy as np

'''
    Calculates the similarity between two users based on the Euclidean metric

    Parameters:
        dataset (dict): A dictionary containing movie ratings from various users.
        user1 (str): Name of the first user.
        user2 (str): Name of the second user (for compare purpose).
    
    Returns:
        similarity_score (numpy.float64): Pearson correlation coefficient between users (-1 to 1, where 1 means full similarity).
'''


def euclidean_score(dataset, chosen_user, user):
    # Create a dictionary to store movies common to both users
    common_movies = {}

    # Identify common movies between the chosen user and the compared user
    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            common_movies[movie] = 1

    # If there are no common movies, return a similarity score of 0
    if len(common_movies) == 0:
        return 0

    # Calculate the squared differences in ratings for common movies
    squared_diff = []

    # Iterate through movies rated by the chosen user that are also rated by the compared user
    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            # Calculate the squared difference in ratings for common movies
            squared_diff.append(np.square(dataset[chosen_user][movie] - dataset[user][movie]))

    # Calculate the Euclidean similarity score between users
    return 1 / (1 + np.sqrt(np.sum(squared_diff)))
