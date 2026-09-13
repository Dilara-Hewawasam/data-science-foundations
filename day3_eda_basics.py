import pandas as pd
import numpy as np

# 1.create raw dataset with categories and missing values
raw_data={
    "StudentID":[101,102,103,104,105,106,107,108],
    "Major":['CS','Stats','CS','Math','Stats','CS','Math','Stats'],
    "Study_Hours":[15,8,20,12,np.nan,18,10,14],#np.nan represents missing data
    "Exam_score":[88,65,95,78,82,92,70,85]
}

df= pd.DataFrame(raw_data)

print("---1. Raw Dataset---")
print(df)

# 2.Check for missing values and fill them with the column mean
print("\n---2. Missing Values check---")
print(df.isnull().sum())

# 3.Impute missing study hours with the average study hours
mean_hours=df["Study_Hours"].mean()
df["Study_Hours"]=df["Study_Hours"].fillna(mean_hours)

print(f"\nMissing value filled with mean hours: {mean_hours:.1f}")

# 4.Filtering data(High performers: exam score>80)
high_performers=df[df["Exam_score"]>80]
print("\n---3. High performers (Score>80)---")
print(high_performers[["StudentID","Major","Exam_score"]])

# 4.GroupBy Analysis:compare average performance by major
major_summary=df.groupby("Major")[["Study_Hours","Exam_score"]].mean()
print("\n---4. Average metrics grouped by major---")
print(major_summary)
