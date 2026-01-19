#write a program to find out which is cheaper approach to buy IPhone 17 pro max.  consider user is going usa should he buy iphone from usa or from india. 


iphone_price_usa_usd = 1199
usa_sales_tax_percent = 8
usd_to_inr_rate = 83


iphone_price_india_inr = 159900


usa_tax_amount_usd = (iphone_price_usa_usd * usa_sales_tax_percent) / 100
usa_total_price_usd = iphone_price_usa_usd + usa_tax_amount_usd
usa_total_price_inr = usa_total_price_usd * usd_to_inr_rate


print("Total cost in USA (INR):", usa_total_price_inr)
print("Total cost in India (INR):", iphone_price_india_inr)


if usa_total_price_inr < iphone_price_india_inr:
    print("Cheaper option is  from USA")
else:
    print("Cheaper option is from India")
