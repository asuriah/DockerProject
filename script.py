import os
import collections
import socket

# File paths
data_dir = "/home/data"
file1_path = os.path.join(data_dir, "IF-1.txt")
file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")
output_path = os.path.join(data_dir, "output/result.txt")

# Function to count words
def count_words(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        words = f.read().lower().split()
    return words, collections.Counter(words)

# Process first file
words1, counter1 = count_words(file1_path)
total_words1 = len(words1)

# Process second file
words2, counter2 = count_words(file2_path)
total_words2 = len(words2)

# Handle contractions in second file
expanded_words2 = []
for word in words2:
    expanded_words2.extend(word.replace("'", " ").split())

counter2_expanded = collections.Counter(expanded_words2)

# Get machine IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare output
output = f"""Total words in {file1_path}: {total_words1}
Total words in {file2_path}: {total_words2}
Grand total of words: {total_words1 + total_words2}

Top 3 frequent words in {file1_path}:
{counter1.most_common(3)}

Top 3 frequent words (handling contractions) in {file2_path}:
{counter2_expanded.most_common(3)}

Container IP Address: {ip_address}
"""

# Ensure output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write results to file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output)

# Print output to console
print(output)

