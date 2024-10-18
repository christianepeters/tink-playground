# source: https://android.googlesource.com/platform/external/tink/+/HEAD/docs/PYTHON-HOWTO.md#digital-signatures
import tink
from tink import signature

# Register key manager for signatures
signature.register()

# Signing
# 1. Generate the private key material.
keyset_handle = tink.new_keyset_handle(signature.signature_key_templates.ED25519)

# 2. Get the primitive.
signer = keyset_handle.primitive(signature.PublicKeySign)

# 3. Use the primitive to sign.
signature_data = signer.sign(b'my super important message')

# Verifying
# 1. Obtain the public key material.
public_keyset_handle = keyset_handle.public_keyset_handle()

# 2. Get the primitive.
verifier = public_keyset_handle.primitive(signature.PublicKeyVerify)

# 3. Use the primitive to verify.
verifier.verify(signature_data, b'my super important message')