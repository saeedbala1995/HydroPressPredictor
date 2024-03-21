# Hydrodynamic Pressure Predictor
Hydro_Pressure_Predictor is a Python package designed for forecasting exerted hydrodynamic pressure on a bridge's pier using an optimized XGBoost model. It leverages input variables such as the Froude number in the river, the pier's shape (Rectangular or Cylindrical), and channel cross-section geometry (Rectangular or Non-rectangular) to predict hydrodynamic pressure in Pascal. This package has been created by [Saeed Balahang](https://www.linkedin.com/in/saeed-balahang-31b52a207/), a student from Tarbiat Modares University in colaboration with [Dr. Soroush Abolfathi](https://warwick.ac.uk/fac/sci/eng/people/soroush_abolfathi/) and [Seyed Mehran Ahmadi](https://www.linkedin.com/in/s-mehran-ahmadi/?originalSubdomain=ir) 

## Features

- Utilizes an XGBoost model optimized through grid search cross-validation for accurate predictions.
- Input parameters include Froude number, pier's shape, and channel cross-section geometry.
- Predicts nondimensional hydrodynamic pressure on a bridge's pier P/ρU₀² (P is Hydrodynamic Pressure (Pa), U₀ is Flow velocity in Channel (m/s), and ρ is Water density which is considered 998.8 (kg/m³)).

## Usage

To use the Hydrodynamic Pressure Predictor package, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required packages by running:
   ```
   pip install pandas xgboost
   ```

3. Ensure [XGBoost model](https://github.com/saeedbala1995/Hydrodynamic-Pressure-Predictor/blob/main/model/XGBoost.json) file is in the `HydroPressPredictor` directory.
4. Ensure the Python script [`Predictor.py`](https://github.com/saeedbala1995/Hydrodynamic-Pressure-Predictor/blob/main/hydro_pressure_predictor/hydro_pressure_predictor.py) in the `HydroPressPredictor` directory.
5. Run `Predictor.py` to interactively make predictions for hydrodynamic pressure.

