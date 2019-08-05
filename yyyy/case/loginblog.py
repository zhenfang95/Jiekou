# coding:utf-8
import requests
from common.logger import Log
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Blog():
    # s = requests.session()  # 全局参数
    log = Log()
    def __init__(self, s):
        self.s = s

    def login(self):
        url = "https://passport.cnblogs.com/user/signin"
        header = {#"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
                #"Accept": "application/json, text/javascript, */*; q=0.01",
                "Cookie":"这里是抓包后获取的完整cookie",
                "X-Requested-With":"XMLHttpRequest",
                # "Connection":"keep-alive",
                # "Content-Length":"385"
                }
        json_data = {"input1":"这里是抓包后获取的加密账号",
                "input2":"这里是抓包后获取的加密密码",
                "remember": False}


        res = self.s.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        self.log.info(u"调用登录方法，获取结果：%s"%result1)
        return res.json()

    def save(self, title, body):
        url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
        d = {"__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR":"FE27D343",
            "Editor$Edit$txbTitle":title,
            "Editor$Edit$EditorBody":"<p>%s</p>"%body,
            "Editor$Edit$Advanced$ckbPublished":"on",
            "Editor$Edit$Advanced$chkDisplayHomePage":"on",
            "Editor$Edit$Advanced$chkComments":"on",
            "Editor$Edit$Advanced$chkMainSyndication":"on",
            "Editor$Edit$lkbDraft":"存为草稿",
             }
        r2 = self.s.post(url2, data=d, verify=False)  #保存草稿箱
        self.log.info(u"调用保存草稿箱方法，获取结果：%s"%r2)
        return r2.url

    def get_postid(self, r2_url):
        # 正则表达式提取
        import re
        postid = re.findall(r"postid=(.+?)&", r2_url)  # 这里是list []
        self.log.info(u"正则提取postid，获取结果：%s"%postid)
        return postid[0]

    def del_tie(self, postid):
        del_json = {"postId": postid}
        del_url = "https://i.cnblogs.com/post/delete"
        r3 = self.s.post(del_url, json=del_json, verify=False)
        self.log.info(u"删除草稿箱，获取结果：%s"%r3.json()["isSuccess"])
        return r3.json()

if __name__ == "__main__":
    import requests
    s = requests.session()
    Blog(s).login()