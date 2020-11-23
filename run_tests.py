"""
总执行脚本 -m 指定执行测试用例类型（web 或者 interface）
python run_tests.py -m web 执行web用例
python run_tests.py -m interface 执行接口用例
"""
import os
import time

import click as click

import src.common.HTMLTestRunner as HTMLTestRunner
from case_list import AllTest
from read_config import get_email
from src.common import sendEmail
from src.common.webConfig import WebConfig
from src.web.util import file_handler


@click.command()
@click.option('-m', default='', help='输入执行用例：web 或 interface. 默认为执行web')
def run(m):
    """
    run test
    """
    total_count = None
    report = None
    on_off = get_email('on_off')
    test = AllTest(m)
    latest_dir = os.path.join(test.reportDir, 'latest')
    file_handler.remove_file(latest_dir, test.reportDir)
    try:
        suit = test.set_case_suite()  # 调用set_case_suite获取test_suite
        total_count = suit.countTestCases()
        if total_count != 0:  # 判断test_suite是否为空
            print('Have %d suits to test' % total_count)
            timeStr = time.strftime("%Y-%m%d-%H%M")
            sub_name = m if m != '' else 'report'
            report = '{}/{}-{}.html'.format(latest_dir, sub_name, timeStr)
            with open(report, 'wb') as fp:  # 打开result/report.html测试报告文件，如果不存在就创建
                # 调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=WebConfig.system_name, description='自动化测试报告')
                result = runner.run(suit)
        else:
            print("No case to test.")
            return
    except Exception as e:
        print(e)
    finally:
        print("*********TEST END*********")
    # 判断邮件发送的开关
    if on_off == 'on':
        sendEmail.send_email(report)
    else:
        print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
    # 判断成功率
    pass_rate = (result.success_count + result.skip_count) * 100 // total_count
    print('通过率为{}%,阈值为{}%'.format(pass_rate, WebConfig.pass_rate))
    assert pass_rate >= WebConfig.pass_rate


if __name__ == '__main__':
    run()
