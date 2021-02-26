from models.customer import Customer

first_name = "dan"
last_name = "retzlaff"
email_address = "glug101@gmail.com"

summary = ''
customer = Customer(first_name, last_name, email_address)
# text = str(customer.formatted())
summary += str(customer.formatted())
print(summary)
print(summary)