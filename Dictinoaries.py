customer = {
    "name" :"prangya",
    "age":"32",
    "is_varified" : True,
    10:False

}
customer["name"] = "lisa"
# print(customer)
# print(customer["name"])
# print(customer.get("name"))
# print(customer.get("Birth year"))
for i in customer:
    print(i, customer[i])
print(customer.keys())
print(customer.values())
print(customer.items())
for t in customer.items():
    k = t [0]
    d = t [1]
    print(k , d)

# or u can write
for t in customer.items():
    k,d = t
    print(k , d)
# or u can write
for k ,d in customer.items():
     print(k , d)    