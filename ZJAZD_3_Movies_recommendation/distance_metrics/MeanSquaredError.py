import numpy as np

#mse

def mean_squared_error_score(dataset, chosen_user, user):
    common_movies = {}

    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            common_movies[movie] = 1

    if len(common_movies) == 0:
        return 0

    diff = []
    count = 0

    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            diff.append(np.abs(dataset[chosen_user][movie] - dataset[user][movie]))
            count += 1

    return 1 / (1 + ((1/count) * np.sum(diff)))
