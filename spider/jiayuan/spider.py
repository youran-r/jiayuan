# -*- coding=utf8 -*-
from urllib import urlencode
from requests import Session
from extension import mongo_collection
import json
import time

session = Session()
LOGIN_HEADERS = {
    'Host': 'passport.jiayuan.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'Origin': 'http://www.jiayuan.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.jiayuan.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Cookie': 'PHPSESSID=a61fceea4f562be57a6e2228bd2c412d; save_jy_login_name=18516993537; DATE_SHOW_LOC=11; DATE_SHOW_SHOP=1; UM_distinctid=15fd2f5008c189-07f561d3247488-178123e-100200-15fd2f5008d7d7; btnuserid=; DATE_FROM=daohang; IM_CON=%7B%22IM_TM%22%3A1511072879886%2C%22IM_SN%22%3A3%7D; IM_S=%7B%22IM_CID%22%3A8479159%2C%22IM_SV%22%3A%22123.59.161.5%22%2C%22svc%22%3A%7B%22code%22%3A0%2C%22nps%22%3A0%2C%22unread_count%22%3A%220%22%2C%22ocu%22%3A0%2C%22ppc%22%3A0%2C%22jpc%22%3A0%2C%22regt%22%3A%221511072724%22%2C%22using%22%3A%22%22%2C%22user_type%22%3A%2210%22%2C%22uid%22%3A170733826%7D%2C%22m%22%3A0%2C%22f%22%3A0%2C%22omc%22%3A0%7D; IM_M=%5B%5D; stadate1=169733826; myloc=11%7C1101; myage=31; mysex=m; myuid=169733826; myincome=40; w_uk=20171119qBp54Yb1t64; buyhistory_v2=%257B%252242%2522%253A%257B%2522pid%2522%253A%252242%2522%252C%2522url%2522%253A%2522%255C%252Fusercp%255C%252Fservice%255C%252Fdo_package_service.php%253Frid%253D1530%2522%252C%2522pname%2522%253A%2522%255Cu94bb%255Cu77f3%255Cu4f1a%255Cu545812%255Cu4e2a%255Cu6708%255Cu7acb%255Cu51cf400%255Cu5143%2522%252C%2522time%2522%253A1511073659%257D%257D; IM_TK=1511097087455; SESSION_HASH=4379cca81704eca50aabdc8b6f37673e5cbef066; user_access=1; pclog=%7B%22170733826%22%3A%221511144185076%7C1%7C0%22%7D; IM_ID=9; IM_CS=1; _gscu_1380850711=111628362jnu5c13; _gscbrs_1380850711=1; REG_ST_ID=15; REG_ST_URL=https://www.baidu.com/link?url=o0CPVzuBDLJMt0_7Qph1Tz50z0cI-1p4bYMBWsZfSWviwLU1W_OVQn8LtufqGGvB&wd=&eqid=de178f9f0002dcb5000000035a112171; REG_REF_URL=https://www.baidu.com/link?url=o0CPVzuBDLJMt0_7Qph1Tz50z0cI-1p4bYMBWsZfSWviwLU1W_OVQn8LtufqGGvB&wd=&eqid=de178f9f0002dcb5000000035a112171',
}
SEARCH_HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'search.jiayuan.com',
    'Origin': 'http://search.jiayuan.com',
    'Pragma': 'no-cache',
    'Referer': 'http://search.jiayuan.com/v2/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def login():
    data = {
        'name': '佳缘账户',
        'password': '登陆密码',
        'channel' : 200,
        'position' : 201,
        'remem_pass': 'on',
    }
    response = session.post('https://passport.jiayuan.com/dologin.php?host=www.jiayuan.com&new_header=1&channel=index',
                            headers=LOGIN_HEADERS, data=urlencode(data))
    assert response.ok


def con():
    age = {
        '2_1': '20.25',
        '2_2': '25.30',
        '2_3': '30.35',
        '2_4': '35.40',
    }
    height = {
        '3_2': '160.165',
        '3_3': '165.170',
        '3_4': '170.175',
        '3_1': '155.160',
        '3_5': '175.180',
    }
    edu = {
        '4_4': '40',
        '4_5': '50',
        '4_3': '30',
        '4_1': '10',
        '4_2': '20',
        '4_6': '60',
        '4_7': '70',
    }
    money = {
        '5_4': '40',
        '5_1': '10',
        '5_2': '20',
        '5_5': '50',
        '5_3': '30',
    }
    is_marry = {
        '6_1': '1',
        '6_2': '2',
        '6_3': '3',
        '6_4': '4',
        '6_5': '5',
        '6_6': '6',
    }
    arr = []
    for (m_k,m_v) in money.items():
        m_key = m_k.split('_')[0]
        for (h_k,h_v) in height.items():
            h_key = h_k.split('_')[0]
            for (e_k,e_v) in edu.items():
                e_key = e_k.split('_')[0]
                for (a_k,a_v) in age.items():
                    a_key = a_k.split('_')[0]
                    for (i_k,i_v) in is_marry.items():
                        i_key = i_k.split('_')[0]
                        sstr = a_key+':'+a_v+','+h_key+':'+h_v+','+e_key+':'+e_v+','+m_key+':'+m_v+','+i_key+':'+i_v
                        arr.append(sstr)
    return arr
    
def search_con():
    arr_con = con()
    for each in arr_con:
        print 'condition stc: {}' . format(each)
        for page in xrange(1, 50):
            data = {
                'p': page,
                'sex': 'f',
                'stc': each,
            }
            print 'current_page:{}'.format(page)
            response = session.post('http://search.jiayuan.com/v2/search_v2.php',
                                    headers=SEARCH_HEADERS, data=urlencode(data))
            if not response.ok:
                print 'page:{} failed'.format(page)
                continue

            users = response.json()['userInfo']
            if not users:
                print 'get emtpy data'
                break;
            for user in users:
                dt = mongo_collection.find_one({'uid': user['uid']})
                if not dt:
                    mongo_collection.insert(user)
                else:
                    print '{} had existed.'.format(user['uid'])
            time.sleep(0.5)

if __name__ == '__main__':
    #登陆
    login()
    #抓取数据
    search_con()
