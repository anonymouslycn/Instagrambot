# -*- coding: utf-8 -*-
import requests
import json
import urllib
import gzip
import io
import os
import http.cookiejar
import re
import random
import time
import csv
import codecs
import demjson

# aaa=open("无问西东.json","r")
# file = aaa.read()
# import json

# a = json.loads(file)

# b = a['graphql']['hashtag']['edge_hashtag_to_media']['edges']
# p = b[1]['node']['edge_media_to_caption']['edges'][0]['node']['text']

# # b = a['graphql']['hashtag']["edge_hashtag_to_media"]
# # p = b['page_info']['has_next_page']
# # p = b['page_info']['end_cursor']

# p = b[1]['node']['shortcode']



# # /graphql/query/?query_hash=298b92c8d7cad703f7565aa892ede943&variables=%7B%22tag_name%22%3A%22%E6%97%A0%E9%97%AE%E8%A5%BF%E4%B8%9C%22%2C%22first%22%3A1%2C%22after%22%3A%22AQAEUYWdTRAutlOYrORQJVhaxZQybn2c_2_sbZDwoVueLG5iR1vAQ1N9uCfes9TQk8OaIYgh5GeoAoAB2eg6Ev2ICJ1OuxbHxzlp09c_tI97gw%22%7D

# # print (p)



# bbb = open("BeK8Ajqh9dj.json","r")
# b = json.loads(bbb.read())

# p = b['graphql']['shortcode_media']['owner']['username']

# p = b['graphql']['shortcode_media']['taken_at_timestamp']

# t = time.strftime('%Y-%m-%d',time.localtime(p))

# print ("Time:",t)

s = requests.session()
s.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
}
#                                     __                     
#  __  __  __     __     _ __    ___ /\_\    ___      __     
# /\ \/\ \/\ \  /'__`\  /\`'__\/' _ `\/\ \ /' _ `\  /'_ `\   
# \ \ \_/ \_/ \/\ \L\.\_\ \ \/ /\ \/\ \ \ \/\ \/\ \/\ \L\ \  
#  \ \___x___/'\ \__/.\_\\ \_\ \ \_\ \_\ \_\ \_\ \_\ \____ \ 
#   \/__//__/   \/__/\/_/ \/_/  \/_/\/_/\/_/\/_/\/_/\/___L\ \
#                                                     /\____/
#                                                     \_/__/ 
#  search = "输入你要搜索的内容"  !!!!英文的话是小写无空格


search = "peterrabbit"
website = "http://www.instagram.com"


q = urllib.parse.quote(search)

print (q)
url1 = website+"/explore/tags/"+q+"/?__a=1"

requests.adapters.DEFAULT_RETRIES = 5

html = s.get(url1)

# print (html.text)

ans = json.loads(html.text)

pgn = 0

########################################

f = open("./Save/"+str(search)+".txt","w",encoding='utf-8')
csvfile = codecs.open("./Save/"+str(search)+".csv", 'wb',encoding='gb18030')
submit = "./Save/"+str(search)+".json"

result = [] 

########################################


writer = csv.writer(csvfile)
writer = csv.writer(csvfile)
data=['评论人', '时间','内容']
writer.writerow(data)
#
#
#
edges = ans['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']
for i in range (len(edges)): 
  temp_dict = {}  
  if len(edges[i]['node']['edge_media_to_caption']['edges']) == 0:
    continue
  d = edges[i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
  shortcode = edges[i]['node']['shortcode']
  url2 = website+"/p/"+shortcode+"/?__a=1"
  getnt = s.get(url2, verify=False)
  getnt = json.loads(getnt.text)
  username = getnt['graphql']['shortcode_media']['owner']['username']
  ptime = getnt['graphql']['shortcode_media']['taken_at_timestamp']
  ptime = time.strftime('%Y-%m-%d',time.localtime(ptime))
  print (username)
  print (ptime)
  print (d)
  data = [username,ptime,re.sub(r'\s+',' ', d)]
  writer.writerow(data)
  temp_dict['author'] = username  
  temp_dict['date'] = ptime  
  temp_dict['comment'] = re.sub(r'\s+',' ', d) 
  result.append(temp_dict) 
  f.writelines("评论人：")
  f.writelines(username)
  f.writelines('\n')
  f.writelines("评论时间：")
  f.writelines(ptime)
  f.writelines('\n')
  f.writelines("评论内容：")
  f.writelines(re.sub(r'\s+',' ', d))
  f.writelines('\n')
  f.writelines('\n')
f2 =  open(submit, 'w')
json.dump(result, f2)
f2.close()
################################################################################
# edges = ans['graphql']['hashtag']['edge_hashtag_to_media']['edges']
# for i in range (len(edges)):
#   if len(edges[i]['node']['edge_media_to_caption']['edges']) == 0:
#     continue   
#   d = edges[i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
#   shortcode = edges[i]['node']['shortcode']
#   url2 = website+"/p/"+shortcode+"/?__a=1"
#   getnt = s.get(url2, verify=False)
#   getnt = json.loads(getnt.text)
#   username = getnt['graphql']['shortcode_media']['owner']['username']
#   ptime = getnt['graphql']['shortcode_media']['taken_at_timestamp']
#   ptime = time.strftime('%Y-%m-%d',time.localtime(ptime))
#   print (username)
#   print (ptime)
#   print (d)
#   data = [username,ptime,re.sub(r'\s+',' ', d)]
#   writer.writerow(data)
#   f.writelines("评论人：")
#   f.writelines(username)
#   f.writelines('\n')
#   f.writelines("评论时间：")
#   f.writelines(ptime)
#   f.writelines('\n')
#   f.writelines("评论内容：")
#   f.writelines(re.sub(r'\s+',' ', d))
#   f.writelines('\n')
#   f.writelines('\n')

##

####################################################################333
b = ans['graphql']['hashtag']["edge_hashtag_to_media"]
hnp = b['page_info']['has_next_page']
hashn = b['page_info']['end_cursor']
print (hnp,hashn)
#                                     __                     
#  __  __  __     __     _ __    ___ /\_\    ___      __     
# /\ \/\ \/\ \  /'__`\  /\`'__\/' _ `\/\ \ /' _ `\  /'_ `\   
# \ \ \_/ \_/ \/\ \L\.\_\ \ \/ /\ \/\ \ \ \/\ \/\ \/\ \L\ \  
#  \ \___x___/'\ \__/.\_\\ \_\ \ \_\ \_\ \_\ \_\ \_\ \____ \ 
#   \/__//__/   \/__/\/_/ \/_/  \/_/\/_/\/_/\/_/\/_/\/___L\ \
#                                                     /\____/
#                                                     \_/__/ 
# 下面的设置为  pgn != -1时，将抓取所有结果，可能抓取到的结果十分庞大

while hnp == True and pgn != 300:
    pgn = pgn + 1 
    url1 = website+"/graphql/query/?query_hash=298b92c8d7cad703f7565aa892ede943&variables=%7B%22tag_name%22%3A%22"+q+"%22%2C%22first%22%3A6%2C%22after%22%3A%22"+hashn+"%22%7D"
    print (url1)
    html = s.get(url1, verify=False)
    try:
      ans = json.loads(html.text)
    except:
      v = open("bug.txt","w")
      v.writelines(html.text)
      v.close()
      print ("ERROR")
      url1 = website+"/graphql/query/?query_hash=298b92c8d7cad703f7565aa892ede943&variables=%7B%22tag_name%22%3A%22"+q+"%22%2C%22first%22%3A6%2C%22after%22%3A%22"+hashn+"%22%7D"
      # print (url1)
      html = s.get(url1, verify=False)
      ans = json.loads(html.text)
      # continue;

    ############################################################################
    # edges = ans['data']['hashtag']['edge_hashtag_to_top_posts']['edges']
    # for i in range (len(edges)):   
    #   d = edges[i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
    #   shortcode = edges[i]['node']['shortcode']
    #   url2 = website+"/p/"+shortcode+"/?__a=1"
    #   getnt = s.get(url2, verify=False)
    #   getnt = json.loads(getnt.text)
    #   username = getnt['graphql']['shortcode_media']['owner']['username']
    #   ptime = getnt['graphql']['shortcode_media']['taken_at_timestamp']
    #   ptime = time.strftime('%Y-%m-%d',time.localtime(ptime))
    #   print (username)
    #   print (ptime)
    #   print (d)
    #   f.writelines(username)
    #   f.writelines('\n')
    #   f.writelines(d)
    #   f.writelines('\n')
    #   f.writelines('\n')
    ############################################################################
    try:
      edges = ans['data']['hashtag']['edge_hashtag_to_media']['edges']
    except:
      v = open("bug.txt","w")
      v.writelines(html.text)
      v.close()
      print ("ERROR")
      url1 = website+"/graphql/query/?query_hash=298b92c8d7cad703f7565aa892ede943&variables=%7B%22tag_name%22%3A%22"+q+"%22%2C%22first%22%3A6%2C%22after%22%3A%22"+hashn+"%22%7D"
      # print (url1)
      html = s.get(url1, verify=False)
      ans = json.loads(html.text)
      edges = ans['data']['hashtag']['edge_hashtag_to_media']['edges']




    for i in range (len(edges)):  
      temp_dict = {}
      # print ((len(edges))) 
      if len(edges[i]['node']['edge_media_to_caption']['edges']) == 0:
        continue
      d = edges[i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
      shortcode = edges[i]['node']['shortcode']
      url2 = website+"/p/"+shortcode+"/?__a=1"
      getnt = s.get(url2, verify=False)
      try:
        getnt = json.loads(getnt.text)
      except:
        url2 = website+"/p/"+shortcode+"/?__a=1"
        getnt = s.get(url2, verify=False)
        getnt = json.loads(getnt.text)
      username = getnt['graphql']['shortcode_media']['owner']['username']
      ptime = getnt['graphql']['shortcode_media']['taken_at_timestamp']
      ptime = time.strftime('%Y-%m-%d',time.localtime(ptime))
      # print (username)
      # print (ptime)
      # print (d)
      nd = re.sub(r'\s+',' ', d)
      data = [username,ptime,nd]
      temp_dict['author'] = username  
      temp_dict['date'] = ptime  
      temp_dict['comment'] = nd 
      result.append(temp_dict) 
      writer.writerow(data)
      f.writelines("评论人：")
      f.writelines(username)
      f.writelines('\n')
      f.writelines("评论时间：")
      f.writelines(ptime)
      f.writelines('\n')
      f.writelines("评论内容：")
      f.writelines(nd)
      f.writelines('\n')
      f.writelines('\n')
    b = ans['data']['hashtag']["edge_hashtag_to_media"]
    hnp = b['page_info']['has_next_page']
    hashn = b['page_info']['end_cursor'] 
    print (hnp,hashn,pgn,len(edges))
    # f.writelines(hashn)
    # f.writelines('\n')
    # f.writelines(hnp)
    f2 =  open(submit, 'w')
    json.dump(result, f2)
    f2.close()
f.close()
csvfile.close()

