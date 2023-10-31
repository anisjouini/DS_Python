

from cryptography import x509
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.asymmetric import rsa
import os
from cryptography.hazmat.primitives.asymmetric import padding


class Certificate:
    def __init__(self) -> None:
        self.public_key = None
        self.private_key = None
        self.certificate = None

    def gen_keys(self, folder):
        key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend())
        self.public_key = key.public_key()
        self.private_key = key
        public_key_file = os.path.join(folder, "public.pub")
        private_key_file = os.path.join(folder, "private.pem")
        key_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
        public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        with open(public_key_file, 'wb') as f:
            f.write(public_key_pem)
        f.close()
        with open(private_key_file, 'wb') as f:
            f.write(key_pem)
        f.close()

    def gen_certif(self, path):

        now = datetime.utcnow()
        name = x509.Name(
            [x509.NameAttribute(NameOID.COMMON_NAME, "localhost")])
        cert = (
            x509.CertificateBuilder()
            .subject_name(name)
            .issuer_name(name)
            .public_key(self.public_key)
            .serial_number(1000)
            .not_valid_before(now)
            .not_valid_after(now + timedelta(days=10 * 365))
            .sign(self.private_key, hashes.SHA256(), default_backend())
        )
        self.certificate = cert

        cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
        certif_path = os.path.join(path, "certificate.pem")
        with open(certif_path, 'wb') as f:
            f.write(cert_pem)
        f.close()

    def encrypt(self, message):
        encrypted_message = self.certificate.public_key().encrypt(message.encode(),
                                                                  padding.PKCS1v15())
        return encrypted_message.hex()
