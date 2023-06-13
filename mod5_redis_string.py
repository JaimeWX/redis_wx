import redis

'''
    1. 百万量级以下，使用字符串保存映射，以上使用哈希，哈希所消耗的内存只有字符串的四分之一
    2. 不要贸然使用keys * 指令，会造成redis短暂不响应
'''

client = redis.Redis(host='0.0.0.0',password='wangxuan')

# client.set('key', 'value')
client.set('key', 'value2', nx=True) # nx: 如果值已经存在的话，则不会被覆盖

# client.append('key', 'value3')

client.set('key2', '100')
res2 = client.incr('key2') # +1
print(res2)
res3 = client.decr('key2') # -1
print(res3)

res = client.get('key')

print(res.decode())