gola_sales = [ 10,20,15,13,9,7,5]

total_sale = [ sale for sale in gola_sales if sale > 10] # list
total_sale = sum( sale for sale in gola_sales if sale > 10) # generator uses ( )
print(total_sale)