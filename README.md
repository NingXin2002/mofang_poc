# mofang_poc
魔方网表存在文件上传漏洞

 python mofang_exp.py -h   

                    ) (`-.            ) (`-.
             ( OO ).           ( OO ).
            (_/.  \_)-. ,-.-')(_/.  \_)-. ,-.-')
             \  `.'  /  |  |OO)\  `.'  /  |  |OO)
              \     /\  |  |  \ \     /\  |  |  \
               \   \ |  |  |(_/  \   \ |  |  |(_/
              .'    \_),|  |_.' .'    \_),|  |_.'
             /  .'.  \(_|  |   /  .'.  \(_|  |
            '--'   '--' `--'  '--'   '--' `--'

usage: mofang_exp.py [-h] [-u URL] [-f FILE] [-exp EXP]  

魔方网表存在文件上传漏洞 

optional arguments:  
  -h, --help            show this help message and exit  
  -u URL, --url URL     添加url信息  
  -f FILE, --file FILE  添加txt文件  
  -exp EXP, --exp EXP   写入webshell  

example:  
        python3 mofang_exp.py.py -u http://xxxx.xxxx.xxxx.xxxx  
        python3 mofang_exp.py -f x_url.txt  
        python3 mofang_exp.py -exp 1  
