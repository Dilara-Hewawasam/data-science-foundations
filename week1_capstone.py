import pandas as pd
import numpy as np

# 1.dictionary consisting raw data
raw_data={
    "Student_Id":[201,202,203,204,205,206,207,208,209,210],
    "Department":["stats","CS","math","CS","stats","Math","CS","stats","maths","CS"],
    "Weekly_hours":[14.5,18.0,12.0,np.nan,16.5,20.0,10.5,15.0,11.0,19.5],
    "Coding_score":[88,95,72,85,np.nan,90,68,82,75,98],
    "Theory_score":[92,89,78,88,85,94,70,80,72,96]
}

# convert to a dataframe
df=pd.DataFrame(raw_data)

print("=== 1.RAW DATASET INSPECTION ===")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())


print(df)
print(df.isnull().sum())

#2.Data cleaning : handling missing values 
mean_hours=df["Weekly_hours"].mean()
df["Weekly_hours"]=df["Weekly_hours"].fillna(mean_hours)
median_score=df["Coding_score"].median()
df["Coding_score"]=df["Coding_score"].fillna(median_score)

#3.Feature engineering
#create a new column for composite score
#create for composite score :60% coding ,40% theory
df["composite_score"]=(df["Coding_score"]*0.6+df["Theory_score"]*0.4)

#create performance classification flags
df["High_capacity"]=(df["composite_score"]>=85)&(df["Weekly_hours"]>=14.0)

print("\n===2.CLEANED AND ENGINEERED DATASET===")
print(df[["Student_Id","Department","Weekly_hours","composite_score","High_capacity"]])

#Department level categorisation and summary statistics
dept_summary=df.groupby("Department").agg(
    avg_hours=("Weekly_hours","mean"),
    avg_composite=("composite_score","mean"),
    total_students=("Student_Id","count"),
    high_capacity_count=("High_capacity","sum")

).round(2)

print(dept_summary)

df.to_csv("week1_cleaned_data.csv",index=False)
print("\n Cleaned data exported successfully to 'week1_cleaned_data.csv'")

