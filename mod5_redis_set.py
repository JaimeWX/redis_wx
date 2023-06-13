import redis

client = redis.Redis(host='0.0.0.0',password='wangxuan')

'''
    集合不能像列表一样，从左侧或是右侧弹出，只能随机地弹出一个元素
'''

# 添加成功，返回值为1
# 添加失败，返回值为0
print(client.sadd('redis_set_demo', 'new_data'))
print(client.sadd('redis_set_demo', 'new_data1'))

# 随机弹出一个数据
# client.spop('')

print(client.smembers('redis_set_demo'))

# 交集
client.sinter('set_a', 'set_b')
# 并集
client.sunion('set_a', 'set_b')
# 差集
client.sdiff('set_a', 'set_b') # 有a无b