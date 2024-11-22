#!/home/sudharsan/myenv3.12/bin/python3
import csv
from deep_translator import GoogleTranslator
import re  # For regular expression handling

# File paths
input_csv_file_path = 'sub_desc.csv'
output_csv_file_path = '2_google_translated(40000).csv'

# Function to translate text to English and clean up unwanted characters
def translate_to_english(text):
    try:
        # Translate the text
        translation = GoogleTranslator(source='auto', target='en').translate(text)

        # Remove unwanted characters and replace with a single space
        cleaned_translation = re.sub(r'[\n\t\r]+', ' ', translation)

        return cleaned_translation
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Return original text in case of failure

# Read and process the CSV file
with open(input_csv_file_path, 'r', encoding='utf-8') as infile, open(output_csv_file_path, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header row and write it to the new file
    headers = next(reader)
    writer.writerow(headers)
    
    # Skip the first 40,000 rows
    # for i in range(40000):
    #     next(reader)  # Skipping rows

    # Now process from the 40,001st row to the end
    for i, row in enumerate(reader):
        
        if i==40001:
            break
        # Translate each cell in the row to English and clean it
        translated_row = [translate_to_english(cell) for cell in row]
        
        # Write the translated row to the new CSV file
        writer.writerow(translated_row)
         
        # Print the translated row (for debugging, optional)
        print(f"Row {i} translated: {translated_row}") 

print(f"Translated data has been saved to {output_csv_file_path}")





# import csv
# from deep_translator import GoogleTranslator
# from langchain_community.llms import Ollama
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate

# # File paths
# input_csv_file_path = 'sub_desc.csv'
# output_csv_file_path = 'processed_sub_desc.csv'

# # Initialize the Ollama LLM
# llm = Ollama(model='llama2')

# # Function to preprocess the last column using the Llama model
# def preprocess_with_llama(text):
#     try:
        
#         prompt = PromptTemplate(
#     input_variables=["question"],
#     template="""
# You are an expert in cybersecurity. Your task is to summarize the following text, making it as concise as possible while retaining all key concepts and important cybersecurity terminology. Focus on shortening the content without omitting any essential details. Provide a summary that captures the core ideas, terms, and important concepts of the text in a clear and concise manner:

# {text}
# """
# )


        
#         # Create the LLM chain and get the response
#         chain = LLMChain(llm=llm, prompt=prompt)
#         response = chain.run(question=text)
        
#         # Clean up the response by removing newlines
#         response = response.replace("\n", "").strip()
#         return response
    
#     except Exception as e:
#         print(f"Error during Llama processing: {e}")
#         return text  # Return the original text if Llama processing fails

# # Function to translate text to English
# def translate_to_english(text):
#     try:
#         translation = GoogleTranslator(source='auto', target='en').translate(text)
#         return translation
#     except Exception as e:
#         print(f"Translation failed: {e}")
#         return text 

# # Read and process the CSV file
# with open(input_csv_file_path, 'r', encoding='utf-8') as infile, open(output_csv_file_path, 'w', newline='', encoding='utf-8') as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)

#     # Read the header row and write it to the new file
#     headers = next(reader)
#     writer.writerow(headers)
    
#     # Skip the first 40,000 rows
#     # for i in range(40000):
#     #     next(reader)  # Skipping rows

#     # Now process from the 40,001st row to the end
#     for i, row in enumerate(reader):
#         # Translate each cell in the row to English (excluding the last column for Llama processing)
#         translated_row = [translate_to_english(cell) for cell in row[:-1]]  # Translate all columns except the last one
        
#         # Process the last column with the Llama model
#         llama_processed_text = preprocess_with_llama(row[-1])  # Process the last column with Llama
#         translated_row.append(llama_processed_text)  # Append the Llama processed text to the row
        
#         # Write the translated row to the new CSV file
#        # Convert all elements in the translated_row to lowercase before writing them to the CSV
#         writer.writerow([cell.lower() if isinstance(cell, str) else cell for cell in translated_row])

        
#         # Print the translated row (for debugging, optional)
#         print(f"Row {i} translated: {translated_row}")

# print(f"Processed data has been saved to {output_csv_file_path}")
