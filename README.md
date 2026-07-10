# montecarlo-sample
Takes historical sample of returns from any ticker and runs a montecarlo simulation to predict possible future outcomes

This is my first of many future finance related projects built using python. It draws from a distribution of log returns of any ticker across any amount of time and samples from returns using average rate of positive vs negetive trades to create many branching possibilities for the stocks future.

This project utilized yfinance for ticker data and matplotlib for graphing. In the future I will experiment with using libraries like numpy and pandas for more advanced work but the basic tools of python worked aproprietly for a simple project such as this

# future of this projct
1. I would like to move it out of log space because it is more useful to see actual price data rather than log returns on the final output
2. I would like to add more metrics other than average % of positive outcomes, such as average draw down, and average return
3. It is possible to create an actual statistcally backed distribution rather than draw from previous returns which would likely yeild marginally better results

# Why did I build this
I built this as a milestone project of starting to learn python. Python is not my first programming language but it is the most widely used in the quantitative finance industry and while building in low level languages like c++ is valuable, java is not used commonly. This project helped me understand the convenience of using python and how quickly a simple project can be built due to the simplicity of the language.
