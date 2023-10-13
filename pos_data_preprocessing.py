# Extracts features from the list of tokens and creates a vector for each token
# The vector contains the following features:
# 1. Word
# 2. POS tag
# 3. Chunk tag

from sklearn.feature_extraction import DictVectorizer

# Import file 
filename = "train.txt"
print("Importing file...", filename)
file = open(filename, 'r');
tokens = []
for line in file:
    data = tuple([wrd for wrd in line.split()])
    # print("Data row:", data)
    tokens += [data]
file.close()
print("Imported file successfully.")

print("Tokens:", tokens)

# Extract features from tokens
print("Extracting features from tokens...")
features = []
vec = DictVectorizer(sparse=False)
#sample = [{'Word': 1, 'POS_Tag': 0, 'Chunk_Tag': 1},
#          {'Word': 2, 'POS_Tag': 1, 'Chunk_Tag': 0},
#          {'Word': 1, 'POS_Tag': 3, 'Chunk_Tag': 2}]
#vec.fit_transform(sample)
#print(vec.feature_names_)
#print(vec.transform(sample))

for token in tokens:
    # Ignore empty tokens
    if not token:
        continue
    # print("Token:", token)
    features += [ {'word': token[0], 'pos': token[1], 'chunk': token[2]} ]

# print("Features:", features)

vec.fit_transform(features)
print(vec.feature_names_)
# print(vec.transform(features))
print("Features extracted successfully.")

