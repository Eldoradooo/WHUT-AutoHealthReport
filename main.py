from health_report import report
from notification import msg
import os

STUID = os.environ['STUID']
PW = os.environ['PW']

if __name__ == "__main__":
        text = report(STUID, PW)
        try:
            msg(text)
        except:
            print("发信异常，请检查发信配置")
