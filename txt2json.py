'''Script for converting txt files into jsonl format required by distllm semantic chunker.'''

import os
import json

def read_txt_files(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            input_filepath = os.path.join(input_directory, filename)
            output_filepath = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.jsonl")

            with open(input_filepath, 'r', encoding='utf-8') as infile, open(output_filepath, 'w', encoding='utf-8') as outfile:
                content = infile.read()
                json_line = json.dumps({"path": input_filepath, "text": content})
                outfile.write(json_line + '\n')

if __name__ == "__main__":
    input_directory = "/homes/ogokdemir/data/cancer_papers"
    output_directory = "/homes/ogokdemir/data/jsonl_files"
    read_txt_files(input_directory, output_directory)
