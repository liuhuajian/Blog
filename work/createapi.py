import base64
import hashlib
import json
import time

import requests

_client = None


def AIUIGetClient():
    global _client
    if _client is None:
        _client = AIUIWebapiClient()
    return _client


class AIUIWebapiClient(object):
    def __init__(self):
        self.base_url = "http://openapi.xfyun.cn/v2/aiui"
        self.app_id = "18a2263b"
        self.api_key = "bf9b96da66d60203ba4959020a1d0faf"

    def _request(self, endpoint, method, headers={}, params=None, body=None):
        requests_method = getattr(requests, method.lower())
        int_headers = {}

        for kk, vv in headers.items():
            int_headers[kk] = vv

        # make the request
        response = requests_method(
            endpoint,
            params=params,
            data=body,
            verify=True,
            headers=int_headers
        )
        return response.text

    def buildHeader(self, result_level="plain", user_id="d15293052168", client_ip="116.237.130.133"):
        curTime = str(int(time.time()))

        md5_1 = hashlib.md5()
        md5_1.update(user_id.encode("utf8"))
        auth_id = md5_1.hexdigest()
        param_json = {"result_level": result_level, "auth_id": auth_id, "data_type": "text", "scene": "main",
                      "client_ip": client_ip}
        param_data = json.dumps(param_json)
        paramBase64 = base64.b64encode(param_data.encode("utf8")).decode()

        md5_2 = hashlib.md5()
        md5_2.update((self.api_key + curTime + paramBase64).encode("utf8"))
        checkSum = md5_2.hexdigest()

        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': self.app_id,
            'X-CheckSum': checkSum,
            'Connection': 'close',
        }
        return header

    def request_aiui_text(self, ask="", result_level="plain", user_id="d15293052168", client_ip="116.237.130.133"):
        aiui_header = self.buildHeader(result_level, user_id, client_ip)

        res_text = self._request(self.base_url, "POST", headers=aiui_header, body=ask)

        return res_text


if __name__ == '__main__':
    ask = '我要听音乐'
    start_time = time.time()
    resp = AIUIGetClient().request_aiui_text(ask.encode('utf-8'))
    print(time.time() - start_time)
    print(resp)