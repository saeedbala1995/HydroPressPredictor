import pandas as pd
from xgboost import XGBRegressor
model = XGBRegressor()
model.load_model("HydroPressPredictor/XGBoost.json")

def normalize_froude_number(X):
    X_norm = (X - 1.334868834) / (1.54443149 - 1.334868834)
    return X_norm, X

def predict_hydrodynamic_pressure(froude_number, pier_shape, channel_geometry, model):
    if froude_number < 1.334868834 or froude_number > 1.54443149:
        print("Warning: This model has been trained for Froude numbers between 1.334 and 1.545.")
    valid_shapes = ['Rectangular', 'Cylindrical']
    valid_geometries = ['Rec', 'Nonrec']
    
    if pier_shape not in valid_shapes or channel_geometry not in valid_geometries:
        raise ValueError("Invalid pier shape or channel geometry. Please provide valid inputs.")
    
    # Create a DataFrame with all required features
    data = pd.DataFrame({'Froude_number':[froude_number],
                         'Pier_shape_Rectangular': [1 if pier_shape == 'Rectangular' else 0],
                         'Pier_shape_Cylindrical': [1 if pier_shape == 'Cylindrical' else 0],
                         'Channel_geometry_Rec': [1 if channel_geometry == 'Rec' else 0],
                         'Channel_geometry_Nonrec': [1 if channel_geometry == 'Nonrec' else 0]})
    data['Froude_number_norm'], data['Froude_number'] = zip(*data['Froude_number'].apply(normalize_froude_number))
    prediction = model.predict(data.drop('Froude_number', axis=1))
    
    return prediction

def load_input_data(file_path):
    data = pd.read_csv(file_path)  # Assuming the input file is in CSV format
    
    valid_shapes = ['Rectangular', 'Cylindrical']
    valid_geometries = ['Rec', 'Nonrec']
    
    if not set(data['Pier_shape']).issubset(valid_shapes) or not set(data['Channel_geometry']).issubset(valid_geometries):
        raise ValueError("Invalid pier shape or channel geometry in input data. Valid shapes are ['Rectangular', 'Cylindrical'] and valid channel geometries are ['Rec', 'Nonrec']")
    
    data['Froude_number_norm'], data['Froude_number'] = zip(*data['Froude_number'].apply(normalize_froude_number))
    
    data = pd.get_dummies(data.drop('Froude_number', axis=1), columns=['Pier_shape', 'Channel_geometry'])
    
    return data

def get_user_input_and_predict(model):
    print('''
This package forecasts P/ρU₀² (nondimensional exerted hydrodynamic pressure) 
on rectangular and cylindrical piers of bridges, here:
P: Hydrodynamic Pressure (Pa)
U₀: Flow velocity in Channel (m/s)
ρ: Water density which is considered 998.8 (kg/m³)
===============================================================
Do you want to forecast a single sample data or a file?
    ''')
    choice = input('''
Enter 'single' for a single sample data or 'file' for a file: 
    ''')
    
    if choice.lower() == 'single':
        froude_number = float(input('''
Enter the Froude number: '''))
        #froude_number_norm = normalize_froude_number(froude_number)
        pier_shape = input('''
Enter the Pier shape (Rectangular or Cylindrical):''')
        channel_geometry = input('''
Enter the Channel geometry (Rec or Nonrec): ''')
        
        prediction = predict_hydrodynamic_pressure(froude_number, pier_shape, 
        channel_geometry, model)
        
        print('-'*15)
        print('Output Prediction:')
        print(f"Predicted P/ρU₀²: {prediction}")
        
    elif choice.lower() == 'file':
        file_path = input('''
The input data file should be in CSV format and must include 3 columns as the following:
1) Froude_number : Continues variable
2) Pier_shape: Categorical Variable (Rectangular or Cylindrical)
3) Channel_geometry: Categorical Variable (Rec or Nonrec)
Please input the file directory (for example HydroPressPredictor/data.csv): 
        ''')
        
        try:
            input_data = load_input_data(file_path)
            predictions = model.predict(input_data)
            
            output_data = input_data.copy()
            output_data['Predicted P/ρU₀²'] = predictions
            
            print('-'*15)
            print('Output Data:')
            print(output_data)
            
            save_output = input('''
Do you want to save the output file as a CSV file? (yes/no): ''')
            
            if save_output.lower() == 'yes':
                output_file_name = input("Enter the name of the output file (without extension): ")
                output_data.to_csv(output_file_name, index=False)
                print(f"{output_file_name} file saved successfully")
            elif save_output.lower() == 'no':
                print("Output file not saved.")
                
            return output_data
        except Exception as e:
            print(f"Error processing input data and making predictions: {e}")
    else:
        print("Invalid choice. Please enter 'single' or 'file'.")

predictions_with_input = get_user_input_and_predict(model)
print('-'*15)
