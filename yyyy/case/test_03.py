# coding:utf-8
import unittest
import requests
from loginblog import Blog
from common.logger import Log

class Test(unittest.TestCase):
    log = Log()
    def setUp(self):
        s = requests.session()
        self.blog = Blog(s)

    def test_login(self):
        u'''测试登录用例'''
        self.log.info("------start!--------")
        result = self.blog.login()
        self.log.info(u"调用登录结果：%s"%result)
        self.log.info(u"获取是否登录成功：%s"%result["success"] )
        self.assertEqual(result["success"] , True)    # 拿结果断言
        self.log.info("------end!--------")

    def test_del(self):
        u'''测试保存草稿箱-删除用例'''
        self.log.info("------start!--------")
        # 第一步：登录
        self.log.info(u"第一步：登录")
        self.blog.login()
        # 第二步：保存
        self.log.info(u"第二步：保存")
        r2_url = self.blog.save("wQEW12", "WQASDA21e3S")
        pid = self.blog.get_postid(r2_url)
        # 第三步：删除
        self.log.info(u"第三步：删除")
        result = self.blog.del_tie(pid)
        self.assertEqual(result["isSuccess"], True)
        self.log.info("------end!--------")

if __name__ == "__main__":
   unittest.main()
