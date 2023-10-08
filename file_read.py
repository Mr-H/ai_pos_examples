import gzip
f=gzip.open('train.txt.gz','rb')
file_content=f.read()
print(file_content)