import csv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

# File paths
input_csv_file_path = '2_google_translated(80000).csv'
output_csv_file_path = '2_processed_sub_desc.csv'

# Specify the directory where you want to store the downloaded model locally
local_cache_dir = '/'

# Ensure the cache directory exists
os.makedirs(local_cache_dir, exist_ok=True)

# Load the model and tokenizer from Hugging Face, specifying the local cache directory
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6", cache_dir=local_cache_dir)
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6", cache_dir=local_cache_dir)

# Function to preprocess the last column using the BART model for summarization
def preprocess_with_bart(text):
    try:
        # Tokenize the input text and get the model input IDs
        inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True, padding="longest")

        # Generate the summary (output ids)
        summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode the generated summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

    except Exception as e:
        print(f"Error during BART processing: {e}")
        return text  # Return the original text if BART processing fails

# Read and process the CSV file
with open(input_csv_file_path, 'r', encoding='utf-8') as infile, open(output_csv_file_path, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header row and write it to the new file
    headers = next(reader)
    writer.writerow(headers)

    # Skip the first 40,000 rows
     # Skip the row without processing it

    # Now process from the 40,001st row to the end
    for i, row in enumerate(reader):  # Start from row 40,001
        # Only process the last column with the BART model
        last_column = row[-1]
        bart_processed_text = preprocess_with_bart(last_column)  # Process only the last column with BART

        # Update the last column with the BART processed text
        row[-1] = bart_processed_text

        # Convert all elements in the row to lowercase before writing them to the CSV
        writer.writerow([cell.lower() if isinstance(cell, str) else cell for cell in row])

        # Print the processed row (for debugging, optional)
        print(f"Row {i} processed: {row}")

print(f"Processed data has been saved to {output_csv_file_path}")
