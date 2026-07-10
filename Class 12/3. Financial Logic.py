sales_dict={"2022":50000,"2023":60000}
profit = {year:sales* 0.15 for year,sales in sales_dict.items()}
print(profit)
