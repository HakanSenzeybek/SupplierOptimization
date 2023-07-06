# Supplier Optimization
The Supplier Optimization project aims to minimize production costs for certain goods at Example Company. During the production process, an essential product P is used, which can be supplied by two partners: supplier A and supplier B. Historical price data for product P from both suppliers (averaged monthly) is available for the period from February 2018 to March 2020.

In order to prepare the company budget for the next twelve months, the plan is to purchase a consistent amount of product P monthly. While analyzing the historical data, it was observed that there were periods when it would have been more profitable to use supplier A (due to lower prices), and other periods when supplier B would have been more favorable. The budget model allows setting a percentage of goods to be purchased from supplier A (e.g., 60%) and the remaining portion from supplier B (e.g., 40%). This split remains consistent throughout the entire twelve-month period. The budget will be used in the upcoming contract negotiations with both suppliers.

The goal is to determine whether a particular percentage allocation between Company A and Company B will be more profitable based on historical prices or if it is feasible to work exclusively with one supplier.

# Mathematical Statement of the Problem
Let 𝑝𝐴 (USD) and 𝑝𝐵 (USD) denote the prices of product P from Company A and Company B, respectively. The volume of the product to be supplied per month is denoted as 𝑛 (units). The total cost in USD is given by the function 𝑓(𝜔) = 𝑝𝐴𝜔 + 𝑝𝐵(1−𝜔), where 0 ≤ 𝜔 ≤ 1 is a parameter. Since 𝑛 remains constant over the next twelve months, we can set 𝑛 = 1. Thus, the simplified total cost becomes 𝑓(𝜔) = 𝑝𝐴𝜔 + 𝑝𝐵.

The historical prices {𝑝1𝐴, ⋯, 𝑝𝑘𝐴} and {𝑝1𝐵, ⋯, 𝑝𝑘𝐵} provide evidence of different periods favoring either 𝜔 = 1 (𝑝𝑖𝐴 < 𝑝𝑖𝐵) or 𝜔 = 0 (𝑝𝑖𝐴 > 𝑝𝑖𝐵). The goal is to find an 𝜔 value that minimizes costs in the future.

# Solution Approach
The Supplier Optimization problem can be approached as a standard portfolio management (investment) problem in statistics, where historical prices are used to make investment decisions that aim to maximize profit (minimize costs). The approach involves calculating 𝑓(𝜔) for each historical price 𝑝𝑖𝐴 and 𝑝𝑖𝐵, where 𝑓𝑖(𝜔) = 𝑝𝑖𝐴𝜔 + 𝑝𝑖𝐵(1−𝜔). By taking the average of these values, 𝑓(v) = mean(𝑓𝑖(𝜔)) = 1/𝑘 ∑(𝑘𝑖=1) 𝑓𝑖(𝜔), we aim to minimize the variance 𝑉(𝜔) = 1/𝑘 ∑(𝑘𝑖=1) (𝑓𝑖(𝜔)−𝑓(v))². This variance 𝑉(𝜔) serves as the objective function to optimize, with 𝜔∈[0,1]. While the reason behind choosing this specific function may not be fully understood, it aligns with risk management theory. 

Statistical theory demonstrates that there exists an 𝜔∈[0,1] that minimizes the variance 𝑉(𝜔) based on the properties of the datasets {𝑝1𝐴,⋯,𝑝𝑘𝐴} and {𝑝1𝐵,⋯,𝑝𝑘𝐵}. In order to find this optimal point, we will upload a dataset and explore the process of identifying the minimum point for the function 𝑉(𝜔).

# Result

In this specific example, based on the historical data, the analysis suggests that 𝜔=0.702 is expected to be the most profitable choice for the share between suppliers A and B. This means that planning to source approximately 70.2% of product P from Company A and 29.8% from Company B is likely to minimize costs.

Note that this is a simplified example with only one parameter, resulting in optimization of a function of one variable. In more complex scenarios, such as machine learning models with hundreds of parameters, optimizing the objective function becomes computationally expensive. However, for this Supplier Optimization problem, it is computationally feasible to evaluate the function in multiple points to find the minimum with a desired level of accuracy.

Feel free to adjust the number of historical data points (N) to improve the accuracy of the optimization.
