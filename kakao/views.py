from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from faq.models import Answer

btns = {
    'type': 'buttons',
    'buttons': ['최신글 보기','검색','사이트 이동']
}

def keyboard(request):
    return JsonResponse(btns)

@csrf_exempt
def message(request):
    if request.body:
        json_str = ((request.body).decode('utf-8'))
        received_json_data = json.loads(json_str)
        input_text = received_json_data['content']
    else:
        input_text = ''

    message_button = { 'label':'사이트 이동', 'url': 'http://kkoon.duckdns.org:8000' }
    if input_text == '최신글 보기':
        latest_answer_list = Answer.objects.filter(is_display__exact=1).order_by('-create_date')[:6]
        if latest_answer_list:
            msg = '최근에 등록된 5개 글입니다.\n\n' + '\n'.join('* ' + e.title for e in latest_answer_list)
        else :
            msg = '등록된 글이 없습니다.'
        
        return_msg = {
            'text': msg,
            'message_button': message_button
        }
    elif input_text == '검색':
        return_msg = { 'text':'아직 준비중인 기능입니다.' }

    elif input_text == '사이트 이동':
        return_msg = { 
            'text': '아래 버튼을 누르면 헬프데스크 사이트로 이동합니다.',
            'message_button': message_button
        }
    else:
        return_msg = { 
            'text': '이해할 수 없는 명령입니다.'
        }

    return_json = {
            'message': return_msg,
            'keyboard': btns,
    }
    return JsonResponse(return_json)