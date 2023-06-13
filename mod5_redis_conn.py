import redis

client = redis.Redis(host='0.0.0.0',password='wangxuan')

print(client.keys()) # 测试刚安装好的redis

for key in client.keys():
    print(key.decode)

