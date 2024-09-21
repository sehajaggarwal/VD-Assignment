#QUESTION 2
#----------------

import pandas as pd
import re

# Function to validate email using regex
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def clean_user_data(input_file, output_file):
    # Read file as pandas DataFrame
    df = pd.read_csv(input_file)

    # Remove duplicate rows
    df_cleaned = df.drop_duplicates(subset='user_id')

    # Filter out rows with invalid email formats
    df_cleaned = df_cleaned[df_cleaned['email'].apply(is_valid_email)]

    # Write the cleaned data to a new CSV file
    df_cleaned.to_csv(output_file, index=False)


#Test the solution
if __name__ == "__main__":
    input_file = 'input.csv'
    output_file = 'output.csv'
    clean_user_data(input_file, output_file)
    print("Completed. Check output.csv for results")