from django.http import HttpResponse
from django.shortcuts import render


def punc_remover(s):

    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    ans = ""
    for i in s:
        flag = 1
        for j in punc:
            if i == j:
                flag = 0
        if flag:
            ans += i

    return ans

def convert_capital(s):
    ans = ""
    for i in s:
        ans+=i.upper()
    return ans

def line_remove(s):
    ans = ""
    for i in s:
        if i!="\n" and i!="\r":
            ans+=i
    return ans

def space_remove(s):
    ans = ""
    n=len(s)
    for i in range(0,n-1):
        if s[i]==" " and s[i+1]==" ":
            continue
        else:
            ans+=s[i]

    ans+=s[n-1]
    return ans


def counter(s):
    c=0
    for i in s:
        if i!=" " and i!="\n":
            c=c+1
    return (f"Number of characters in the input is {c}")


def index(request):
    return render(request,'index.html')


def analyze(request):

    # To Get text from Front End

    djtext=request.POST.get('text','default')
    remove_punc = request.POST.get('removepunc', 'off')
    full_capital= request.POST.get('fullcaps', 'off')
    line_delete = request.POST.get('line_remover', 'off')
    slace_del= request.POST.get('delete_space', 'off')
    char_counter= request.POST.get('char_count', 'off')
    if remove_punc=="on":
        params = {
            'purpose': 'Remove the Punctuations',
            'analyzed_text': punc_remover(djtext)
        }
        djtext=punc_remover(djtext)
        # return render(request,'analyze.html',params)


    if full_capital== "on":
        params = {
            'purpose': 'Convert into Capital Letters',
            'analyzed_text': convert_capital(djtext)
        }
        djtext = convert_capital(djtext)
        # return render(request, 'analyze.html', params)

    if line_delete== "on":
        params = {
            'purpose': 'Remove the blank line',
            'analyzed_text': line_remove(djtext)
        }
        djtext = line_remove(djtext)
        # return render(request, 'analyze.html', params)

    if slace_del=="on":
        params = {
            'purpose': 'Remove the Extra Space between the words',
            'analyzed_text': space_remove(djtext)
        }
        djtext = space_remove(djtext)
        # return render(request, 'analyze.html', params)

    elif char_counter=="on":
        params = {
            'purpose': 'To count total number of characters',
            'analyzed_text': counter(djtext)
        }
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Please select any one operation and try again")

    return render(request, 'analyze.html', params)