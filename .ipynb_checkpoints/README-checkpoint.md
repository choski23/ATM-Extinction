# Are Automatic Teller Machines (ATM) going extinct?

Access to financial services leads to more inclusion in the economy which is great for everyone.  With so many digital payment options such as venmo, square, zelle, and paypal to name a few, I wanted to see how this impacted the consumer's need for physical cash.  ATMs are a popular way to access cash and this project will explore global trends on ATM availability.

# Data Sources
I gathered data through World Bank's Open Data on 233 Countries, 6 Regions, with data from 2004-2019.  I focused on the following development indicators as potential variables that could impact ATMs per 100,000:
&nbsp;
*GDP
&nbsp;
*GDP per capita
&nbsp;
*GDP Growth (annual percentage)
&nbsp;
*Mobile subscriptions per 100,000


# Background
The first ATM debuted over 50 years ago and there are about 4 million in circulation today.  The ATM functionality has evolved over time from simply dispensing cash using a physical card to many more advanced functions today such was deposits, bitcoin transfers, and mobile phone access.

On one hand, the explosion of mobile payment options, peer to peer payments, and online shopping likely contribute to decreasing demand for cash.  On the other hand, more physical banks are closing with increased functionality and other fintech development which may drive more customers to ATMs for banking needs.   

# Exploratory Data Analysis
In my first step in exploratory data analysis, I wanted to see how ATMs were distributed around the world. The graph below shows ATM availability by region over the last 15 years.  North America had more than twice that of the European Union and was left off for scale.  It was interesting to see that most regions are actually increasing the number ATMs.

![ATM Availability by Region](/img/ATM%20Availability%20by%20Region.png)

I wanted to see if GDP had any impact on the ATM availability so I broke the data into three equal GDP categories - Small, Medium and Large.  I applied a best fit line which also shows an positive increase over time for all three categories  

![ATM by GDP Category](/img/ATM%20per%20100,000%20by%20GDP%20Category%20Scatterplot.png)

ATMs are utilized at the consumer level so I wanted to consider the data by GDP per capita and look at the mean and variance of each subset. The histogram below shows that the larger GDP per capita countries have the largest variance and more ATMs per 100,000

![ATM by GDP Per Capita Category](/img/ATM%20per%20100,000%20by%20GDP%20Per%20Capita%20Quantile%20Combined%20Histogram.png)

&nbsp;
I would think the variables could have a different impact based on the GDP size so I plotted each variable against the ATM availability to look for any correlations. 

![Small GDP Correlations](/img/Small%20GDP%20Correlations%20Scatter%20Matrix.png)
&nbsp;

![Medium GDP Correlations](/img/Medium%20GDP%20Correlations%20Scatter%20Matrix.png)
&nbsp;

![Large GDP Correlations](/img/Large%20GDP%20Correlations%20Scatter%20Matrix.png)

&nbsp;

I couldn't ascertain any obvious correlation and decided to utilize a partial regression plot to incorporate all the variables to help predict ATM availability.  

![Partial Regression Plot to Predict ATM Availability](/img/World%20Correlations%20Scatter%20-%20Partial%20Regression.png)

&nbsp;
The variable with the greatest beta coefficient was the GDP Growth by Annual Percentage indicating the highest correlation. Upon further analysis this variable had the greatest impact on a Large GDP Country.  Because GDP Annual growth is generally single digits, the range for the confidence interval increases in larger numbers in this model.  If the GDP growth percentage is negative, it could indicate a rise in ATM availability.

![Large GDP Growth Annual Percentage as a Predictor for ATM per 100,000](/img/Large%20GDP%20Growth%20Annual%20Percentage%20as%20a%20Predictor%20for%20ATM%20per%20100,000.png)

# Conclusion



# Next Steps
