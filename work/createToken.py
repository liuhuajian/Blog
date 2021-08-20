import time 
import hashlib
appId = '18a2263b'
appKey = 'bf9b96da66d60203ba4959020a1d0faf'
time_tamp = str(int(time.time() * 1000))
token_str = appId + appKey + time_tamp
hl = hashlib.md5()
hl.update(token_str.encode('utf-8'))
print(f"讯飞时间戳: {time_tamp}")
print(f"讯飞时间戳: {token_str}")
print("讯飞token:{}".format(hl.hexdigest()))