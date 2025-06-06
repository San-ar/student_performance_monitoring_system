from ModelManager import ModelManager
from UserInterface import start_ui
import pandas as pd

# Loading datset and training model
df = pd.read_csv("./Data/Student_Performance_Data.csv")
model = ModelManager(df)
model.train()

# Testing the model
print("Model Accuracy:", model.evaluate())

# Launching the ui with model
start_ui(model)