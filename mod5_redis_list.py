import redis

client = redis.Redis(host='0.0.0.0',password='wangxuan')
'''
    把列表当成队列去使用
'''
# client.lpush('list_redis_demo', 'python')
# client.rpush('list_redis_demo', 'cpp')

# print(client.llen('list_redis_demo'))

# lpop() rpop()
# data = client.lpop('list_redis_demo')
# print(data)

# 查看列表中一定范围内的数据
# print(client.lrange('list_redis_demo', 0, -1))

while True:
    phone = client.rpop('list_redis_demo')
    if not phone:
        print('发送完毕')
        break
    # sendms(phone)
    # res_times = retry_once(phone)
    # if res_times >= 5:
    #     client.lpush('list_redis_demo', phone)