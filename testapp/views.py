from django.shortcuts import render

# Create your views here.
def home__page__view(request):
    return render(request,'testapp/home.html')

def movie__news__view(request):
    news1='in devadas movie is not good'
    news2='salman updates 100% movie is hit'
    news3='priyanka chopra is getting married to jones'
    news4='varun movie is relesed in tommarrrow'
    news5='venki and varun is f12'
    news6='pawan is gabbarsingh'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5,'news6':news6}
    return render(request,'testapp/mnews.html',my_dict)

def sports__news__view(request):
    news1='dhoni isretaired in 2020'
    news2='next 2019 ipl session yuvarajsingh is not played in ipl'
    news3='next ipl session started at march '
    news4='next ipl session teams mubai indians,chennaikings,ddl,rcb'
    news5='mumbai indians captain is rohit sharma'
    news6='chennai superkings captain dhoni'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5,'news6':news6,}
    return render(request,'testapp/snews.html',my_dict)


def political__news__view(request):
    news1='telangana elections is sucessfully.....'
    news2='telagan votings is selected to our cm in kcr'
    news3='kcr is high majarioty of the sirisilla dist in our own distic..'
    news4='kcr suninlaw harish rao is high majariorty of the kondagal'
    news5='ktr is telanga party leader'
    news6='revanth reddy is fired on the cm kcr y becuase is falling on the votings'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5,'news6':news6,}
    return render(request,'testapp/mnews.html',my_dict)
