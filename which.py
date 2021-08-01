# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from urllib import request
import time
import requests
import re
import json

def content_zhihu():
    url_main = "http://www.zhihu.com/"
    url_topic="https://www.zhihu.com/question/39821720"
    url_answer="http://www.zhihu.com/question/39821720/answer/83531838"
    url_api="https://www.zhihu.com/api/v4/questions/39821720/answers"
    #url_batch="https://zhihu-web-analytics.zhihu.com/api/v2/za/logs/batch"
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",

        "Cookie": "_zap=ea672ba5-0b97-4545-9ffc-bcef47a5e504; d_c0=ADBfp0-LZxOPTnJnXwkm9hM29Ero7AiW1Ig=|1626146247;_xsrf=yfitydicizzt8j64TgrEuv4Ey7UFDJ8X; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1626146247,1627616257; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1627616257; SESSIONID=yBX6HBxiXsnir5CRoRzvYiXjmxSnucaoXLtl0BAJ2eC; __snaker__id=38aPLaZ3ppC3M4j7; JOID=W1gQA0zqNMKS9nc1XuMDUCgBDE9BmnOfo7A8SDK8Tqn-g0x_CeRAw_rxezVc8yz9E67nnrbDcdsizmaNQ-ryzis=; osd=VlkRB07nNcOW9Ho0X-cBXSkACE1Mm3Kbob09STa-Q6j_h05yCOVEwffwejFe_i38F6zqn7fHc9Yjz2KPTuvzyik=; gdxidpyhxdE=oD%2BAGHEJrTP%5CZylXeytw9%2BihZGtfDGHSYB%5CdsWYTsLtTqoY8MJ40LgV7ILroa%2FmK5xpczDYo2uIVc7k7CUeQYMa5%2B9eAnRYrVdpiX0s5V%5CAG8GOEpn6BypvbI%2BVbP%2FrgQ7RX%5CRDJgWXBx93klN83dSo%2FQ2eXv%2ByPaJ6abfUR4qYJH3Vr%3A1627617159002; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=egAWkt3Tn967Vvp%2B3Z7xyR%2BIqiBH9j4viUFVY1SUsoSq3Jy010cHQ1ho%2FjdnBZ9cNtMKg%2B%2BHXjnK1XCY8dUMgxhM1GYjftk825qiXsLey%2B75yjo6TloSWJqENTEwPXPhNmM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee89f66ef29ffe8af260f7868ea2c45b928a8b85f5738db0a6acf470a1e9a9b5e92af0fea7c3b92aa7b98fb8ea80f18ca2dab53d96aac0ccb252f5a8b7b3aa43b3b78ea9bc62f8aaa7b6c55e9bef9db6f26591affdabfc3cf3f0ada9d43bacb1e18be7668286f784cd808f95a9ccaa449cb6a2acb4548187f885d847a5a8a8aeb44d9bb6aa95ea34f2ebbf8adb7990bbb7ccb63fbbb6a1d7d768ad8d99abf44f8e8c8b98d35494b8828ed037e2a3; YD00517437729195%3AWM_TID=HfcC8%2F8TlQlEUVQEFBY63L9iLqdYvgTj; captcha_session_v2=2|1:0|10:1627616309|18:captcha_session_v2|88:UlBraXdycm83Sm9DREQ1V0NHVGhydnRBSkQwTWFHaDllejhoVDJRbnNYWVNDc2tTU0VqOTdhZURPSmpRZExoeg==|6c1838c4acf941fcb52ddd2c7d1ba00024b1138ffb475d80de7909af6f7c0d5a; captcha_ticket_v2=2|1:0|10:1627616641|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfbHA3aG1WaTRiamRxb3djdEN3MlFpZ3owZmZ4LTZCUGd4TS14NkJ4VDE4UlZqQmhubG1jbFhuZGlPcXItaXhmbkh4alpSRHJlYTdjMEgwUC4ydmVybDJ2OFlWSmphNUNuLW1FQWJleTdKdUItanpsbm9OYThPb29FYXN5YTd0aC5GZ1V5MlFSb2RRVkgxOEotaG82MXRuX0IxT1FxZFV6ZnprSlpKSHNFZTkuTHdZaE1tTFQybGFYTEtzN0lWZW5jVTU3R25YUGVNeGV3dnFKOTFsRHFJYlM0cHZzendHaEhZQlN4cnZEdGNzekg5R2t3T2tENms4V2txMVFmOG5jYTBKaVpGSUh1YVhuTzFUd3gwY1c0cFllVUFGOGlaVjViOGxWaGcxb1B0ZXg1VU5HZ3RsSkdTWF9MYkhkSXJWdC4yX2xBMlFVVWNBSWFmYjB5Z0VZd28yRVZNcEs2SWEuWjVkdDhRTUhzNmtlT1VnOFExa1NyWmtzYmVpRFNFVUZ5Q2VFQXZrWmtmUXJGbmFNLXBncGxhVm55ckZmb0xrNzBxdmE5RGgwOUkwanhlY3FyWjBMWXdQLlNSbUR5LVhlUWU0eF81dWp5aEN1VmsyZ200VGJ0YklsdGlIWnFXbG5uUk10S04wUTlTMkY4VUxPNmNzTFFydHV3ODhyMyJ9|b588622985f835c04d54d3f4604f1c4d13059dc0b21af548b1c19f24f0b5f89d; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1627616654|1627616256; z_c0=2|1:0|10:1627616654|4:z_c0|92:Mi4xQ1FTREVBQUFBQUFBTUYtblQ0dG5FeVlBQUFCZ0FsVk5qc1B3WVFBUUxmYXhYTy0xTmVXQ2RFYndHbVlWV1E0c0Rn|06ae364500fd7e432b6a12659ba40731510738e1fec365c31cbbaaa11f9dbdd0; unlock_ticket=AEDtTpFTog8mAAAAYAJVTZZ8A2E0X-1er8DV1rHQnOEp5WqZFJnDBQ=="
    }
    req = request.Request(url_topic, headers=headers)
    response = request.urlopen(req).read().decode()
    print(response)

def html_zhihu():               #每次5个输出某问题下的答案
    global answer_num
    url_topic = "https://www.zhihu.com/question/39821720"
    url_api="https://www.zhihu.com/api/v4/questions/39821720/answers"
    #有哪些阴暗不适
    url_now1="https://www.zhihu.com/api/v4/questions/39821720/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=3&platform=desktop&sort_by=default"
    #有哪些能吓尿的恐怖游戏
    url_now2="https://www.zhihu.com/api/v4/questions/27519062/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default"
    #你玩过最恐怖的单机游戏是什么？
    url_now="https://www.zhihu.com/api/v4/questions/25579367/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default"
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",

        "Cookie": "_zap=ea672ba5-0b97-4545-9ffc-bcef47a5e504; d_c0=ADBfp0-LZxOPTnJnXwkm9hM29Ero7AiW1Ig=|1626146247;_xsrf=yfitydicizzt8j64TgrEuv4Ey7UFDJ8X; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1626146247,1627616257; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1627616257; SESSIONID=yBX6HBxiXsnir5CRoRzvYiXjmxSnucaoXLtl0BAJ2eC; __snaker__id=38aPLaZ3ppC3M4j7; JOID=W1gQA0zqNMKS9nc1XuMDUCgBDE9BmnOfo7A8SDK8Tqn-g0x_CeRAw_rxezVc8yz9E67nnrbDcdsizmaNQ-ryzis=; osd=VlkRB07nNcOW9Ho0X-cBXSkACE1Mm3Kbob09STa-Q6j_h05yCOVEwffwejFe_i38F6zqn7fHc9Yjz2KPTuvzyik=; gdxidpyhxdE=oD%2BAGHEJrTP%5CZylXeytw9%2BihZGtfDGHSYB%5CdsWYTsLtTqoY8MJ40LgV7ILroa%2FmK5xpczDYo2uIVc7k7CUeQYMa5%2B9eAnRYrVdpiX0s5V%5CAG8GOEpn6BypvbI%2BVbP%2FrgQ7RX%5CRDJgWXBx93klN83dSo%2FQ2eXv%2ByPaJ6abfUR4qYJH3Vr%3A1627617159002; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=egAWkt3Tn967Vvp%2B3Z7xyR%2BIqiBH9j4viUFVY1SUsoSq3Jy010cHQ1ho%2FjdnBZ9cNtMKg%2B%2BHXjnK1XCY8dUMgxhM1GYjftk825qiXsLey%2B75yjo6TloSWJqENTEwPXPhNmM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee89f66ef29ffe8af260f7868ea2c45b928a8b85f5738db0a6acf470a1e9a9b5e92af0fea7c3b92aa7b98fb8ea80f18ca2dab53d96aac0ccb252f5a8b7b3aa43b3b78ea9bc62f8aaa7b6c55e9bef9db6f26591affdabfc3cf3f0ada9d43bacb1e18be7668286f784cd808f95a9ccaa449cb6a2acb4548187f885d847a5a8a8aeb44d9bb6aa95ea34f2ebbf8adb7990bbb7ccb63fbbb6a1d7d768ad8d99abf44f8e8c8b98d35494b8828ed037e2a3; YD00517437729195%3AWM_TID=HfcC8%2F8TlQlEUVQEFBY63L9iLqdYvgTj; captcha_session_v2=2|1:0|10:1627616309|18:captcha_session_v2|88:UlBraXdycm83Sm9DREQ1V0NHVGhydnRBSkQwTWFHaDllejhoVDJRbnNYWVNDc2tTU0VqOTdhZURPSmpRZExoeg==|6c1838c4acf941fcb52ddd2c7d1ba00024b1138ffb475d80de7909af6f7c0d5a; captcha_ticket_v2=2|1:0|10:1627616641|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfbHA3aG1WaTRiamRxb3djdEN3MlFpZ3owZmZ4LTZCUGd4TS14NkJ4VDE4UlZqQmhubG1jbFhuZGlPcXItaXhmbkh4alpSRHJlYTdjMEgwUC4ydmVybDJ2OFlWSmphNUNuLW1FQWJleTdKdUItanpsbm9OYThPb29FYXN5YTd0aC5GZ1V5MlFSb2RRVkgxOEotaG82MXRuX0IxT1FxZFV6ZnprSlpKSHNFZTkuTHdZaE1tTFQybGFYTEtzN0lWZW5jVTU3R25YUGVNeGV3dnFKOTFsRHFJYlM0cHZzendHaEhZQlN4cnZEdGNzekg5R2t3T2tENms4V2txMVFmOG5jYTBKaVpGSUh1YVhuTzFUd3gwY1c0cFllVUFGOGlaVjViOGxWaGcxb1B0ZXg1VU5HZ3RsSkdTWF9MYkhkSXJWdC4yX2xBMlFVVWNBSWFmYjB5Z0VZd28yRVZNcEs2SWEuWjVkdDhRTUhzNmtlT1VnOFExa1NyWmtzYmVpRFNFVUZ5Q2VFQXZrWmtmUXJGbmFNLXBncGxhVm55ckZmb0xrNzBxdmE5RGgwOUkwanhlY3FyWjBMWXdQLlNSbUR5LVhlUWU0eF81dWp5aEN1VmsyZ200VGJ0YklsdGlIWnFXbG5uUk10S04wUTlTMkY4VUxPNmNzTFFydHV3ODhyMyJ9|b588622985f835c04d54d3f4604f1c4d13059dc0b21af548b1c19f24f0b5f89d; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1627616654|1627616256; z_c0=2|1:0|10:1627616654|4:z_c0|92:Mi4xQ1FTREVBQUFBQUFBTUYtblQ0dG5FeVlBQUFCZ0FsVk5qc1B3WVFBUUxmYXhYTy0xTmVXQ2RFYndHbVlWV1E0c0Rn|06ae364500fd7e432b6a12659ba40731510738e1fec365c31cbbaaa11f9dbdd0; unlock_ticket=AEDtTpFTog8mAAAAYAJVTZZ8A2E0X-1er8DV1rHQnOEp5WqZFJnDBQ=="
    }
    i=0
    while(1):
        req = requests.get(url_now, headers=headers).json()
        analyze_answer(req,url_now)     #截取内容并输出
        time.sleep(10)          #以防被反爬
        if req["paging"]["is_end"] == 'true' or answer_num >= req["paging"]["totals"]:
            print("已爬完。\n当前回答数："+str(answer_num)+"\n当前网址："+url_now)
            break
        url_now=req["paging"]["next"]
        i+=1


answer_num=0
record_headless=[]
def analyze_answer(res,url):
    global answer_num
    for story in res["data"]:
        answer_num+=1
        content=story["content"]
        p_find=["无头女","没有头","眨眼频率"]    #泪目！！！终于找到了！！！！！叫which
        #p_find=['outlast','魔女之家','b站']
        for key_word in p_find:
            if re.search(key_word, content) is not None :
                content = content.replace("<br/>", '\n')
                content = content.replace('。', '。\n')
                content = re.sub("<.*?>", '', content)
                print("******************"+url+"*******************\n")
                print('答案' + str(answer_num) + ':关键词：'+key_word+'\n' + content + '\n\n')
                break
            elif answer_num%5==0:
                content = content.replace("<br/>", '\n')
                content = content.replace('。', '。\n')
                content = re.sub("<.*?>", '', content)
                print('解闷' + str(answer_num) + ':\n' + content + '\n\n')
                break
    #print(res["paging"])
    pattern1="^content"


if __name__ == '__main__':
    #content_zhihu()
    html_zhihu()



