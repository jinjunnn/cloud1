import os, sys
import csv
import leancloud
from leancloud import cloud
import requests
import re

leancloud.init("ELXEVn8IoKWzNVU52gmYKnn6-gzGzoHsz", master_key="kYWSFq2AwQyBhujn5oIBo64n")

result = cloud.run('write_users',id='_id',user_name='u_name',first_name='f_name',last_name='l_name',userName='result[1]',url='result[0]',bio='bio')
print(result)
