import csv


fo = open('OrganizationsExport.csv')
fo1 = open('Tricore_account_numbers_in_CMS (5).csv')
fo2 = open('CMSTricore.csv')

reader = csv.reader(fo)
reader1 = csv.reader(fo1)
reader2 = csv.reader(fo2)

data = {}
num = []
for r in reader2:
    num.append(r[0])
for i in reader:
    data[i[1]] = i[0]

writer = csv.writer(open('temp1.csv', 'w'), delimiter=',')
writer2 = csv.writer(open('temp2.csv', 'w'), delimiter=',')
writer3 = csv.writer(open('temp3.csv', 'w'), delimiter=',')


for r in reader1:
    if r[1] in num:
        print(r[0], ',', r[1], ',', data.get(r[0]))
        writer.writerow([r[0], r[1], data.get(r[0])])
        writer2.writerow([r[0], r[1]])
    else:
        writer3.writerow([r[0], r[1]])