# NAI 3
Machine learning with K-means algorithm application.

# Movie Recommendations Engine based on Machine Learning

## Table of Contents

- [Authors](#authors)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How To Use The Engine](#how-to-use-the-engine)
  - [Output](#output)
  - [Program Examples](#program-examples)
- [DataFormat](#data-format)
- [Contributing](#contributing)

## Authors
- Alicja Szczypior
- Krzysztof Szczypior

## Getting Started

### Prerequisites
To run the Movie Recommendations Engine you need to have Python 3 installed on your system. If you don't have it, you can download it from the [official Python website](https://www.python.org/).

### Installation
To install the required libraries, you can use pip:

```bash
pip3 install numpy
pip3 install argparse
```

## How To Use The Engine
Your will find in the main.py file where all logic starts. In the program three distance metrics are implemented, so you can choose which one you want to use or even compare results between all those distance metrics. 

To run the program use the command line to provide user and score type:

**python3 main.py --user <username> --score-type <score_type>**

**--user:** Input user, as a String.

**--score-type:** Choose between Euclidean, Pearson, or MSE distance metrics, as a String.


### Output
The program will display movie recommendations for the specified user based on the selected score type. The recomentations are splitted to the 5 most recomended and to the 5 most not recommended.


### Program Examples

Pearson distance measure
![Pearson](https://github.com/s23578-pj/kolokwiumJAZ/assets/73029891/eeef87b0-086a-4daa-a8e2-9193cde26c95)

Euclidean distance measure
![Euclidean](https://github.com/s23578-pj/kolokwiumJAZ/assets/73029891/9c2cfb9e-5533-45a5-a36c-e2f05df890a5)

MSE distance measure
![MSE](https://github.com/s23578-pj/kolokwiumJAZ/assets/73029891/08892c8b-46e8-4943-af95-dfef47f0c13b)

## Data Format
Ensure your movie ratings data is in JSON format and follows the structure outlined below:

```
{
  "user1": {"movie1": 5, "movie2": 3, ...},
  "user2": {"movie1": 4, "movie3": 1, ...},
  ...
}
```

## Contributing

If you would like to contribute to this project, please feel free to create issues, submit pull requests, or make suggestions. We welcome all contributions.

Enjoy using The Movie Recommendation Engine!
