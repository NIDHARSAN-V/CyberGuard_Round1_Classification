#!/home/sudharsan/myenv3.12/bin/python3
import csv
from deep_translator import GoogleTranslator

# File paths
input_csv_file_path = 'test.csv'
output_csv_file_path = 'translated_test111.csv'

# Function to translate text to English
def translate_to_english(text):
    try:
        translation = GoogleTranslator(source='auto', target='en').translate(text)
        return translation
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Return original text if translation fails

# Read and process the CSV file
with open(input_csv_file_path, 'r', encoding='utf-8') as infile, open(output_csv_file_path, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header row and write it to the new file
    headers = next(reader)
    writer.writerow(headers)
    
    # Iterate over all rows in the CSV file
    for i, row in enumerate(reader):
        # Translate each cell in the row to English
        translated_row = [translate_to_english(cell) for cell in row]
        
        # Write the translated row to the new CSV file
        writer.writerow(translated_row)
        
        # Print the translated row (for debugging, optional)
        print(f"Row {i} translated: {translated_row}")

print(f"Translated data has been saved to {output_csv_file_path}")
