import requests
from qiniu import Auth, put_file, etag

access_key='yourAccessKey'
secret_key='yourSecretKey'
path="yourPicPath"
def upload(id):
    global access_key
    global secret_key
    url = "http://jwzx.cqupt.edu.cn/showstuPic.php?xh="
    pic = requests.get(url+id)
    with open(path + id + ".jpg", "wb") as code:
        code.write(pic.content)

    q = Auth(access_key, secret_key)
    bucket_name = 'picture'
    key = id+".jpg"
    token=q.upload_token(bucket_name,key)
    localfile=path + id + ".jpg"
    ret,info = put_file(token,key,localfile)
    assert ret['key']==key
    assert ret['hash']==etag(localfile)