import hashlib
import rsa
import base64
from Crypto.Cipher import AES

hash_function = hashlib.sha256
symmetric_key = b'secret_key_/x00/'

(pubkey, privkey) = rsa.newkeys(2048)

def pad(data):
  num_padding_bytes = AES.block_size - (len(data) % AES.block_size)
  return data + (chr(num_padding_bytes) * num_padding_bytes).encode()

def sign_and_encrypt(message):
  message_hash = hash_function(message.encode()).hexdigest()

  encrypted_hash = rsa.encrypt(message_hash.encode(), privkey).hex()

  signed_message = message + encrypted_hash

  cipher = AES.new(symmetric_key, AES.MODE_ECB)
  padded_message = pad(signed_message.encode())
  encrypted_message = cipher.encrypt(padded_message)

  encoded_ciphertext = base64.b64encode(encrypted_message).decode()

  return encoded_ciphertext

def verify_message(encoded_ciphertext):
  ciphertext = base64.b64decode(encoded_ciphertext)

  cipher = AES.new(symmetric_key, AES.MODE_ECB)
  decrypted_message = cipher.decrypt(ciphertext)
  num_padding_bytes = decrypted_message[-1]
  signed_message = decrypted_message[:-num_padding_bytes].decode()

  message = signed_message[:-512]
  encrypted_hash = signed_message[-512:]

  decrypted_hash = rsa.decrypt(bytes.fromhex(encrypted_hash), privkey).decode()

  message_hash = hash_function(message.encode()).hexdigest()

  if decrypted_hash == message_hash:
    return ("Authentication Successful" , decrypted_hash, message)
  else:
    return "Authentication Unsuccessful"

message = "Hi_Hello"

(encoded_ciphertext) = sign_and_encrypt(message)

(verification_status, decrypted_hash, original_message) = verify_message(encoded_ciphertext)

print(verification_status)
print("\nDecrypted Hash of Message: " + decrypted_hash)
print("\nOriginal Message: " + original_message)
