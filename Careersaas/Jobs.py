import requests

cookies = {
    'PHPSESSID': '9d31982e1ab49589a3a751dd8cae8854',
    '_gid': 'GA1.2.996993134.1612540943',
    '__zlcmid': '12Vjmy3vhmpjL7C',
    '_ga_D2X3MB9R6R': 'GS1.1.1612632562.4.1.1612632563.0',
    '_ga': 'GA1.2.81353456.1612540943',
    '_gat_gtag_UA_154680923_1': '1',
}
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://app.careersaas.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://app.careersaas.com/portal/job-search.html',
    'Accept-Language': 'en-GB,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,en-US;q=0.6',
}
data = {
  'draw': '2',
  'columns^%^5B0^%^5D^%^5Bdata^%^5D': 'LOGO',
  'columns^%^5B0^%^5D^%^5Bname^%^5D': '',
  'columns^%^5B0^%^5D^%^5Bsearchable^%^5D': 'true',
  'columns^%^5B0^%^5D^%^5Borderable^%^5D': 'false',
  'columns^%^5B0^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D': '',
  'columns^%^5B0^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D': 'false',
  'columns^%^5B1^%^5D^%^5Bdata^%^5D': 'BUTTON',
  'columns^%^5B1^%^5D^%^5Bname^%^5D': '',
  'columns^%^5B1^%^5D^%^5Bsearchable^%^5D': 'true',
  'columns^%^5B1^%^5D^%^5Borderable^%^5D': 'false',
  'columns^%^5B1^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D': '',
  'columns^%^5B1^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D': 'false',
  'columns^%^5B2^%^5D^%^5Bdata^%^5D': 'A',
  'columns^%^5B2^%^5D^%^5Bname^%^5D': '',
  'columns^%^5B2^%^5D^%^5Bsearchable^%^5D': 'true',
  'columns^%^5B2^%^5D^%^5Borderable^%^5D': 'false',
  'columns^%^5B2^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D': '',
  'columns^%^5B2^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D': 'false',
  'columns^%^5B3^%^5D^%^5Bdata^%^5D': 'B',
  'columns^%^5B3^%^5D^%^5Bname^%^5D': '',
  'columns^%^5B3^%^5D^%^5Bsearchable^%^5D': 'true',
  'columns^%^5B3^%^5D^%^5Borderable^%^5D': 'false',
  'columns^%^5B3^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D': '',
  'columns^%^5B3^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D': 'false',
  'columns^%^5B4^%^5D^%^5Bdata^%^5D': 'C',
  'columns^%^5B4^%^5D^%^5Bname^%^5D': '',
  'columns^%^5B4^%^5D^%^5Bsearchable^%^5D': 'true',
  'columns^%^5B4^%^5D^%^5Borderable^%^5D': 'false',
  'columns^%^5B4^%^5D^%^5Bsearch^%^5D^%^5Bvalue^%^5D': '',
  'columns^%^5B4^%^5D^%^5Bsearch^%^5D^%^5Bregex^%^5D': 'false',
  'start': '0',
  'length': '2000',
  'search^%^5Bvalue^%^5D': '',
  'search^%^5Bregex^%^5D': 'false',
  'options': 'python',
  'options2': ''
}
response1 = requests.post('https://app.careersaas.com/portal/search/search_jobs.html', headers=headers, cookies=cookies, data=data)
response = requests.post('https://app.careersaas.com/portal/search/search_jobs.html', headers=headers, cookies=cookies, data=data).json()

response_data = response['data']

profession_dict = {}


def get_profession(response_item):
    response_profession = response_item['A']
    return get_substring(response_profession, 'title="', '">')


def get_substring(string, start, end):
    return string[string.find(start)+len(start):string.find(end)]


def get_professions():
    profession_list = []
    for i in range(len(response_data)-1):
        profession_list.append(get_profession(response_data[i]))
    return profession_list


def count_profession(professions):
    for profession in professions:
        #if "python" in profession.lower():
        if "python" not in profession.lower():
            if profession in profession_dict.keys():
                profession_dict[profession] += 1
            else:
                profession_dict[profession] = 1


count_profession(get_professions())

