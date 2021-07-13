import base64
import hashlib
from typing import List, Dict

from tencentcloud.dnspod.v20210323.models import RecordListItem
from tqdm import tqdm

import config
from tencent import *
from utils import *


def gen_b64(file: str) -> List[str]:
    with open(file, "rb") as f:
        content = f.read()
    content = base64.b64encode(content)
    blocks = len(content) // 255
    if len(content) % 255 != 0:
        blocks += 1
    result = []
    index = 0
    while index < blocks:
        result.append(content[index*255:(index+1)*255].decode())
        index += 1
    return result


def add_file(arg: Dict[str, str]):
    b64 = []
    try:
        print("[*] generate base64 payloads")
        b64 = gen_b64(arg["file"])
        print(f"[*] {len(b64)} records will be create")
    except FileNotFoundError:
        print_end_exit(f"[x] file does not exists: {arg['file']}")
    if "key" in arg:
        key = arg["key"]
    else:
        key = config.key
    start_prefix = hashlib.md5(config.key.encode()).hexdigest()
    prefix = start_prefix
    print("[*] start to create TXT records")
    for value in tqdm(b64):
        create_txt_record(f"{prefix}.{arg['prefix']}", value)
        prefix = hashlib.md5(value.encode()).hexdigest()
    print(f"[!] done. file url: {start_prefix}.{arg['prefix']}.{config.domain}")


def delete_file(arg: Dict[str, str]):
    prefix = hashlib.md5(config.key.encode()).hexdigest()
    record: RecordListItem = describe_record_list(f"{prefix}.{arg['prefix']}")
    while record:
        delete_record(record.RecordId)
        print(f"[*] delete {prefix}.{arg['prefix']}")
        prefix = hashlib.md5(record.Value.encode()).hexdigest()
        record = describe_record_list(f"{prefix}.{arg['prefix']}")
    print("[!] done.")


if __name__ == '__main__':
    args = get_args_with_valid()
    if args["type"] == "add":
        add_file(args)
    else:
        delete_file(args)

