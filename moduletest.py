print("How much was your bill?")
bill = (int(input()))
print(''' "How were the services?
Good
Great
Terrible?"''')
rating = str(input())
print(rating)
if rating == "good":
    Tip = (0.15*bill)
elif rating == "great":
    Tip = (0.2*bill)
else:
    rating == "terrible"
    Tip = (0),

print("You should tip " + str(Tip) + " KES")
