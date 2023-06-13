# zset

import redis

client = redis.Redis(host='0.0.0.0',password='wangxuan')

# client.zadd('rank', {'a':4, 'b':3, 'c':1, 'd':2, 'e':5})

# client.zincrby('rank', -2, 'e') # 把e从第五名变成第三名

print(client.zrangebyscore('rank', min=1, max=5)) # 从小到大列出
print(client.zrevrangebyscore('rank',max=5, min=1)) # 从大到小

# 基card
print(client.zcard('rank')) # 有序集合中有多少个值 

# 显示评分
print(client.zrange('rank', 0, -1, withscores=True)) # 从第一个元素到最后一个元素(从小到大)
print(client.zrevrange('rank', 0, -1, withscores=True)) # 从大到小