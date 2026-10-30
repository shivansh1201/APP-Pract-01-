import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("employee.csv")

# Display employee details
print("Employee Details:")
print(df[["Name", "Department", "Salary"]])

# Calculate average salary department-wise
avg = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary:")
print(avg)

# Display bar graph
avg.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()
