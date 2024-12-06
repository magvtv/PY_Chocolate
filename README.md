# Traffic Accident Analysis Application

## Overview

This application analyzes traffic accident data to predict risk factors and provide insights into accident patterns. It uses machine learning models to predict death risk, location risk, and time-based risk, and provides additional analyses on the most dangerous counties and accident distribution by time.

## Features

1. Data Preprocessing
   - Converts date and time data
   - Categorizes time of day
   - Calculates location risk based on average deaths

2. Risk Prediction Models
   - Death Risk Prediction
   - Location-based Risk Prediction
   - Time-based Risk Prediction

3. Model Comparison
   - Trains and evaluates multiple models:
     - Logistic Regression
     - Decision Tree
     - Random Forest
     - Support Vector Machine (SVM)
     - K-Nearest Neighbors (KNN)
   - Compares model performance using accuracy scores

4. Additional Analyses
   - Identifies most and least dangerous counties
   - Shows distribution of accidents by time of day

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Usage

1. Ensure your data file is named `traffic_data_updated.csv` and is located in a [data](cci:1://file:///home/pharoh/JKUAT/YR%204/S4.1/Knowledge%20Based%20Systems/Classification/traffic_accident.py:20:0-22:13) folder in the project directory.
2. Run the main script:

## Output

The application will generate:

1. Model performance comparisons for each risk prediction task
2. A list and plot of the most dangerous counties
3. Plots showing the distribution of accidents by time of day and time category

## File Structure

- `traffic_accident.py`: Main script containing all functions and analysis code
- `data/traffic_data_updated.csv`: Input data file (not included in repository)
- `README.md`: This file, containing project documentation

## Future Improvements

- Implement cross-validation for more robust model evaluation
- Add feature importance analysis for each prediction task
- Incorporate geographic visualization of accident hotspots
- Develop a user interface for interactive data exploration

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License

[Include your chosen license here]

## Contact

[Your Name]
[Your Email or Contact Information]