import operator

from django.shortcuts import render


# Create your views here.


def word_count(request):
    return render(request, "word_count.html")


def count(request):
    text = request.GET['wordcount']
    words = text.split(" ")
    words_frequency = {}
    for word in words:
        if word in words_frequency:
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1
    #sorting a list
    # sorted(words_frequency.items(), key=operator.itemgetter(1), reverse=True)
    sorte = sorted(words_frequency.items(), key= operator.itemgetter(1),reverse=True)
    return render(request, "count.html", {"words": len(words), "wordf": sorte})
