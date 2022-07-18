import requests

header = {

}

data = {
    'cname': '',
    'pid': '',
    'keyword': '闵行',
    'pageIndex': '1',
    'pageSize': '10'
}
ret = requests.post('http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',data=data)
# print(ret.json()['Table1'])
for i in ret.json()['Table1']:
    print(i)