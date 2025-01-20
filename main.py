
import pandas as pd

# Step 1: Read the file
file_path = 'BRCA_clinical_short.csv'  # Replace 'BRCA_clinical_short.csv' with your file path
df = pd.read_csv(file_path)

# Step 2: Calculate Fractions
gender_counts = df['gender'].value_counts()
total_patients = gender_counts.sum()

# Step 3: Determine the fraction of male and female patients
if 'male' in gender_counts:
    male_fraction = gender_counts['male'] / total_patients
else:
    male_fraction = 0

if 'female' in gender_counts:
    female_fraction = gender_counts['female'] / total_patients
else:
    female_fraction = 0

# Step 4: Display the Results
print("Fraction of Male Patients:", male_fraction)
print("Fraction of Female Patients:", female_fraction)


