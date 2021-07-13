import json
from typing import Dict

from ratelimiter import RateLimiter
from utils import *
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models

import config


@RateLimiter(max_calls=20, period=1)
def describe_record_list(subdomain: str):
    try:
        cred = credential.Credential(config.tencent["secret_id"], config.tencent["secret_key"])
        http_profile = HttpProfile()
        http_profile.endpoint = "dnspod.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        client = dnspod_client.DnspodClient(cred, "", client_profile)

        req = models.DescribeRecordListRequest()
        params = {
            "Domain": config.domain,
            "Subdomain": subdomain
        }
        req.from_json_string(json.dumps(params))

        resp = client.DescribeRecordList(req)
        return resp.RecordList[0]

    except TencentCloudSDKException as err:
        if err.code == "ResourceNotFound.NoDataOfRecord":
            return False
        print_end_exit(f"[x] API ERROR: {err.code}")


@RateLimiter(max_calls=20, period=1)
def create_txt_record(prefix: str, value: str):
    try:
        cred = credential.Credential(config.tencent["secret_id"], config.tencent["secret_key"])
        http_profile = HttpProfile()
        http_profile.endpoint = "dnspod.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        client = dnspod_client.DnspodClient(cred, "", client_profile)

        req = models.CreateRecordRequest()
        params = {
            "Domain": config.domain,
            "RecordType": "TXT",
            "RecordLine": "默认",
            "Value": value,
            "SubDomain": prefix
        }
        req.from_json_string(json.dumps(params))

        _ = client.CreateRecord(req)
    except TencentCloudSDKException as err:
        print_end_exit(f"[x] API ERROR: {err.message}")


@RateLimiter(max_calls=20, period=1)
def delete_record(record_id: int):
    try:
        cred = credential.Credential(config.tencent["secret_id"], config.tencent["secret_key"])
        http_profile = HttpProfile()
        http_profile.endpoint = "dnspod.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        client = dnspod_client.DnspodClient(cred, "", client_profile)

        req = models.DeleteRecordRequest()
        params = {
            "Domain": config.domain,
            "RecordId": record_id
        }
        req.from_json_string(json.dumps(params))

        _ = client.DeleteRecord(req)

    except TencentCloudSDKException as err:
        print_end_exit(f"[x] API ERROR: {err.message}")


# a = describe_record_list("c4a646bead2cd7e6616d69f84a4d6b26.testa")
# print(a)

