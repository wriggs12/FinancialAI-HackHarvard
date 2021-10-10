from django.http import HttpResponse
from django.shortcuts import render
import requests
import csv
import pandas as pd
from sklearn import tree

def index(request):
    if (request.method == 'POST'):
        return output(request)
    return render(request, 'index.html')

def output(request):
    creditScore = request.POST.get('creditScore','')
    creditLine = request.POST.get('creditLines','')
    creditLimit = request.POST.get('creditLimit', '')
    creditDebt = request.POST.get('creditDebt', '')
    income = request.POST.get('income', '')
    expenses = request.POST.get('expenses', '')
    savings = request.POST.get('savings', '')
    retirement = request.POST.get('retirement', '')
    totalIvestments = request.POST.get('investments', '')
    age = request.POST.get('age', '')
    wealth = request.POST.get('wealth', '')
    debt = request.POST.get('debt', '')

    amex = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/American_Express_logo_%282018%29.svg/1200px-American_Express_logo_%282018%29.svg.png'
    capitalOne = 'https://logos-world.net/wp-content/uploads/2021/04/Capital-One-Logo.png'
    chase = 'https://logodownload.org/wp-content/uploads/2021/04/chase-logo-1.png'
    citiBank = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Citi.svg/1200px-Citi.svg.png'
    deserve = 'https://www.insart.com/wp-content/uploads/Deserve.png'
    discover = 'https://1000logos.net/wp-content/uploads/2021/05/Discover-logo.png'
    fizz = 'https://uploads-ssl.webflow.com/60f9992abb0c4bd8b15b2240/61003408879dc5cf3533040c_FIzz.png'
    wellsFargo = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Wells_Fargo_Bank.svg/1024px-Wells_Fargo_Bank.svg.png'

    images = [amex, capitalOne, chase, citiBank, deserve, discover, fizz, wellsFargo]

    newPage = '<!DOCTYPE html>' \
              '<html lang="en">' \
              '<head>' \
              '<meta charset="utf-8">' \
              '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">' \
              '<meta name="description" content="">' \
              '<title>Financial AI</title>' \
              '<link rel="shortcut icon" type="image/jpg" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjPzoOm3_5AkBtG7ZQ93qYTJQUYwTcwa57xg&usqp=CAU" />' \
              '</head>' \
              '<style>' \
              'html {' \
              'font-family: sans-serif;' \
              'color: #555555;' \
              'background-color: #203354;' \
              '}' \
              'a {' \
              'text-decoration: none;' \
              'color: #555555;' \
              '}' \
              '#name {' \
              'color: white;' \
              '}' \
              '.content {' \
              'text-align: center;' \
              '}' \
              '.overview {' \
              'width: 100%;' \
              'text-align: center;' \
              '}' \
              '.bubble {' \
              'border-radius: 5px;' \
              'border: 1px solid grey;' \
              'padding: 1em;' \
              'margin: auto 3em;' \
              'display: inline-block;' \
              'width: 20em;' \
              'margin-top: 3em;' \
              'background-color: #f5f5f5;' \
              '}' \
              '.creditCards {' \
              'width: 90%;' \
              'background-color: #f5f5f5;' \
              'border-radius: 5px;' \
              'border: 1px solid grey;' \
              'margin: 3em auto;' \
              'height: 38em;' \
              '}' \
              '.card {' \
              'display: inline-block;' \
              'margin: auto 3em;' \
              'border-radius: 5px;' \
              'border: 1px solid grey;' \
              'padding: 1em;' \
              'width: 20em;' \
              'height: 75%;' \
              'overflow: hidden;' \
              'position: relative;' \
              '}' \
              '.money {' \
              'height: 15em;' \
              'margin-bottom: 6em;' \
              '}' \
              '.save {' \
              'border: 1px solid grey;' \
              'display: inline-block;' \
              'margin: auto 3em;' \
              'border-radius: 5px;' \
              'padding: 1em;' \
              'background-color: #f5f5f5;' \
              'width: 35em;' \
              'height: 100%;' \
              'overflow: hidden;' \
              'position: relative;' \
              '}' \
              '.inflation {' \
              'width: 90%;' \
              'border-radius: 5px;' \
              'border: 1px solid grey;' \
              'margin: 3em auto;' \
              'height: 24em;' \
              '}' \
              '.card img {' \
              'width: 15em;' \
              '}' \
              '.imgContain {' \
              'height: 15em;' \
              '}' \
              '.inflation {' \
              'background-color: #f5f5f5;' \
              '}' \
              'form {' \
              'text-align: center;' \
              '}' \
              'form a {' \
              'border: none;' \
              'padding: 16px 32px;' \
              'background-color: #f5f5f5; ' \
              'font-size: 16px;' \
              'transition-duration: 0.4s;' \
              'cursor: pointer;' \
              'border-radius: 5px;' \
              'text-decoration: none;' \
              'color: black;' \
              '}' \
              'form a:hover {' \
              'background-color: #008CBA;' \
              'color: white;' \
              '}' \
              '</style>' \
              '<body>' \
              '<div class="content">' \
              '<h1 id="name">Financial AI</h1>' \
              '<div class="overview">' \
              '<div class="bubble">' \
              '<h1>Your Credit Score</h1>' \
              '<h3>'

    scoreBijection = {'1': '720 - 850 (Excellent)', '2': '690 - 719 (Good)', '3': '630 - 689 (Fair)', '4': '300 - 629 (Bad)', '5': 'No Credit'}

    newPage += scoreBijection[creditScore]
    newPage += '</h3>' \
               '<p>' \
               'A good credit score gets you good interest rates on loans' \
               '</p>' \
               '</div>' \
               '<div class="bubble">' \
               '<h1>Net Monthly Income</h1>' \
               '<h3>'

    netIncome = int(income) - int(expenses);
    newPage += '$' + ("{:,}".format(int(netIncome)))
    newPage += '</h3>' \
               '<p>' \
               'Net income is what you can use to grow your wealth over time' \
               '</p>' \
               '</div>' \
               '<div class="bubble">' \
               '<h1>Your Net Worth</h1>' \
               '<h3>'


    netWorth = int(wealth) - int(debt)
    newPage += '$' + ("{:,}".format(int(netWorth)))
    newPage += '</h3>' \
               '<p>'

    newPage += formatNetworth(netWorth, age)

    newPage += '</p>' \
               '</div>' \
               '</div>' \
               '<div class="creditCards">' \
               '<h1>A Few Credit Card Recommendations</h1>'

    newPage += creditCards(creditScore, creditLimit, images)

    newPage += emergencyFund(savings, expenses, retirement, age)

    inflationRate = predictInflation()

    newPage += inflationSection(inflationRate)

    newPage += '<form>' \
               '<a href="http://127.0.0.1:8000/">BACK</a>' \
               '</form>' \
               '<footer>' \
               '&copy; Copyright <strong><span>FinancialAI</span></strong><br>All Rights Reserved' \
               '<p style="color:gray;font-size: 13px;">Designed and developed in New York</p>' \
               '</footer>' \
               '</body>' \
               '</html>'

    return HttpResponse(newPage)

def inflationSection(inflationRate):
    section = '<div class="inflation">' \
              '<h1>Inflation</h1>' \
              '<h1>Machine Learning Inflation Prediciton: '

    section += str(inflationRate)
    section += '%</h1>' \
               '<h2>According to our machine learning model, your money will loose '

    section += str(inflationRate)
    section += '% next year.<br>To counter act this you can invest in the stock market, real estate, or commodities.</h2>' \
               '<h2>S&P 500 2020 Return: 18.4%</h2>' \
               '<h2>Average Real Estate 2020 Return: 11.6%</h2>' \
               '<h2>Gold 2020 Return: 28%</h2>' \
               '</div>' \
               '</div>'

    return section

def emergencyFund(savings, expenses, retirement, age):
    minSaved = int(expenses) * 3
    maxSaved = int(expenses) * 6

    saveSection = '<div class="money">' \
                  '<div class="save">' \
                  '<h1>Savings</h1>' \
                  '<h2>Currently Saved: $'

    saveSection += ("{:,}".format(int(savings)))
    saveSection += '</h2>'

    if (int(savings) > int(maxSaved)):
        saveSection += '<h3>You have too much in savings. You want to keep around 3-6 months of expenses in savings as an emergency ' \
               'fund. Putting money into savings actually costs money because of inflation. It\'s better to put the excess in to investments.</h3>'
    elif (int(savings) > int(minSaved)):
        saveSection += '<h3>Your savings look great! Try and keep around 3-6 months of expenses in savings as an emergency fund.</h3>'
    elif (int(savings) < int(minSaved)):
        saveSection += '<h3>You need more savings! Try and budget to build up some savings in case of an emergency. It is best to have' \
               'around 3-6 months of expenses in savings as an emergency fund.</h3>'

    saveSection += '</div>' \
                   '<div class="save">' \
                   '<h1>Retirement</h1>' \
                   '<h2>Current Retirement: $'

    saveSection += ("{:,}".format(int(retirement)))
    saveSection += '</h2>' \
                   '<h3>' \
                   'If current amount is invested into an S&P 500 index fund, at 65 years old the account value will be:<br>'
    saveSection += '$' + compound(age, retirement)

    saveSection += '</h3>' \
                   '</div>' \
                   '</div>'

    return saveSection

def compound(age, retirement):
    amount = float(retirement)
    for i in range (65 - int(age)):
        amount *= 1.15
    integerAmount = int(amount * 100)
    floatAmount = float(integerAmount) / 100

    finalNum = "{:,}".format(floatAmount)

    return finalNum

def formatNetworth(netWorth, age):
    avgWorthByAge = [[0, 34, '$76,340'],
                     [35, 44, '$437,770'],
                     [45, 54, '$833,790'],
                     [55, 64, '$1,176,520'],
                     [65, 74, '$1,215,920'],
                     [75, 200, '$958,450']]

    for i in range(5):
        if (int(age) >= avgWorthByAge[i][0] & int(age) <= avgWorthByAge[i][1]):
            return 'The average net worth for your age group is ' + avgWorthByAge[i][2]

def creditCards(creditScore, creditLimit, images):
    cards = [['name','credit_low','credit_high','cash_back','annual_fee', 'img', 'link'],
             ['Discover it Student Cash', 630, 689, '1% - 5%', '$0', images[5], 'https://www.discover.com/products/student-it-af.html?sc=RJUK&cmpgnid=ls-dca-ir-student-it-RJUK-dtop-980&irgwc=1&gclid=_m22kcu6hiskf6h6ss911j6p6022xreznspp0nowb00&sid=04664157&pid=170911&aid=568217&source=Affiliates&sku=110'],
             ['Discover it Student Chrome', 630, 689, '1% - 2%', '$0', images[5], 'https://www.discover.com/products/student-chrome-af.html?sc=RJUL&cmpgnid=ls-dca-ir-student-chrome-RJUL-dtop-980&irgwc=1&gclid=_m22kcu6hiskf6h6ss911j6p6022xreznu1p0nowb00&sid=04664157&pid=170911&aid=568217&source=Affiliates&sku=111'],
             ['Chase Freedom Student', 690, 850, '1%', '$0', images[2], 'https://creditcards.chase.com/a1/freedom/studentcard?CELL=640K&AFFID=SWlnSnn6x54-tarYaA_TSfri5n8dXhULCg&pvid=fd33d953c3b24f2e912cd95b8bbdfc1e&jp_cmp=cc/857932/aff/15-31557/na'],
             ['Deserve Student', 630, 850, '1%', '$0', images[4], 'https://www.deserve.com/apply-for-deserve/?utm_source=NerdWallet&utm_campaign=Edu&utm_medium=hasoffers&utm_offer={deserve_offer_id}&utm_content=AP-NerdWallet_EDU-001&pid=DESERVE_EDU&mode={mode}&dtxid=102f66a52ca4a886d077e442dcaa59&dafid=1019&dofid=23&dgid=&dafref=NerdWallet&dofref=Edu&dofurl=0&dfil={file_id}&dofil=0&dip=98.7.80.155&dts=2021-10-09+23%3A49%3A30&dmc=%3F&dafcid=&dafsub=c28f29d5daed4026a2793927cc71f999&dafsub2=&dafsub3=&dafsub4=&dafsub5=AP-NerdWallet_EDU-001&dafun1=&dafun2=&dafun3=&dafun4=&dafun5=&dcity=New%20York&dreg=NY&dcc=US'],
             ['Discover it Secured', 0, 850, '1% - 2%', '$0', images[5], 'https://www.discover.com/products/secured-card-af.html?sc=GEGX&cmpgnid=ls-dca-ir-secured-GEGX-980&irgwc=1&gclid=_m22kcu6hiskf6h6ss911j6p6022xrezi9hp0nowb00&sid=04664157&pid=170911&aid=568217&source=Affiliates&sku=109'],
             ['Capital One<br>Platinum Secured', 0, 850, 'N/A', '$0', images[1], 'https://applynow.capitalone.com/?irgwc=1&external_id=IRAFF_ZZ9d92fcbfbf374f00bd2dddd57bd2a0cb_USCIR_K170911_A344893L_C2a20401bN297d11ec9caee92be815501_S_P&transid=&marketingChannel=P23235&productId=13728'],
             ['Chase Freedom Unlimited', 690, 850, '1.5% - 5%', '$0', images[2], 'https://creditcards.chase.com/a1/freedom-unlimited/affiliates2021g?CELL=6H8X&AFFID=SWlnSnn6x54-1MBAJU4lHrteyd0jWp2FRQ&pvid=7135d748ca734cdd939fa52c6e66f3a6&jp_cmp=cc/993749/aff/15-31543/na'],
             ['Citi Custom Cash', 690, 850, '1% - 5%', '$0', images[3], 'https://citicards.citi.com/usc/LPACA/Citi/Cards/CustomCash/External_HC2/index.html?BTData=N2U.B.gAB6f.J.Bzk.SDci.X88.lRG.BJ.xAX.Bj.Tj.2l.E&HKOP=944512e2c9a63143a898080d03e67a1b2c591af82233b4e5075e4db39fdc5adf&cmp=afa|acquire|2003|nerdwallet&ranMID=44660&ranEAID=2955213&ranSiteID=SWlnSnn6x54-oXefW_4ZLrqU5SdTPGp.AA&ProspectID=4979CEAF77FC4DE6B6188D2B0D26C910'],
             ['Chase Sapphire Preferred', 690, 850, '1% - 5%', '$95', images[2], 'https://creditcards.chase.com/a1/21Q4/sapphirepreferred/compare/onecta?CELL=6H8X&AFFID=SWlnSnn6x54-rU.zbcxzyX1VXfRgfg9RJA&pvid=39ee211bc8304db186881e3c7a760d3a&jp_cmp=cc/993749/aff/15-31593/na'],
             ['Amex Blue Cash Preferred', 690, 850, '1% - 6%', '$95', images[0], 'https://www.americanexpress.com/us/credit-cards/card/blue-cash-preferred/?eep=26129&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-BCP&irgwc=1&veid=3VUV3B2t9xyIT0l2t-RrFXUXUkBXpc11u0FkRI0&affid=1193684&pid=IR&affname=NerdWallet%2C%20Inc.&sid=14011830016&pmc=796&BUID=CCG&CRTV=controlaffcps&MPR=03'],
             ['Fizz Credit', 0, 850, 'N/A', '$0', images[6], 'https://www.joinfizz.com/'],
             ['Wells Fargo Active Cash', 690, 850, '2%', '$0', images[7], 'https://creditcards.wellsfargo.com/cards/active-cash-credit-card?product_code=CC&subproduct_code=AC&vendor_code=LS&sub_channel=AFF&siteID=SWlnSnn6x54-3VQuMj3kGfiqtbgrcz7OEA&WFSPAT=VQNNR3']]

    if (int(creditScore) > 2):
        if (int(creditScore) > 3):
            recommendation = [cards[5], cards[6], cards[11]]
        else:
            recommendation = [cards[1], cards[2], cards[4]]
    elif (int(creditLimit) < 5000):
        recommendation = [cards[3], cards[7], cards[12]]
    else:
        recommendation = [cards[8], cards[9], cards[10]]

    cardSection = ''

    for card in recommendation:
        cardSection += '<a href="'
        cardSection += card[6]
        cardSection += '" target="_blank">' \
                       '<div class="card">' \
                       '<h1>'
        cardSection += card[0]
        cardSection += '</h1>' \
                       '<div class="imgContain"><img src="'
        cardSection += card[5]
        cardSection += '" /></div>' \
                       '<h3>Annaul Fee: '

        cardSection += card[4]
        cardSection += '<br>CashBack: '
        cardSection += card[3]
        cardSection += '</h3>' \
                       '</a>' \
                       '</div>'

    cardSection += '</div>'

    return cardSection

def prepData():
    cpi = getData(
        'https://data.nasdaq.com/api/v3/datasets/FRED/CPIAUCSL?start_date=2000-01-01&end_date=2020-12-01&api_key=',
        'Q_EPkoyWXDoQhyLL_YTv')
    gdp = getData('https://data.nasdaq.com/api/v3/datasets/FRED/GDP?start_date=2000-01-01&end_date=2020-12-01&api_key=',
                  'Q_EPkoyWXDoQhyLL_YTv')
    realGDP = getData(
        'https://data.nasdaq.com/api/v3/datasets/FRED/GDPC1?start_date=2000-01-01&end_date=2020-12-01&api_key=',
        'Q_EPkoyWXDoQhyLL_YTv')
    m1v = getData('https://data.nasdaq.com/api/v3/datasets/FRED/M1V?start_date=2000-01-01&end_date=2020-12-01&api_key=',
                  'Q_EPkoyWXDoQhyLL_YTv')
    m2v = getData('https://data.nasdaq.com/api/v3/datasets/FRED/M2V?start_date=2000-01-01&end_date=2020-12-01&api_key=',
                  'Q_EPkoyWXDoQhyLL_YTv')
    ffRate = getData(
        'https://data.nasdaq.com/api/v3/datasets/FRED/DFF?start_date=2000-01-01&end_date=2020-12-01&api_key=',
        'Q_EPkoyWXDoQhyLL_YTv')
    unemployRate = getData(
        'https://data.nasdaq.com/api/v3/datasets/FRED/UNRATE?start_date=2000-01-01&end_date=2020-12-01&api_key=',
        'Q_EPkoyWXDoQhyLL_YTv')
    fedDebt = getData(
        'https://data.nasdaq.com/api/v3/datasets/FRED/GFDEBTN?start_date=2000-01-01&end_date=2020-12-01&api_key=',
        'Q_EPkoyWXDoQhyLL_YTv')

    with open('econ_data.csv', 'w', newline='') as d:
        writer = csv.writer(d)

        writer.writerow(['cpi', 'gdp', 'real_gdp', 'm1v', 'm2v', 'ff_rate', 'un_rate', 'fed_debt'])

        cpiData = []
        gdpData = []
        realGdpData = []
        m1vData = []
        m2vData = []
        ffRateData = []
        unRateData = []
        fedDebtData = []

        for data in cpi['dataset']['data']:
            if(data[0][5:] == '01-01' or data[0][5:] == '04-01' or data[0][5:] == '07-01' or data[0][5:] == '10-01'):
                cpiData.append(data[1])

        for data in gdp['dataset']['data']:
            if(data[0][5:] == '01-01' or data[0][5:] == '04-01' or data[0][5:] == '07-01' or data[0][5:] == '10-01'):
                gdpData.append(data[1])

        for data in realGDP['dataset']['data']:
            if(data[0][5:] == '01-01' or data[0][5:] == '04-01' or data[0][5:] == '07-01' or data[0][5:] == '10-01'):
                realGdpData.append(data[1])

        for data in m1v['dataset']['data']:
            if(data[0][5:] == '01-01' or data[0][5:] == '04-01' or data[0][5:] == '07-01' or data[0][5:] == '10-01'):
                m1vData.append(data[1])

        for data in m2v['dataset']['data']:
            if(data[0][5:] == '01-01' or data[0][5:] == '04-01' or data[0][5:] == '07-01' or data[0][5:] == '10-01'):
                m2vData.append(data[1])

        for data in ffRate['dataset']['data']:
            if(data[0][5:] == '01-01' or data[0][5:] == '04-01' or data[0][5:] == '07-01' or data[0][5:] == '10-01'):
                ffRateData.append(data[1])

        for data in unemployRate['dataset']['data']:
            if(data[0][5:] == '01-01' or data[0][5:] == '04-01' or data[0][5:] == '07-01' or data[0][5:] == '10-01'):
                unRateData.append(data[1])

        for data in fedDebt['dataset']['data']:
            if(data[0][5:] == '01-01' or data[0][5:] == '04-01' or data[0][5:] == '07-01' or data[0][5:] == '10-01'):
                fedDebtData.append(data[1])

        for i in range(len(cpiData)):
            writer.writerow(
                [int(cpiData[i]), int(gdpData[i]), int(realGdpData[i]), int(m1vData[i]) * 100, int(m2vData[i]) * 100,
                 int(ffRateData[i]) * 100, int(unRateData[i]) * 100, int(fedDebtData[i])])


def getData(url, key):
    url = url + key
    f = requests.get(url)
    return f.json()

def trainModel(features, labels):
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(features, labels)

    d = {'gdp': [22300],
         'real_gdp': [19550],
         'm1v': [119],
         'm2v': [112],
         'ff_rate': [6],
         'un_rate': [590],
         'fed_debt': [29000000]}
    df = pd.DataFrame(data = d)

    prediction = classifier.predict(df)



    curCPI = 255

    inflation = int((((prediction / curCPI) - 1) * 100) * 4)

    return inflation

def predictInflation():
    prepData()
    data = pd.read_csv('econ_data.csv')

    labels = data.pop('cpi')
    features = data

    return trainModel(features, labels)