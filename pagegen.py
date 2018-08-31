import json
from glob import glob

with open("index.html", "w", 1024, 'utf-8') as html_file:
    html_file.write('''
<html>
<head>

<meta http-equiv="X-UA-Compatible" content="IE=9"/>
<meta charset="utf-8">
<title>CSN eksāmens</title>    
<link rel="stylesheet" href="css/csn.css"/>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<style>
.image_zoom {
    width: 100% !important;
    height: 100% !important;
    z-index: 1000;
}
</style>

</head><body>
''')

    for file_name in glob("data/*.json"):
        with open(file_name) as json_file:
            data = json.load(json_file)

            ### TEXT
            html_file.write('''
                <img height=50% onclick="$(this).toggleClass('image_zoom');" src="{img}"; cursor: default;"/>
<div id="ex_left">
    <img id="ex_pic_container" src="{img}"; cursor: default;"/>
    <div id="ex_text_container">
        <div id="test_text"><small>[{file}]</small> {text}</div>
    </div>
</div>
<div id="ex_right">
    <div id="test_table">
        <div id="ex_q_container">'''.format(img=data['picturedata'], file=file_name, text=data['text'], ))

            ### QQQQ
            for idx, val in enumerate(data['answ']):
                addclass = ''
                if data['coransw'] == idx + 1:
                    addclass = ' correct_answer'

                html_file.write('''
                <div id="EX_Q_A{num}" class="ex_q_variant";">{num}</div>
                <div id="EX_Q_B{num}" class="ex_q_question {addclass}";">{ans}</div>
                '''.format(num=idx+1, ans=val, addclass = addclass))

            ### FOOTER
            html_file.write('''
            <button onClick='$(".correct_answer").toggleClass("ex_q_question_neytral_cor")'>Show correct</button>
        </div>
    </div>
</div>
''')
