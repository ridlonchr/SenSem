
donation = 300
my_range = range(donation)
total = 0
for i in my_range:
    total += i

deduction = total*.05
print "Donations total: ", total
print "Average Donation: ", (total/300)
print "Deduction: ", deduction
print "Gross: ", (total - deduction)

print "\n.05 each transaction"
total_deduc = 0
total = 0
for i in my_range:
    deduction = i * .05
    total_deduc += deduction
    total = total + (i-deduction)


print "Donations total: ", total
print "Average Donation: ", (total/300)
print "Deduction: ", total_deduc
#print "Gross: ", (total - deduction)
