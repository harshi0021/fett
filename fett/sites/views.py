from django.shortcuts import render
from email import header
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from django.http.response import JsonResponse
import json, requests
from cleantext import clean


# Create your views here.

@api_view(['GET'])
def freelancerView(request):
   headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
   #freelancer_url = requests.get("https://www.freelancer.com/jobs/?fixed_min=0&status=all&fixed_max=1000&hourly_duration=2",headers)
   freelancer_url = requests.get("https://www.freelancer.com/jobs/?fixed_min=0&fixed_max=1000&hourly_duration=1")
   #print(Indeed_url)
   freelacne_soup = BeautifulSoup(freelancer_url.content, 'html.parser')
   freelacne_heading=freelacne_soup.findAll('div', {"class":"JobSearchCard-primary"})
   freelacne_heading = freelacne_heading[2:]
   freelance_data = []
   
   
   for sth in freelacne_heading:
         freelance_data.append(sth.text)
         a=clean(text=freelance_data,
            fix_unicode=True,
            to_ascii=True,
            lower=True,
            no_line_breaks=True,
            no_urls=False,
            no_emails=False,
            no_phone_numbers=False,
            no_numbers=False,
            no_digits=False,
            no_currency_symbols=False,
            no_punct=False,
            replace_with_punct="",
            replace_with_url="This is a URL",
            replace_with_email="Email",
            replace_with_phone_number="",
            replace_with_number="123",
            replace_with_digit="0",
            replace_with_currency_symbol="$",
            lang="en"
            )
   return JsonResponse(
         {"data_from_freelance_web":a},
         safe=False)




