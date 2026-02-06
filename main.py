#reciept

aitem, aprice = "burger", 60
bitem, bprice = "momo" , 40
citem, cprice = "coffee" , 80
ditem, dprice = "pizza" , 150

restname = "Raathi Restaraunt"
restaddress = "DD PURAM CANT"
restcity = "BAREILLY"

messege = "thankyou sir"

print("*"*50)

print("\t\t{}".format(restname.title()))
print("\t\t  {}".format(restaddress))
print("\t\t     {}".format(restcity))
print("*"*50)

print("\tproduct name \tproduct price")
print("\t{}\t\t₹{}".format(aitem.title(), aprice))
print("\t{}\t\t₹{}".format(bitem.title(), bprice))
print("\t{}\t\t₹{}".format(citem.title(), cprice))
print("\t{}\t\t₹{}".format(ditem.title(), dprice))

print("="*50)

print("\t\t\ttotal")

total = aprice + bprice + cprice + dprice
print("\t\t\t₹{}".format(total))

print("="*50)

print("\n\t\t{}\n".format(messege))

print("*"*50)
