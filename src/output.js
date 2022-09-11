import "./output.css";
import "./App.css";
import amex from "./images/amex.png";
import capitalone from "./images/capital_one.png";
import chase from "./images/chase.png";
import citi from "./images/citi_bank.png";
import deserve from "./images/deserve.png";
import discover from "./images/discover.png";
import fizz from "./images/fizz.png"
import wellsfargo from "./images/wells_fargo.png"

function Output({setIsAppOpen, creditScore, netIncome, netWorth, age, savings, totalRetirement, expenses, creditLimit}) {
    function getAvgNetWorth() {
        if (age < 35) {
            return "$76,340";
        }
        else if (age < 45) {
            return "$437,770";
        }
        else if (age < 55) {
            return "$833,790";
        }
        else if (age < 65) {
            return "$1,176,520";
        }
        else if (age < 75) {
            return "$1,215,920";
        }

        return "$958,450";
        
    }
    
    function getCreditCardRecommendations() {
        const cards = [['name','credit_low','credit_high','cash_back','annual_fee', 'img', 'link'],
                ['Discover it Student Cash', 630, 689, '1% - 5%', '$0', discover, 'https://www.discover.com/products/student-it-af.html?sc=RJUK&cmpgnid=ls-dca-ir-student-it-RJUK-dtop-980&irgwc=1&gclid=_m22kcu6hiskf6h6ss911j6p6022xreznspp0nowb00&sid=04664157&pid=170911&aid=568217&source=Affiliates&sku=110'],
                ['Discover it Student Chrome', 630, 689, '1% - 2%', '$0', discover, 'https://www.discover.com/products/student-chrome-af.html?sc=RJUL&cmpgnid=ls-dca-ir-student-chrome-RJUL-dtop-980&irgwc=1&gclid=_m22kcu6hiskf6h6ss911j6p6022xreznu1p0nowb00&sid=04664157&pid=170911&aid=568217&source=Affiliates&sku=111'],
                ['Chase Freedom Student', 690, 850, '1%', '$0', chase, 'https://creditcards.chase.com/a1/freedom/studentcard?CELL=640K&AFFID=SWlnSnn6x54-tarYaA_TSfri5n8dXhULCg&pvid=fd33d953c3b24f2e912cd95b8bbdfc1e&jp_cmp=cc/857932/aff/15-31557/na'],
                ['Deserve Student', 630, 850, '1%', '$0', deserve, 'https://www.deserve.com/apply-for-deserve/?utm_source=NerdWallet&utm_campaign=Edu&utm_medium=hasoffers&utm_offer={deserve_offer_id}&utm_content=AP-NerdWallet_EDU-001&pid=DESERVE_EDU&mode={mode}&dtxid=102f66a52ca4a886d077e442dcaa59&dafid=1019&dofid=23&dgid=&dafref=NerdWallet&dofref=Edu&dofurl=0&dfil={file_id}&dofil=0&dip=98.7.80.155&dts=2021-10-09+23%3A49%3A30&dmc=%3F&dafcid=&dafsub=c28f29d5daed4026a2793927cc71f999&dafsub2=&dafsub3=&dafsub4=&dafsub5=AP-NerdWallet_EDU-001&dafun1=&dafun2=&dafun3=&dafun4=&dafun5=&dcity=New%20York&dreg=NY&dcc=US'],
                ['Discover it Secured', 0, 850, '1% - 2%', '$0', discover, 'https://www.discover.com/products/secured-card-af.html?sc=GEGX&cmpgnid=ls-dca-ir-secured-GEGX-980&irgwc=1&gclid=_m22kcu6hiskf6h6ss911j6p6022xrezi9hp0nowb00&sid=04664157&pid=170911&aid=568217&source=Affiliates&sku=109'],
                ['Capital One Platinum Secured', 0, 850, 'N/A', '$0', capitalone, 'https://applynow.capitalone.com/?irgwc=1&external_id=IRAFF_ZZ9d92fcbfbf374f00bd2dddd57bd2a0cb_USCIR_K170911_A344893L_C2a20401bN297d11ec9caee92be815501_S_P&transid=&marketingChannel=P23235&productId=13728'],
                ['Chase Freedom Unlimited', 690, 850, '1.5% - 5%', '$0', chase, 'https://creditcards.chase.com/a1/freedom-unlimited/affiliates2021g?CELL=6H8X&AFFID=SWlnSnn6x54-1MBAJU4lHrteyd0jWp2FRQ&pvid=7135d748ca734cdd939fa52c6e66f3a6&jp_cmp=cc/993749/aff/15-31543/na'],
                ['Citi Custom Cash', 690, 850, '1% - 5%', '$0', citi, 'https://citicards.citi.com/usc/LPACA/Citi/Cards/CustomCash/External_HC2/index.html?BTData=N2U.B.gAB6f.J.Bzk.SDci.X88.lRG.BJ.xAX.Bj.Tj.2l.E&HKOP=944512e2c9a63143a898080d03e67a1b2c591af82233b4e5075e4db39fdc5adf&cmp=afa|acquire|2003|nerdwallet&ranMID=44660&ranEAID=2955213&ranSiteID=SWlnSnn6x54-oXefW_4ZLrqU5SdTPGp.AA&ProspectID=4979CEAF77FC4DE6B6188D2B0D26C910'],
                ['Chase Sapphire Preferred', 690, 850, '1% - 5%', '$95', chase, 'https://creditcards.chase.com/a1/21Q4/sapphirepreferred/compare/onecta?CELL=6H8X&AFFID=SWlnSnn6x54-rU.zbcxzyX1VXfRgfg9RJA&pvid=39ee211bc8304db186881e3c7a760d3a&jp_cmp=cc/993749/aff/15-31593/na'],
                ['Amex Blue Cash Preferred', 690, 850, '1% - 6%', '$95', amex, 'https://www.americanexpress.com/us/credit-cards/card/blue-cash-preferred/?eep=26129&linknav=US-Acq-Shop-Consumer-VAC-Prospect-ViewCardDetail-BCP&irgwc=1&veid=3VUV3B2t9xyIT0l2t-RrFXUXUkBXpc11u0FkRI0&affid=1193684&pid=IR&affname=NerdWallet%2C%20Inc.&sid=14011830016&pmc=796&BUID=CCG&CRTV=controlaffcps&MPR=03'],
                ['Fizz Credit', 0, 850, 'N/A', '$0', fizz, 'https://www.joinfizz.com/'],
                ['Wells Fargo Active Cash', 690, 850, '2%', '$0', wellsfargo, 'https://creditcards.wellsfargo.com/cards/active-cash-credit-card?product_code=CC&subproduct_code=AC&vendor_code=LS&sub_channel=AFF&siteID=SWlnSnn6x54-3VQuMj3kGfiqtbgrcz7OEA&WFSPAT=VQNNR3']];

            var recommendation = [];

            if (parseInt(creditScore) > 2)
                if (parseInt(creditScore) > 3)
                    recommendation = [cards[5], cards[6], cards[11]];
                else
                    recommendation = [cards[1], cards[2], cards[4]];
            else if (parseInt(creditLimit) < 5000)
                recommendation = [cards[3], cards[7], cards[12]];
            else
                recommendation = [cards[8], cards[9], cards[10]];

        return <div>
        <a href={recommendation[0][6]} target="_blank" rel="noreferrer noopener">
            <div className="card">
                <h1>
                    {
                        recommendation[0][0]
                    }
                </h1>
                <div className="imgContain">
                    <img src={recommendation[0][5]} alt="Credit Card Logo" />
                </div>
                <h3>
                    Annual Fee: {recommendation[0][4]}
                    <br />
                    CashBack: {recommendation[0][3]}
                </h3>
            </div>
        </a>
        <a href={recommendation[1][6]} target="_blank" rel="noreferrer noopener">
            <div className="card">
                <h1>
                    {
                        recommendation[1][0]
                    }
                </h1>
                <div className="imgContain">
                    <img src={recommendation[1][5]} alt="Credit Card Logo" />
                </div>
                <h3>
                    Annual Fee: {recommendation[1][4]}
                    <br />
                    CashBack: {recommendation[1][3]}
                </h3>
            </div>
        </a>
        <a href={recommendation[2][6]} target="_blank" rel="noreferrer noopener">
            <div className="card">
                <h1>
                    {
                        recommendation[2][0]
                    }
                </h1>
                <div className="imgContain">
                    <img src={recommendation[2][5]} alt="Credit Card Logo" />
                </div>
                <h3>
                    Annual Fee: {recommendation[2][4]}
                    <br />
                    CashBack: {recommendation[2][3]}
                </h3>
            </div>
        </a>
        </div>
    }

    function getSavingsRecommendation() {
        const minSavings = expenses * 3;
        const maxSavings = expenses * 6;
        let rec = <div></div>;

        if (parseInt(savings) < minSavings) {
            rec = <h3>You need more savings! Try and budget to build up some savings in case of an emergency. It is best to have around 3-6 months of expenses in savings as an emergency fund.</h3>;
        }
        else if (parseInt(savings) > maxSavings) {
            rec = <h3>You have too much in savings. You want to keep around 3-6 months of expenses in savings as an emergency fund. Putting money into savings actually costs money because of inflation. It's better to put the excess into investments.</h3>;
        }
        else {
            rec = <h3>Your savings look great! Try and keep around 3-6 months of expenses in savings as an emergency fund.</h3>;
        }
        
        return rec;
    }

    function getRetirementPrediction() {
        const yearsLeft = 65 - age;
        const annualRate = .1188;

        const ans = Math.round((totalRetirement * Math.pow(1 + annualRate, yearsLeft)) * 100) / 100;
        
        const res = `If the current amount is invested into an S&P 500 index fund, at 65 years old the account value will be $${ans}`;

        return res;
    }

    return (
            <div className="content">
                <h1 id="name">Financial AI</h1>
                <div className="overview">
                    <div className="bubble">
                        <h1>Your Credit Score</h1>
                        <h3>{creditScore}</h3>
                        <p>A good credit score gets you good interest rates on loans</p>
                    </div>
                    <div className="bubble">
                        <h1>Net Monthly Income</h1>
                        <h3>{netIncome}</h3>
                        <p>Net income is what you can use to grow your wealth over time</p>
                    </div>
                    <div className="bubble">
                        <h1>Your Net Worth</h1>
                        <h3>{netWorth}</h3>
                        <p>The average net worth for your age group is {getAvgNetWorth()}</p>
                    </div>
                </div>
                <div className="creditCards">
                    <h1>A Few Credit Card Recommendations</h1>
                    {
                        getCreditCardRecommendations()
                    }
                </div>
                <div className="money">
                    <div className="save">
                        <h1>Savings</h1>
                        <h2>Currently Saved : ${savings}</h2>
                        {
                            getSavingsRecommendation()
                        }
                    </div>
                    <div className="save">
                        <h1>Retirement</h1>
                        <h2>Current Retirement: ${totalRetirement}</h2>
                        {
                            getRetirementPrediction()
                        }
                    </div>
                </div>
                <button onClick={() => setIsAppOpen(true)}>Back</button>
            </div>
    );
}

export default Output;








// def inflationSection(inflationRate):
// section = '<div class="inflation">' \
//           '<h1>Inflation</h1>' \
//           '<h1>Machine Learning Inflation Prediction: '

// section += str(inflationRate)
// section += '%</h1>' \
//            '<h2>According to our machine learning model, your money will lose '

// section += str(inflationRate)
// section += '% next year.<br>To counteract this you can invest in the stock market, real estate, or commodities.</h2>' \
//            '<h2>S&P 500 2020 Return: 18.4%</h2>' \
//            '<h2>Average Real Estate 2020 Return: 11.6%</h2>' \
//            '<h2>Gold 2020 Return: 28%</h2>' \
//            '</div>' \
//            '</div>'

// return section