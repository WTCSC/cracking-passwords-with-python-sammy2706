import argparse
import hashlib

# Adds required arguments then saves them to args
parser = argparse.ArgumentParser()
parser.add_argument("password_file")
parser.add_argument("dict_file")
args = parser.parse_args()

hashes = []
names = []
output = []
# Opens up the passwords.txt and reads it
with open(args.password_file) as f:
    encryption = f.read()

# Gets rid of the /n
list = encryption.split("\n")
for hash in list:
    # Takes the name and splits it from the password
    names.append(hash.split(":")[0])
    # It tries to split, adn if there is an error, it ignores it
    try:
        hashes.append(hash.split(":")[1])
    except:
        continue

# Reads each line in worldlist.txt
with open(args.dict_file) as f:
    passwords = f.readlines()
# Takes each passowd and encrypt's it into a sha256 hash
for index, line in enumerate(passwords):
    line = line.rstrip("\n")
    sha_256_hash = hashlib.sha256()
    sha_256_hash.update(line.encode('utf-8'))
    
    # If the Sha256 hashes match up, it saves the user and their password matching the hash
    if sha_256_hash.hexdigest() in hashes:
        output.append([hashes.index(sha_256_hash.hexdigest()), f"{names[hashes.index(sha_256_hash.hexdigest())]}:{line}"])

#Sorts list, then goes through each item in list
output.sort()
for item in output:
    print(item[1])
