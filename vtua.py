import requests

found = []

cookies = {
    'PHPSESSID': 'cgth29ngpdmq4803mqedpvd933',
}

headers = {
    'Origin': 'http://csn.vtua.gov.lv',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.44',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'http://csn.vtua.gov.lv/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'DNT': '1',
}

for exam_id in range(224692, 324692):
    data = [
        ('action', 'questionList'),
        ('examid', exam_id),
    ]

    response = requests.post('http://csn.vtua.gov.lv/files/exam_questions.php',
                             headers=headers, cookies=cookies, data=data)

    for question in response.json()['exam_questions']:
        if question not in found:
            found.append(question)

            data = [
                ('action', 'examQuestion'),
                ('examid', exam_id),
                ('question_id', question),
                ('lang', 'lv'),
            ]
            response = requests.post('http://csn.vtua.gov.lv/files/exam_questions.php',
                             headers=headers, cookies=cookies, data=data)
            print("{} {}".format(question, response.json()['text']))
            with open('data/{}.json'.format(question), 'wb') as fd:
                for chunk in response.iter_content(chunk_size=128):
                    fd.write(chunk)

    print("\n Total: {}".format(len(found)))
