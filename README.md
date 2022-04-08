# Object detection: Bounding box regression.


## Bounding box regression


**What is a bounding box?**

Typically a bounding box is a set of 2 coordinates of a rectangle (upper left and lower right corners) around an area of interest, such as the dog in the image below.

<p align='center'>
<img src=reports/figures/bounding_box2.jpg width="400" height="500" />
</p>

For instance, in this image we have, a bounding box <!-- $B = \{(x_1, y_1), (x_2, y_2)\}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=B%20%3D%20%5C%7B(x_1%2C%20y_1)%2C%20(x_2%2C%20y_2)%5C%7D"> where

<!-- <!-- $$
\begin{aligned}
(x_1, y_1) &= (400, 750)\\
(x_2, y_2) &= (1305, 1625)
\end{aligned}
$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=%5Cbegin%7Baligned%7D%0D%0A(x_1%2C%20y_1)%20%26%3D%20(400%2C%20750)%5C%5C%0D%0A(x_2%2C%20y_2)%20%26%3D%20(1305%2C%201625)%0D%0A%5Cend%7Baligned%7D%0D"></div>



**What is bounding box regression?**

Is just technique to predict the coordinates of a bounding-box of a given image, learn more details in [Universal Bounding Box Regression and Its Applications](https://doi.org/10.48550/arXiv.1904.06805).


## Main Idea

In order to perform bounding box regression for object detection, all we need to do is build a network architecture:

- At the head of the network, place a fully-connected layer with four neurons, corresponding to the values of the upper-left and lower-right (x, y)-coordinates.
- Given that four-neuron layer, implement a sigmoid activation function such that the outputs are returned in the range [0, 1].
- Train the model using a loss function on:
  - the input images
  - the bounding box of the object in the image.

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
