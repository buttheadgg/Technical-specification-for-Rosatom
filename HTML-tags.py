import requests
from bs4 import BeautifulSoup as BS

URL = 'https://www.greenatom.ru/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'upgrade-insecure-requests': '1',
    'cookie': 'mos_id=CllGxlx+PS20pAxcIuDnAgA=; session-cookie=158b36ec3ea4f5484054ad1fd21407333c874ef0fa4f0c8e34387efd5464a1e9500e2277b0367d71a273e5b46fa0869a; NSC_WBS-QUBG-jo-nptsv-WT-443=ffffffff0951e23245525d5f4f58455e445a4a423660; rheftjdd=rheftjddVal; _ym_uid=1552395093355938562; _ym_d=1552395093; _ym_isad=2'
}

def request_teg(soup):
    tag_count = 0
    attr_tag_count = 0

    for child in soup.recursiveChildGenerator():
        if child.name:
            tag_count += 1
            if child.attrs:
                attr_tag_count += 1
    print('Количество html-тегов:', tag_count)
    print('Количество html-тегов с атрибутами:', attr_tag_count)



if __name__ == '__main__':
    parsing_method = 'html.parser'
    request = requests.get(URL, headers=HEADERS)
    soup = BS(request.text, parsing_method)
    request_teg(soup)
