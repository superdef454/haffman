from django.shortcuts import render
from django.http import JsonResponse
import json
from .encode import haffman_in_json
from .shared_memory import Shared
import sys

def home(request):
    ip = request.META["REMOTE_ADDR"]
    return render(request, "base.html")

last_json = ''

def algorithm(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request).get('data')
            global last_json
            last_json = haffman_in_json(data)
            out = {
                "unshifr":data,
                "shifr": last_json,
            }
            print(sys.getsizeof(data))
            print(round(sys.getsizeof(last_json)/ 2 - 0.1, 3))
            return JsonResponse(out)

def send_mess(request):
    global last_json
    if last_json:
        Shared(last_json)
    return JsonResponse({})























































# def decode(request):
#     is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
#     if is_ajax:
#         if request.method == 'POST':
#             data = json.load(request).get('data')
#             out = {
#                 "shifr":data,
#                 # "shifr": haffman_in_json(data),
#             }
#             return JsonResponse(out)