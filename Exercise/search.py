import csv
# import pandas


f = open('New Relic.csv')
reader = csv.reader(f)
print(reader)
email = ('hari', 'samatha', 'vamshi', 'jose', 'roger', 'keith')
print(email)
data = {}
for row in reader:
    email = row[1].strip().lower()
    # print(email)
    if data.get(email):
        data[email].append(row[0])
    else:
        data[email] = [row[0]]
    #data.append([row[0], row[1].strip().lower()])
    print(email)
# print(data)
# names = data['name']
# email = data['email']

# print(reader)
# # d1 =
#
#


for r in email:
    for i in data:
        if r in i[1]:
            pass
            # print(i)
        else:
            continue
    # for h in d1:
    #     if r in h:
    #         print(h)
