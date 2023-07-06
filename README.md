# Supplier Optimization
Your Company is aiming to minimize production costs of some goods. During the production process, an essential product P is used, which can be supplied from one of two partners - supplier A and supplier B. Your consultants requested the historical prices of product P from both suppliers A and B, which were provided as monthly averages for the period from February 2018 to March 2020.

Preparing Company Budget for the coming twelve months period, your plan is to purchase the same amount of product P monthly. Choosing the supplier, you noticed, that there were some periods in the past, when it would be more profitable to use supplier A (the prices of product P were lower), and other periods to work with supplier B. For the Budget model you can set some percentage of the goods to be purchased from supplier A (e.g. 60%) and the remaining part from supplier B (e.g. 40%), but this split should be kept consistent for the whole of the twelve months period. The Budget will be used in preparation for the contract negotiations with both suppliers.

Based on the historical prices, is there a particular percentage which will be more profitable to supply from Company A, and the remaining part from Company B? Or maybe it does not matter and you can work just with one of the suppliers?

# Mathematical Statement of the Problem:

Denoting the prices of product P from Company A and Company B as 𝑝𝐴 (USD) and 𝑝𝐵 (USD) respectively, and the volume of the product to be supplied per month as 𝑛 (units), the total cost in USD is given by 𝑓(𝜔) = 𝑝𝐴𝜔 + 𝑝𝐵(1−𝜔), where 0≤𝜔≤1 is the parameter. In the mathematical model, we can set 𝑛=1 as it remains constant over the next twelve months. Thus, the simplified total cost becomes 𝑓(𝜔) = 𝑝𝐴𝜔 + 𝑝𝐵.

Historical prices {𝑝1𝐴,⋯,𝑝𝑘𝐴} and {𝑝1𝐵,⋯,𝑝𝑘𝐵} provide evidence of different periods favoring either 𝜔=1 (𝑝𝑖𝐴<𝑝𝑖𝐵) or 𝜔=0 (𝑝𝑖𝐴>𝑝𝑖𝐵). The goal is to find an 𝜔 value that minimizes costs in the future.

# Solution Approach
This is a standard portfolio management (investment) problem in statistics, where historical prices are used to make investment decisions to maximize profit (minimize costs). The approach is to calculate 𝑓(𝜔) for each historical price 𝑝𝑖𝐴 and 𝑝𝑖𝐵, where 𝑓𝑖(𝜔) = 𝑝𝑖𝐴𝜔 + 𝑝𝑖𝐵(1−𝜔). Taking the average of these values, 𝑓(v) = mean(𝑓𝑖(𝜔)) = 1/𝑘 ∑(𝑘𝑖=1) 𝑓𝑖(𝜔), we aim to minimize the variance 𝑉(𝜔) = 1/𝑘 ∑(𝑘𝑖=1) (𝑓𝑖(𝜔)−𝑓(v))². This variance 𝑉(𝜔) is the objective function to optimize, where 𝜔∈[0,1]. Although we may not fully understand why this function was chosen, it aligns with risk management theory. Statistical theory demonstrates that there exists an 𝜔∈[0,1] that minimizes the variance 𝑉(𝜔) based on the properties of the datasets {𝑝1𝐴,⋯,𝑝𝑘𝐴} and {𝑝1𝐵,⋯,𝑝𝑘𝐵}. Let's upload a dataset and explore finding the minimum point for the function 𝑉(𝜔).

