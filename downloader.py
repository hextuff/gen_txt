import base64
import hashlib
import sys

import dns.resolver

resolver = dns.resolver.Resolver()


def resolve_txt(name: str) -> str:
    try:
        result = resolver.resolve(name, "TXT")
    except:
        return ""
    return str([k for k in result.response.answer[0].items][0]).replace("\"", "")


def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()


def print_and_exit(s: str):
    print(s)
    exit(0)


help_info = """download file uploaded by gen_txt
    python downloader.py <url> [out_file_name]
example:
    python downloader.py 4464014eislkfjxsb5642451fea512a4.test.b477ery.cc
"""

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print_and_exit(help_info)

url = sys.argv[1]
if not resolve_txt(url):
    print_and_exit(f"[*] no file found through this url: {url}")

domain = ".".join(url.split(".")[1:])
result = ""
while True:
    print(f"[*] download {url}")
    value = resolve_txt(url)
    if not value:
        break
    result += value
    prefix = md5(value)
    url = f"{prefix}.{domain}"

if len(sys.argv) == 3:
    file_name = sys.argv[2]
else:
    file_name = "out.dat"

with open(file_name, "wb") as f:
    f.write(base64.b64decode(result.encode()))

print(f"[*] out file to {file_name}")
