import os, json, base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def b64e(b: bytes) -> str:
    # Zet bytes om naar base64
    return base64.b64encode(b).decode("utf-8")

def b64d(s: str) -> bytes:
    # zet base64 om naar bytes
    return base64.b64decode(s.encode("utf-8"))

def derive_key_from_passphrase(passphrase: str, *, salt: bytes | None = None, n: int = 2**14, r: int = 8, p: int = 1) -> tuple[bytes, dict]:
    # Genereer een salt van 16 bytes als er nog geen salt is
    if salt is None:
        salt = os.urandom(16)
    # Zet de passphrase om in bytes
    passphrase_bytes = passphrase.encode("utf-8")
    # Pas de Scrypt KDF toe op de passphrase om de key aan te maken
    kdf = Scrypt(salt=salt, length=32, n=n, r=r, p=p)
    key = kdf.derive(passphrase_bytes)
    # Verzamel de metadata in een dictionary, de salt wordt weer omgezet in base64
    kdf_meta = {"name": "scrypt", "n": n, "r": r, "p": p, "salt": b64e(salt)}
    return key, kdf_meta

def encrypt_text_with_passphrase(plaintext: str, passphrase: str)