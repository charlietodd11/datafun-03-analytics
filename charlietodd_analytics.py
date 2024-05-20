# This program will fetch a variety of data types and write the data to files. 

#Import dependencies
import pathlib
import requests



# Definitions

##Fetch data from the Web and save it to a file. 
def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):
    try:

        response = requests.get(txt_url)
        response.raise_for_status()
        text_folder_path = pathlib.Path(txt_folder_name)
        text_file_path = text_folder_path / txt_filename
        text_file_path.parent.mkdir(parents=True, exist_ok=True)
        text_file_path.write_text(response.text, encoding ='utf-8')
        print(f"Text was saved to {text_file_path}")

    except Exception as e:
        print(f"Error fetching and writing text data: {e}")
              
## Process the text file by finding
def process_txt_file(txt_folder_name, txt_filename, output_filename):
    try:
        txtt_folder_path = pathlib.Path(txt_folder_name)
        txtt_file_path = txtt_folder_path / txt_filename
        text_data = txtt_file_path.read_text(encoding ='utf-8')
        
        lines=text_data.split('\n')
        lines_count = len(lines)
        processed_data = f'The line count is {lines_count}\n{text_data}'
        output_file_path = txtt_folder_path / output_filename
        output_file_path.write_text(processed_data, encoding='utf-8')
        print(f"Text data processing saved to {output_file_path}")
        
    except Exception as ep:
        print("Error processing text file: {ep}")    

def main():
    txt_url = 'https://www.gutenberg.org/cache/epub/1342/pg1342-images.html'
    txt_folder_name = 'data-txt'
    txt_filename = 'data.txt'

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    process_txt_file('data-txt', 'data.txt', 'count.txt')
if __name__=='__main__':
    main()