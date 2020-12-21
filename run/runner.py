import unittest
from BeautifulReport import BeautifulReport
from configuration.config import REPORT_PATH,CASE_PATH
import time

suite=unittest.defaultTestLoader.discover(CASE_PATH,"test_shopping.py")
now=time.strftime("%Y%m%d%H%M%S")
file_name="MRY-report-{}.html".format(now)     #生成报告的文件
runner=BeautifulReport(suite)
runner.report(description="MRY登录测试报告",
              filename=file_name,
              report_dir=REPORT_PATH)
