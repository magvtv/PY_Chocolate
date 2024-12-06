import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
from datetime import datetime


# data preprocessing
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')
    df['Hour'] = pd.to_datetime(
        df['Time of the Accidents'], format='%H:%M', errors='coerce'
    ).dt.hour
    df['Day_of_Week'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month

    # create time category
    df['Time_Category'] = pd.cut(df['Hour'], bins=[-np.inf, 6, 12, 18, np.inf],
                                 labels=['Night', 'Morning', 'Afternoon', 'Evening'])

    # calculate average deaths per county
    county_avg_deaths = df.groupby(
        'County')['Total people confirmed dead'].mean()
    death_thresholds = county_avg_deaths.quantile([0.33, 0.67])
    df['Location_Risk'] = df['County'].map(
        lambda x: 'Low' if county_avg_deaths[x] <= death_thresholds.iloc[0]
        else 'Medium' if county_avg_deaths[x] <= death_thresholds.iloc[1]
        else 'High')

    # df['Danger_Level'] = pd.cut(
    #     df['Total people confirmed dead'],
    #     bins=[-1, 0, 2, 5, np.inf],
    #     labels=['Low', 'Medium', 'High', 'Very High']
    # )
    # df = df.dropna(subset=['Date', 'Hour'])

    return df


def create_features_target(df):
    features = [
        'Accident Spot',
        'Area',
        'County',
        'Hour',
        'Day_of_Week',
        'Month'
    ]
    X = df[features]
    y_deaths = pd.cut(
        df['Total people confirmed dead'],
        bins=[-1, 0, 2, 5, np.inf],
        labels=['Low', 'Medium', 'High', 'Very High']
    )
    y_location = df['Location_Risk']
    y_time = df['Time_Category']
    # y = df['Danger_Level']
    return X, y_deaths, y_location, y_time


def split_data(X, y, test_size=0.25, random_state=35):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def create_preprocessor():
    numeric_features = ['Hour', 'Day_of_Week', 'Month']
    categorical_features = ['Accident Spot', 'Area', 'County']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )

    return preprocessor


def get_models():
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC(),
        'KNN': KNeighborsClassifier()
    }
    return models


# model training and evaluation
def train_evaluate_models(X, y, preprocessor):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=40)
    models = get_models()
    results = {}

    for name, model in models.items():
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', model)
        ])

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(f"{name} - Accuracy: {accuracy:.4f}")
        print(classification_report(y_test, y_pred))
        print("-----------------------------")

    return results


def plot_model_performance(results, title):
    plt.figure(figsize=(10, 6))
    plt.bar(results.keys(), results.values())
    plt.title(title)
    plt.xlabel('Models')
    plt.ylabel('Accuracy')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# def predict_danger(model, area, accident_spot, county, date_time):
#     # input to dataframe
#     input_data = pd.DataFrame({
#         'Accident Spot': [accident_spot],
#         'Area': [area],
#         'County': [county],
#         'Hour': [date_time.hour],
#         'Day_of_Week': [date_time.weekday()],
#         'Month': [date_time.month]
#     })

#     # making prediction
#     danger_level = model.predict(input_data)[0]
#     return danger_level

# visualization
# def plot_confusion_matrix(y_true, y_pred, classes):
#     cm = confusion_matrix(y_true, y_pred)
#     plt.figure(figsize=(10, 8))
#     sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
#                 xticklabels=classes, yticklabels=classes)
#     plt.title('Confusion Matrix')
#     plt.xlabel('Predicted Label')
#     plt.ylabel('True Label')
#     plt.show()


# utils
# def save_model(model, filename):
#     joblib.dump(model, filename)


# def load_model(filename):
#     return joblib.load(filename)


def analyze_dangerous_counties(df, top_n=5):
    county_deaths = df.groupby('County')['Total people confirmed dead'].agg([
        'mean', 'count']).reset_index()
    county_deaths = county_deaths.sort_values('mean', ascending=False)

    print("\nMost Dangerous Counties:")
    print(county_deaths.head(top_n))

    print("\nLeast Dangerous Counties:")
    print(county_deaths.tail(top_n))

    plt.figure(figsize=(12, 6))
    sns.barplot(x='County', y='mean',
                data=county_deaths.head(top_n), palette='Reds_r')
    plt.title(f'Top {top_n} Most Dangerous Counties')
    plt.xlabel('County')
    plt.ylabel('Average Deaths per Accident')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def analyze_accidents_by_time(df):
    # count accidents by hour
    accidents_by_hour = df['Hour'].value_counts().sort_index()

    # Plotting
    plt.figure(figsize=(12, 6))
    sns.barplot(x=accidents_by_hour.index,
                y=accidents_by_hour.values, palette='Blues_r')
    plt.title('Distribution of Accidents by Time of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Accidents')
    plt.xticks(range(0, 24))
    plt.tight_layout()
    plt.show()

    # Print time categories
    time_categories = df['Time_Category'].value_counts()
    print("\nAccidents by Time Category:")
    print(time_categories)

    # Plotting time categories
    plt.figure(figsize=(10, 6))
    sns.barplot(x=time_categories.index,
                y=time_categories.values, palette='Greens_r')
    plt.title('Distribution of Accidents by Time Category')
    plt.xlabel('Time Category')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.show()


# main
def main():
    # load and preprocess data
    df = load_data('./data/traffic_data_updated.csv')
    df = preprocess_data(df)

    # create features and target
    X, y_deaths, y_location, y_time = create_features_target(df)
    preprocessor = create_preprocessor()

    print("Training models for Death Prediction:")
    results_deaths = train_evaluate_models(X, y_deaths, preprocessor)
    plot_model_performance(
        results_deaths, "Model Performance - Death Prediction")

    print("\nTraining models for Location Risk Prediction:")
    results_location = train_evaluate_models(X, y_location, preprocessor)
    plot_model_performance(
        results_location, "Model Performance - Location Risk Prediction")

    print("\nTraining models for Time Category Prediction:")
    results_time = train_evaluate_models(X, y_time, preprocessor)
    plot_model_performance(
        results_time, "Model Performance - Time Category Prediction")

    # Additional analyses
    analyze_dangerous_counties(df)
    analyze_accidents_by_time(df)

    # # split data
    # X_train, X_test, y_train, y_test = split_data(X, y)

    # create preprocessor

    # train models
    # models = ['logistic_regression', 'decision_tree',
    #           'random_forest', 'svm', 'knn']
    # performance = {}

    # for model_name in models:
    #     try:
    #         model = get_models(model_name)
    #         model.fit(X_train, y_train)
    #         y_pred = model.predict(X_test)
    #         accuracy = accuracy_score(y_test, y_pred)
    #         performance[model_name] = accuracy
    #         print(f"{model_name}: {accuracy}")

    #     except Exception as e:
    #         print(f"Error with {model_name}: {str(e)}")

    # plot_model_performance(performance)

    # while True:
    #     area = input("Enter area: ")
    #     accident_spot = input("Enter the accident spot: ")
    #     county = input("Enter the county: ")
    #     date_str = input("Enter the date (YYYY-MM-DD): ")
    #     time_str = input("Enter the time (HH:MM): ")

    #     try:
    #         date_time = datetime.strptime(
    #             f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    #         danger_level = predict_danger(
    #             model, area, accident_spot, county, date_time)
    #         print(f"Predicted danger level: {danger_level}")

    #     except ValueError:
    #         print("Invalid date or time format. Please try again.")

    #     continue_pred = input(
    #         "Do you want to make another prediction? (y/n): "
    #     )
    #     if continue_pred.lower() != 'y':
    #         break
    # visualize results
    # y_pred = trained_model.predict(X_test)
    # plot_confusion_matrix(y_test, y_pred, classes=[
    #                       'class1', 'class2', ...])
    # save plots
    # plt.savefig(f'{name.lower().replace(" ", "_")}_confusion_matrix.png')


if __name__ == '__main__':
    main()
