import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# df = pd.read_csv("./Data/Student_Performance_Data.csv")

# # Encoding categorical column
# encoder = LabelEncoder()
# df['gender_encoded'] = encoder.fit_transform(df['gender'])
# df['final_grade_encoded'] = encoder.fit_transform(df['final_grade'])

# # Separating data as x and y
# x = df[['gender_encoded', 'study_hours', 'attendance_rate', 'previous_garde', 'participation_score']]
# y = df['final_grade_encoded']

# # Splitting the data into training and test sets
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Training the model
# model = DecisionTreeClassifier(random_state=42)
# model.fit(x_train, y_train)

# # Evaluating the model
# y_pred = model.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Model Accuracy: {accuracy}")

class ModelManager:
    def __init__(self, df):
        self.df = df.copy()
        self.model = DecisionTreeClassifier()
        self.encoder = LabelEncoder()

    def prepare_data(self):
        x = self.df[['gender_encoded', 'study_hours', 'attendance_rate', 'previous_grade', 'participation_score']]
        x['gender'] = self.encoder.fit_transform(x['gender'])
        y = self.encoder.fit_transform(self.df['final_grade'])
        return train_test_split(x, y, test_size=0.2, random_state=42)
    
    def train(self):
        x_train, x_test, y_train, y_test = self.prepare_data()
        self.model.fit(x_train, y_train)
        self.x_test, self.y_test = x_test, y_test

    def evaluate(self):
        y_pred = self.model.predict(self.x_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        return accuracy

    def predict(self, student_dict):
        df_input = pd.DataFrame([student_dict])
        df_input['gender'] = self.encoder.transform(df_input['gender'])
        prediction = self.model.predict(df_input)[0]
        return self.encoder.inverse_transform([prediction])[0]

df = pd.read_csv("./Data/Student_performance_cleaned.csv")
manager = ModelManager(df)
manager.train()
print("✅ Accuracy:", manager.evaluate())

sample = {
    'gender': ['Female'],
    'study_hours': 6.5,
    'attendance_rate': 92.0,
    'previous_grade': 13.0,
    'participation_score': 7
}
print("🎯 Prediction:", manager.predict(sample))
       