import pandas as pd

#1.create a simple dictionary with mock student data
data={
    "Student":['Asha','Banuka','Chathura','Dilini','Eshani'],
    "Maths_score":[85,92,78,95,88],
    "Stats_score":[90,88,72,98,91],
    "Hours_studied":[12,15,8,18,14]
}

#2.convert dictionary to a pandas DataFrame
df=pd.DataFrame(data)

#3.Inspect the DataFrame
print("---First 5 Rows od Data---")
print(df)
print("\n---Summary Statistics---")
print(df.describe())

#4.Perform basic data manipulation
df["Total_Score"]=df["Maths_score"]+df["Stats_score"]
df["Passed"]=df["Total_Score"]>=160

print("\n---Updated data with Total Score & status ---")
print(df)