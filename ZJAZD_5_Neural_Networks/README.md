# NAI 5
Neural Networks for Classification

## Table of Contents

- [Authors](#authors)
- [Datasets](#datasets)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Output](#output)
- [Program Output Examples](#program-output-examples)
- [Contributing](#contributing)

## Authors
- Alicja Szczypior
- Krzysztof Szczypior

## Datasets

1. fashion_mnist from <br> _**fashion_mnist.load_data()**_
2. Chlorophyll A and B levels in Chestnut and Chives from author`s file source: _**chlorophyll_a_b_levels.csv**_

## Getting Started

### Prerequisites and Installation

To run the program, install the following Python packages (if required):
TensorFlow with some packages which should be imported in the code:
- fashion_mnist dataset
- Flatten, Dense
- Sequential model
- seaborn package
- numpy package
- pyplot from matplotlib
- sklearn.metrics
- tensorflow

### How to run the program
Run just every .py file with script per project and used method or press the run button.

### Output

1. **wheat_seeds** displays prediction and accuracy.
2. **Cifar-10** (animals) displays predicted model + actual class with accuracy.
3. **Clothes** displays predicted image, model A & B, visualization of confusion matrix.
4. **chlorophyll** displays prediction and accuracy.

## Program Output Examples

1. Wheat seed 

### Decision Tree
* Plots

![wheat_seed_dt_figure1.png](assets%2Fwheat_seed_dt_figure1.png)
![wheat_seed_dt_figure2.png](assets%2Fwheat_seed_dt_figure2.png)

* Decision Tree Schema

![wheat_seed_dt_diagram.png](assets%2Fwheat_seed_dt_diagram.png)

* Metrics related to the quality of the classification

![wheat_seed_dt.png](assets%2Fwheat_seed_dt.png)

### Support Vector Machine
* Metrics related to the quality of the classification

![wheat_seed_svm.png](assets%2Fwheat_seed_svm.png)

2. Chlorophyll A and B levels in Chestnut and Chives

### Decision Tree
* Plot

![chlorophyl_dt_figure.png](assets%2Fchlorophyl_dt_figure.png)

* Decision Tree Schema

![chlorophyl_dt_diagram.png](assets%2Fchlorophyl_dt_diagram.png)

* Metrics related to the quality of the classification

![chlorophyl_dt.png](assets%2Fchlorophyl_dt.png)



### Support Vector Machine
* Metrics related to the quality of the classification

![chlorophyl_svm.png](assets%2Fchlorophyl_svm.png)



## Contributing

If you would like to contribute to this project, please feel free to create issues, submit pull requests, or make suggestions. We welcome all contributions.

Enjoy!
