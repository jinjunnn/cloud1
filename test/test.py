import os, sys
import csv
import leancloud
from leancloud import cloud
import requests
import re

leancloud.init("ELXEVn8IoKWzNVU52gmYKnn6-gzGzoHsz", master_key="kYWSFq2AwQyBhujn5oIBo64n")

data_info = {'id': 2017718538, 'user_name': 'js999986', 'first_name': '一手引流工作室', 'last_name': None, 'userName': None, 'url': None, 'bio': '一手工作室出粉。精准 JZ 六🈴。体育。博彩。彩票。综合赌粉。网赚。体育。兼职。涩粉 ，劫持各种行业流量等 广告位招租'}

for key in list(data_info.keys()):
        if not data_info.get(key):
            data_info.pop(key)

print(data_info)
# result = cloud.run('write_users',id='_id',user_name='u_name',first_name='f_name',last_name='l_name',userName='result[1]',url='result[0]',bio=None)
# print(result)
