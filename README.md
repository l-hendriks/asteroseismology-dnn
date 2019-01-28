# Calculate stellar parameters using deep networks

This repository contains the code that was used to calculate the stellar parameters in [https://arxiv.org/abs/1811.03639](https://arxiv.org/abs/1811.03639).
If you plan to use this code, please cite the following paper: [https://arxiv.org/abs/1811.03639](https://arxiv.org/abs/1811.03639)

## Requirements

- Tensorflow (tested and run on version 1.12.0)
- TFLearn (tested and run on version 0.3.2)
- The trained model code ([download here](https://fys.kuleuven.be/ster/research-projects/spaceinn/spaceinn) and paste in the models folder)
- To run the notebook: Jupyter, matplotlib and tqdm

You can install specific versions using pip with for example `pip install tensorflow==1.12.0`. It is recommended to run tensorflow with a GPU, please refer to the tensorflow documentation to set it up.

## How to use the notebook

The notebook should work out of the box on the existig stars in the stars folder and give similar results (due to the random nature of the scanning algorithm the results will be slighly different each time, but the conclusions should be the same.

If you want to apply the network on your own star, create a star JSON folder and put it in the stars folder. Then, edit the stars array in the last cell. The algorithm works iteratively on multiple stars, but if you have only 1 star, of course this will work:

```for starname in ['your-star-name']:```

### Structure of the star JSONs

There are a few constraints the star json file has to follow. Please make sure the JSON always has a `settings` and a `data` key. `settings` should always contain the `match_mode` (please refer to the paper for the exact definition of the `exact` and `relative` options) and a `filename` (this is the filename of the result files). Optionally, you can put a `min_n_pg` and `max_n_pg` here to constrain the algorithm.

The data object should contain an array of frequencies and their corresponding `l` and `n_pg` values. The array should be ordered from highest frequency to lowest. For the `l` value you can put either a value or an array of possible values, for example `1` or `[0,1,2]`. The `n_pg` value is the exact frequency mode. If this is not known, but only that it is at maximum as high as the previous frequency (within the same `l`-mode), `n_pg_max: "prev"` is the value you should use (without `n_pg` key). See the stars in the stars folder for examples.
