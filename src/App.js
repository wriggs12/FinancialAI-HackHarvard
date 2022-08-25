import { useState } from 'react';
import './App.css';
import banner from './images/FinancialAI_Banner.png';
import Output from './output';

function App() {  

  const [creditScore, setCreditScore] = useState("");
  const [netIncome, setNetIncome] = useState("");
  const [netWorth, setNetWorth] = useState("");
  const [age, setAge] = useState("");
  const [savings, setSavings] = useState("");
  const [retirement, setRetirement] = useState("");
  const [creditLimit, setCreditLimit] = useState("");
  
  const [income, setIncome] = useState(0);
  const [expenses, setExpenses] = useState(0);

  const [isAppOpen, setIsAppOpen] = useState(true);

  const app = <div>
  <img src={banner} className="mainBanner" alt="Financial AI Logo"/>
  <div className="textbox">
    <form method="POST" action="#">
      <div className="banner1">
        <h1 id="h1Main">Credit</h1>
      </div>
      <div className="select-box">
        <label htmlFor="select-box" className="label select-box">
          <span className="label-desc">Choose your credit score: </span>
        </label>
        <select id="select-box" className="select" name="creditScore" value={creditScore} onChange={(e) => setCreditScore(e.target.value)}>
          <option value="1">720 - 850 (Excellent)</option>
          <option value="2">690 - 719 (Good)</option>
          <option value="3">630 - 689 (Fair)</option>
          <option value="4">300 - 629 (Bad)</option>
          <option value="5">No Credit Score</option>
        </select>
      </div>
      <br/>

      <label>Number of Credit Lines: *</label><br/>
      <input type="creditLines" name="creditLines" placeholder="Credit Lines" required/>
      <br/>
      <br/>

      <label>Current Credit Limit: *</label><br/>
      <input type="creditLimit" name="creditLimit" placeholder="Credit Limit" required value={creditLimit} onChange={(e) => setCreditLimit(e.target.value)} />
      <br/>
      <br/>

      <label>Amount of Credit Debt: *</label><br/>
      <input type="creditDebt" name="creditDebt" placeholder="Credit Debt" required/>
      <br/>

      <div className="banner">
        <h1 id="h1Main">Investments and Savings</h1>
      </div>

      <label>Monthly Income: *</label><br/>
      <input type="income" name="income" placeholder="Income" required value={income} onChange={(e) => {setIncome(e.target.value); setNetIncome(income - expenses); }}/>
      <br/>
      <br/>

      <label>Essential Monthly Expenses: *</label><br/>
      <input type="expense" name="expenses" placeholder="Expenses" required value={expenses} onChange={(e) => {setExpenses(e.target.value); setNetIncome(income - expenses); }}/>
      <br/>
      <br/>

      <label>Amount in Savings: *</label><br/>
      <input type="savings" name="savings" placeholder="Savings" required value={savings} onChange={(e) => setSavings(e.target.value)}/>
      <br/>
      <br/>

      <label>Amount in Retirement Accounts: *</label><br/>
      <input type="retirement" name="retirement" placeholder="Retirement" required value={retirement} onChange={(e) => setRetirement(e.target.value)}/>
      <br/>
      <br/>

      <label>Total Amount Invested: *</label><br/>
      <input type="investments" name="investments" placeholder="Investments" required/>
      <br/>
      <br/>

      <label>Age: *</label><br/>
      <input type="age" name="age" placeholder="Age" required value={age} onChange={(e) => setAge(e.target.value)}/>
      <br/>

      <div className="banner">
        <h1 id="h1Main">Net Worth</h1>
      </div>

      <label>Total Wealth: *</label><br/>
        <input type="wealth" name="wealth" placeholder="Wealth" required value={netWorth} onChange={(e) => setNetWorth(e.target.value)}/>
      <br/>
      <br/>

      <label>Total Debt: *</label><br/>
      <input type="debt" name="debt" placeholder="Debt" required/>

      <div className="btn-block"><br/>
        <button type="button" onClick={() => setIsAppOpen(false)}>CHECK</button>
      </div>
    </form>
  </div>
  <footer style={{textAlign: "center"}}>
    &copy; Copyright <strong><span>FinancialAI</span></strong><br/>All Rights Reserved
    <p style={{color: "gray", fontSize: "13px"}}>Designed and developed in New York</p>
  </footer>
</div>;

  return (
    isAppOpen ? app :
    <Output setIsAppOpen={setIsAppOpen} creditScore={creditScore} netIncome={netIncome} netWorth={netWorth} age={age} savings={savings} totalRetirement={retirement} expenses={expenses} creditLimit={creditLimit} />
  );
}

export default App;
