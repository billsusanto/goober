import os
from index_builder import build_index, merge_partial_indexes_streaming
from analytics import generate_analytics_report
from nltk.stem import SnowballStemmer
import json

if __name__ == "__main__":
      # Define paths for data and output files
      data_dir = "./DEV"  # Directory containing files to index

      # Initialize a stemmer for token processing
      stemmer = SnowballStemmer("english")

      # Build the index and URL mapping from the provided data directory
      print("Building index...")

      #index, url_mapping = build_index(data_dir, stemmer)
      # with open("./indices/dev_index.json", "w") as outfile:
      #       json.dump(index, outfile)

      build_index(data_dir, stemmer)

      # Save URL mappings to a separate 
      ### json instead of txt
      # with open("url_mapping.json", "w", encoding='utf-8') as file:
      #       json.dump(url_mapping, file)

      merge_partial_indexes_streaming()

      # Generate a report with basic analytics on the index
      #generate_analytics_report("./indices/dev_index.json", "url_mapping.json")
      generate_analytics_report("full_index.json", "url_mapping.json")
