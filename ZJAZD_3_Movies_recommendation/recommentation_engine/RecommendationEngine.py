import numpy as np
from distance_metrics.Euclidean import euclidean_score
from distance_metrics.Pearson import pearson_score
from distance_metrics.MeanSquaredError import mean_squared_error_score


# 1. liczenie odległości (ocena usera - ocena usera2) w zależności od wyranej metody
# 2. potem wyliczenie współczynnika pomiedzy dwoma osobami, który jest brany potem do obliczen
# 3. potem kazdy film innego usera niz tego dla ktorego chcemy zaproponowac filmy i nie jest to film ogladany przez nas
# jest mnozony razy ten wspolczynnik
# 4. mamy listę filmow z ocenami wynikajacymi ze wspolzynnikow miedzy kolejnymi userami
# 5. potem na liste trafiaja filmy z nowa przeliczona ocena wzgledem wag (normalizacja)
# 6. potem sortowanie malejaco list z filmami i mamy gotowa liste do rekomendacji


def get_recommendations(dataset, chosen_user, score_type):
    if chosen_user not in dataset:
        raise TypeError('Missing ' + chosen_user + ' in the dataset')

    ov = {}

    for user in [x for x in dataset if x != chosen_user]:
        if score_type == "euclidean":
            similarity_score = euclidean_score(dataset, chosen_user, user)
            print(user)
            print(similarity_score)
        elif score_type == "pearson":
            similarity_score = pearson_score(dataset, chosen_user, user)
            print(user)
            print(similarity_score)
        else:
            similarity_score = mean_squared_error_score(dataset, chosen_user, user)
            print(user)
            print(similarity_score)

        if score_type == "mse" and similarity_score <= 0.4:
            continue
        elif score_type == "pearson" and similarity_score <= 0.7:
            continue
        elif score_type == "euclidean" and similarity_score <= 0.3:
            continue

        filtered_list = [movie for movie in dataset[user] if movie not in dataset[chosen_user]
                         or dataset[chosen_user][movie] == 0]

        # loop to calculate weighted average for each movie
        for movie in filtered_list:
            if movie not in ov:
                ov.update({movie: [dataset[user][movie] * similarity_score, similarity_score]})
            else:
                temp_weight = similarity_score + ov[movie][1]
                # print(user + movie)
                # print(temp_weight)
                weighted_average = (dataset[user][movie] * similarity_score + ov[movie][0]) / temp_weight
                # print(weighted_average)
                ov.update({movie: [weighted_average, temp_weight]})
                # print(ov)

    print("\nOV")
    print(ov)

    if len(ov) == 0:
        return ['No recommendations possible']

    # przygotowanie do porównywania ocen filmow na podstawie ocen i wag
    movie_scores = np.array([[data[0] * data[1], movie] for movie, data in ov.items()])

    print("NOT SORTED\n")
    print(movie_scores)

    # Sort in decreasing order
    movie_scores = movie_scores[np.argsort(movie_scores[:, 0].astype(float))[::-1]]

    # Extract the movie recommendations
    movie_recommendations = [movie for _, movie in movie_scores]
    print("SORTED\n")
    print(movie_scores)

    return movie_recommendations
