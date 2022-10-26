# WHUT-ActionHealthReport

**研究生系统填报功能已支持。**
** Action 自动运行现已支持。**

通过访问学校健康填报接口，模拟健康填报过程，通过邮件发送结果到指定邮箱,或通过 cqhttp 发送结果到QQ（支持批量）。

配置方法非常简单，只需填写填写相关信息，即可健康填报并发送结果消息。

配置完成后，可通过 crontab 等手段定时运行 `main.py`，即可每日自动填报。

现支持利用GitHub Action功能完成定时自动填报（不建议），只需在Security中添加对应secrets即可。

![image](https://user-images.githubusercontent.com/109326501/197983479-7e175420-e69d-49cf-a7ea-670d6f460937.png)
![image](https://user-images.githubusercontent.com/109326501/197984059-f7d7f460-3d83-42ca-b017-5180433e0ee3.png)

PS:仅适配了邮件发送、单人填报，且由于GitHub Action的定时功能不稳定，因此设置了每天早上8点和中午12点的两次自动运行（可在workflows/python-app.yml第十行修改，若每天只运行一次可能会出现某一天未运行的情况，两次则几乎不会漏填），若第一次成功，第二次填报失败，显示已填报。

### 效果预览

![image](https://user-images.githubusercontent.com/109326501/197984378-03e95d15-717b-4bd0-999c-83e27ddaac51.png)


### 免责声明

该自动填报程序仅为了方便每日填报过程，严禁通过该程序伪造填报地址、健康状态。**若使用该程序导致不良后果，使用者需承担所有责任！**

### 使用方法

1. 在 `main.py` 中填写账号、密码（请解绑微信小程序）
2. 在 `health_report.py` 修改填报地址、填报温度。（余家头校区可保持默认值不改）
3. 在 `notification.py` 中填写你需要的发信方式，支持 cqhttp 和邮件。
4. 定时运行 `main.py` 即可。

### 所需模块

- requests
    - `pip install requests`

### 问题反馈

如果你使用的时候出现了异常情况，欢迎提交 issue 并附上错误详情。

注意，详细日志中含有敏感隐私信息，不建议直接公开。详细日志中的 `message` 条目和 `Python Traceback` 信息可公开分享。

### 鸣谢

程序流程借鉴 [xiaozhangtongx/WHUT-JKRBTB](https://github.com/xiaozhangtongx/WHUT-JKRBTB)，
因学校给每次的请求都进行了base64编码，因此该程序已经失效。
后作者ChrisKimZHT（https://github.com/ChrisKimZHT/WHUT-AutoHealthReport）重新抓包重构了该程序，
本人仅在此基础上添加了研究生填报功能并于此添加Action自动运行功能，
特此鸣谢。
