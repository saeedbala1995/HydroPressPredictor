# Hydrodynamic-Pressure-Predictor
Hydro_Pressure_Predictor is a Python package designed for forecasting exerted hydrodynamic pressure on a bridge's pier using an optimized XGBoost model. It leverages input variables such as the Froude number in the river, the pier's shape (Rectangular or Cylindrical), and channel cross-section geometry (Rectangular or Non-rectangular) to predict hydrodynamic pressure in Pascal.

## Features

- Utilizes an XGBoost model optimized through grid search cross-validation for accurate predictions.
- Input parameters include Froude number, pier's shape, and channel cross-section geometry.
- Predicts nondimensional hydrodynamic pressure on a bridge's pier P/ρU₀² (P is Hydrodynamic Pressure (Pa), U₀ is Flow velocity in Channel (m/s), and ρ is Water density which is considered 998.8 (kg/m³)).

## Usage

To use the Hydrodynamic Pressure Predictor package, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required packages by running: pip install pandas xgboost
3. 

