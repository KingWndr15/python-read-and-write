def process_text_file(file_path, new_content):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"Number of words in the file: {word_count}")

        with open(file_path, 'a') as file:
            file.write('\n' + new_content.strip() + '\n')  
            print("New content has been appended to the file.")
    
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'example.txt'  
new_content = "This is the new content to be appended to the file."
process_text_file(file_path, new_content)
