import argparse


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Check movie recommendations for chosen user from classes:')
    parser.add_argument('--user',
                        dest='user',
                        required=True,
                        help='Input user, as String')
    parser.add_argument("--score-type",
                        dest="score_type",
                        required=True,
                        choices=['Euclidean', 'Pearson', "MSE"],
                        help='Choose between Euclidean, Pearson or MSE distance metrics, as String')
    return parser
