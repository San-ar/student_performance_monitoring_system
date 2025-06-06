import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

class ModelManager:
    def __init__(self, df):
        self.df = df.copy()
        self.model = DecisionTreeClassifier(random_state=42)
        self.gender_encoder = LabelEncoder()
        self.grade_encoder = LabelEncoder()

    def prepare_data(self):
        self.df['gender_encoded'] = self.gender_encoder.fit_transform(self.df['gender'])
        x = self.df[['gender_encoded', 'study_hours', 'attendance_rate', 'previous_grade', 'participation_score']]
        y = self.grade_encoder.fit_transform(self.df['final_grade'])
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
        df_input['gender_encoded'] = self.gender_encoder.transform(df_input['gender'])
        df_input = df_input[['gender_encoded', 'study_hours', 'attendance_rate', 'previous_grade', 'participation_score']]
        prediction = self.model.predict(df_input)[0]
        return self.grade_encoder.inverse_transform([prediction])[0]
       