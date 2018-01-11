# coding=utf-8
'''
Project:读取mysql数据库的数据，转为json格式
'''
import json, MySQLdb,sys
import email, os
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
num = 100
host = '172.28.235.114'
res = 'wangwei@propersoft.cn,hexin@propersoft.cn,shanzheping@propersoft.cn,wangzhiming@propersoft.cn'
#res = 'wangwei@propersoft.cn'
def TableToJson():
    try:
        # 1-7：如何使用python DB API访问数据库流程的
        # 1.创建mysql数据库连接对象connection
        # connection对象支持的方法有cursor(),commit(),rollback(),close()
        conn = MySQLdb.Connect(host=host, user='root', passwd='xxx', db='isj', port=33306, charset='utf8')
        # 2.创建mysql数据库游标对象 cursor
        # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
        cur = conn.cursor()
        cur2 = conn.cursor()
        # 3.编写sql
        processlist = "show full processlist;"
        Threads_running = "SHOW STATUS LIKE '%Threads_running%';"
        # 4.执行sql命令
        # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
        cur.execute(processlist)
	cur2.execute(Threads_running)
        # 5.获取数据
        # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
        # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
        data = cur.fetchall()
        #Threads_running_v = cur2.execute(Threads_running)
        Threads_running_v = cur2.fetchone()
        processlist_v = cur.execute(processlist)
        # print u'fetchall()返回的数据：', data2
        # 6.关闭cursor
        cur.close()
        # 7.关闭connection
        conn.close()
        jsonData = []
        # 循环读取元组数据
        # 将元组数据转换为列表类型，每个条数据元素为字典类型:[{'字段1':'字段1的值','字段2':'字段2的值',...,'字段N:字段N的值'},{第二条数据},...,{第N条数据}]
        for row in data:
            result = {}
            result['Id'] = row[0]
            result['User'] = str(row[1])
            result['Host'] = str(row[2])
            result['db'] = str(row[3])
            result['Command'] = str(row[4])
            result['Time'] = row[5]
            result['State'] = str(row[6])
            result['Info'] = row[7]
            jsonData.append(result)
            # print u'转换为列表字典的原始数据：', jsonData
    except:
        print 'MySQL connect fail...'
    else:
        # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
        # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
        # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
        #jsondatar = json.dumps(jsonData,sort_keys=True,ensure_ascii=False)
        jsondatar = json.dumps(jsonData,sort_keys=True,indent=2)
        # 去除首尾的中括号
        #return jsondatar[1:len(jsondatar) - 1]
    print u'Threads_running:', Threads_running_v[1]	
#    print u'阀值:', num	
    if int(Threads_running_v[1]) > num:
        return 'Threads_running：' + str(Threads_running_v[1]) + '\n' + 'show full processlist：' + str(processlist_v) + '\n\n' + jsondatar
    else:
        return ''
if __name__ == '__main__':
    # 调用函数
    jsonData = TableToJson()
    # 以读写方式w+打开文件，路径前加r，防止字符转义
    if jsonData.strip()!= '':
        #f = open(r'processlistjson', 'w+')
        f = open('/opt/zabbix/result/processlistjson', 'w+')
        # 写数据
        f.write(jsonData)
        # 关闭文件
        f.close()

def sendMail(subject, receivers, cc, content, atts):
    SENDER = 'gdpr@propersoft.cn'
    msg = MIMEMultipart('related')
    msg['Subject'] = unicode(subject, "UTF-8")
    msg['From'] = SENDER
    msg['To'] = receivers
    msg['Cc'] = cc

    # 邮件内容
    if os.path.isfile(content):
        if (content.split('.')[-1] == 'html'):
            cont = MIMEText(open(content).read(), 'html', 'utf-8')
        else:
            cont = MIMEText(open(content).read(), 'plain', 'utf-8')
    else:
        cont = MIMEText(content, 'plain', 'utf-8')
    msg.attach(cont)

    # 构造附件
    if atts != -1 and atts != '':
        for att in atts.split(','):
            os.path.isfile(att)
            name = os.path.basename(att)
            att = MIMEText(open(att).read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            # 将编码方式为utf-8的name，转码为unicode，然后再转成gbk(否则，附件带中文名的话会出现乱码)
            att["Content-Disposition"] = 'attachment; filename=%s' % name.decode('utf-8').encode('gbk')
            msg.attach(att)
    smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com', port=465)
    smtp.login('gdpr@propersoft.cn', '31353260Gdpr')
    for recev in receivers.split(','):
        smtp.sendmail(SENDER, recev, msg.as_string())
    if cc != '':
        for c in cc.split(','):
            smtp.sendmail(SENDER, c, msg.as_string())
    smtp.close()

def main(argv):
    subject = 'MySQL Threads_running 超过 ' + str(num) + ' 在 ' + host + '主机上'
    content = jsonData
    receivers = res
    cc = 'pr@propersoft.cn'
    if jsonData.strip()!= '':
        sendMail(subject, receivers, cc, content, '')

if __name__ == '__main__':
    main(sys.argv)
