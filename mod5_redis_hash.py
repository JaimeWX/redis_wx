import redis

client = redis.Redis(host='0.0.0.0',password='wangxuan')

''' 
    python中的字典就使用了哈希表这个数据结构
    哈希的用途：键值对映射，通过key快速找到value
    哈希要比字符串占用的内存少很多
'''

client.hset('vip_user', '1001', 1)
client.hset('vip_user', '1002', 1)

client.hdel('vip_user','1002')

# 检查是否存在
print(client.hexists('vip_user', '1002'))

# 添加多个键值对
client.hmset('vip_user', {'1003':1, '1004':0})

# 读取
# hkeys hget gmget hgetall
field = client.hkeys('vip_user')
print(field)

print(client.hget('vip_user', '1001'))
print(client.hmget('vip_user', {'1001', '1004'}))

print(client.hgetall('vip_user'))


