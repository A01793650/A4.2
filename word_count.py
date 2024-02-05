"""Module providing a function printing python version."""
import sys
import time

def process_file(file_path):
    """Function to count distinct words and their frequencies."""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            words = file.read().split()
    except IOError as e:
        print(f"Error: {e}")
        return None

    word_count = {}
    invalid_data = []

    for word in words:
        # Removing punctuation and converting to lowercase for case-insensitive counting
        cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
        if cleaned_word:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
        else:
            invalid_data.append(word)

    return word_count, invalid_data, len(words)

def save_results_to_file(file_path, word_count, invalid_data, total_words):
    """Function to save results to a file."""
    with open(file_path, 'w', encoding="utf-8") as result_file:
        result_file.write("Row Labels\tCount\n")
        for word, count in word_count.items():
            result_file.write(f"{word}\t{count}\n")

        for invalid_word in invalid_data:
            result_file.write(f"{invalid_word}\n")

        result_file.write(f"\nGrand Total: {total_words}")

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = time.time()

    results = process_file(input_file)

    if results:
        word_count, invalid_data, total_words = results

        save_results_to_file("WordCountResults.txt", word_count, invalid_data, total_words)

        print("Row Labels\tCount")
        for word, count in word_count.items():
            print(f"{word}\t{count}")

        for invalid_word in invalid_data:
            print(invalid_word)

        print(f"\nGrand Total: {total_words}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nElapsed Time: {elapsed_time:.4f} seconds")
    with open("WordCountResults.txt", 'a', encoding="utf-8") as result_file:
        result_file.write(f"\nElapsed Time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    main()
    # End-of-file
    