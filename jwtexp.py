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
    with open("pw_longlist.txt") as infile:
        for line in infile:
            key = line.rstrip()
            try:
                solution = jwt.decode(encoded_Data, key, algorithm='HS256')
                print ("Found solution!!! --> {} <--".format(key))
                return(solution) # In doubt use algorithm='RS256'
            except jwt.exceptions.InvalidSignatureError:
                print ("{} not valid".format(key))
                continue



if __name__ == '__main__':
    token = read_file("crack_this_token.txt")

    #Encode Data
    #data = json.load(open("demo_jwt.txt"))
    #encoded_Data = encode_Data(data, 'secret')
    #decoded_Data = decode_Data(token, 'secret')

    #Crack Data
    token = token.rstrip()
    token = token.encode()
    print ("Token gets encoded: {}\n".format(token))

    decoded_Data = try_passwords(token)

    print (decoded_Data)
