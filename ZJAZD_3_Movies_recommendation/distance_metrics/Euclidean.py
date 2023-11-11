import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def euclidean_score(dataset, chosen_user, user):
    common_movies = {}

    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            common_movies[movie] = 1

    if len(common_movies) == 0:
        return 0

    squared_diff = []

    for movie in dataset[chosen_user]:
        if movie in dataset[user]:
            squared_diff.append(np.square(dataset[chosen_user][movie] - dataset[user][movie]))

    # Tworzenie wykresu
    # plt.figure(figsize=(8, 6))
    # plt.plot(squared_diff, marker='o', linestyle='-', color='b')
    # plt.title('Wykres odległości')
    # plt.xlabel('Indeks filmu')
    # plt.ylabel('Kwadrat różnicy ocen')
    # plt.grid(True)
    # plt.show()

    return 1 / (1 + np.sqrt(np.sum(squared_diff)))
