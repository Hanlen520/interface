# -*- coding: utf-8 -*-
import os
import unittest
import time
import HtmlTestRunner

# 当前脚本所在文件的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)

# 1、加载所有的测试用例
def add_one(caseName="case",rule="test*.py"):
    case_path = os.path.join(cur_path,caseName) # 用例文件夹
    # 若不存在case文件夹，则自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    print(discover)
    return discover

# 2、执行用例，生成HTML报告
def run_case(all_case,reportName="report"):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName) #报告文件夹
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    print("html报告文件：%s"%report_abspath)
    fp = open(report_abspath,"w")

    runner = HtmlTestRunner.HTMLTestRunner(stream=fp,report_title=u"test-results",output=report_path,descriptions=u"test-case-run")
    #调用add_case函数返回值all_case
    runner.run(all_case)
    fp.close()


if __name__ == '__main__':
    allcase = add_one()
    run_case(all_case=allcase)