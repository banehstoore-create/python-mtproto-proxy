import os
import subprocess

secret = os.getenv("SECRET", "")
port = os.getenv("PORT", "443")

print("Starting MTProto Proxy Python Version...")
print("Using SECRET:", secret)
print("PORT:", port)

cmd = [
    "python3",
    "-m",
    "mtprotoproxy"
]

os.environ["PORT"] = port
os.environ["SECRET"] = secret

subprocess.call(cmd)
