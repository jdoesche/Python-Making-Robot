def clean_corpus(input_file, output_file):
    """
    Cleans a Python corpus by removing comments and blank lines.

    Args:
        input_file (str): Path to the raw corpus file.
        output_file (str): Path to the cleaned corpus file.
    """
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            stripped_line = line.strip()
            # Skip comments and blank lines
            if stripped_line and not stripped_line.startswith("#"):
                outfile.write(line)  # Preserve original indentation

# File paths
input_file = "corpus.txt"       # Your original corpus
output_file = "cleaned_corpus.txt"  # Output for the cleaned corpus

# Run the cleaning process
clean_corpus(input_file, output_file)
print("Cleaned corpus saved to {}".format(output_file))
