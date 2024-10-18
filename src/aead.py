import tink
from tink import aead

plaintext = b'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, and what is the use of a book, thought Alice without pictures or conversation?'
associated_data = b'context'

# Register all AEAD primitives
aead.register()

# 1. Get a handle to the key material.
keyset_handle = tink.new_keyset_handle(aead.aead_key_templates.AES256_GCM)

# 2. Get the primitive.
aead_primitive = keyset_handle.primitive(aead.Aead)

# 3. Use the primitive.
ciphertext = aead_primitive.encrypt(plaintext, associated_data)

print(plaintext)
print(ciphertext)
