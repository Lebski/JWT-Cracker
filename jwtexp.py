import jwt
import json

def encode_Data(data, secret):
    key = secret
    encoded = jwt.encode(data, secret, algorithm='HS256')
    return encoded

def decode_Data(encoded_Data, key):
    try:
        return(jwt.decode(encoded_Data, key, algorithm='HS256')) # In doubt use algorithm='RS256'
    except jwt.exceptions.InvalidSignatureError:
        print ("Invalid sig")

def read_file(filename):
    token = ""
    with open(filename) as infile:
        for line in infile:
            token += (line)
    return token

def try_passwords(encoded_Data):
    with open("pwfile.txt") as infile:
        for line in infile:
            key = line.rstrip()
            try:
                solution = jwt.decode(encoded_Data, key, algorithm='HS256')
                print ("Found solution!!!")
                return(solution) # In doubt use algorithm='RS256'
            except jwt.exceptions.InvalidSignatureError:
                print ("{} not valid".format(key))
                continue



if __name__ == '__main__':
    encoded = jwt.encode({'some': 'payload'}, 'badumts', algorithm='HS256')
    token = read_file("tokenized.txt")

    #Encode Data
    #data = json.load(open("jwt.txt"))
    #encoded_Data = encode_Data(data, 'secret')
    #decoded_Data = decode_Data(token, 'secret')

    token = token.rstrip()
    token = token.encode()
    print ("Token gets encoded: {}\n".format(token))

    decoded_Data = try_passwords(token)

    print (decoded_Data)
