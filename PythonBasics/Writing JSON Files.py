import pandas as pd

# Create a DataFrame from the above dictionary
df = pd.DataFrame({"Name":["Braund", "Cumings", "Heikkinen"], 
"Gender": ["Male", "Female", "Female"],
"Age": [30, 25, 25]})
print("Original DataFrame:\n", df)    

# Write DataFrame to a JSON file
df.to_json("output_written_json_file.json", orient='records', lines=True)

print("The output JSON file has been written successfully.")