# get a list of the next 20 birthdays from your contacts

import contacts
from datetime import datetime
import operator

days_list = []
people = contacts.get_all_people()
now = datetime.now()
for p in people:
	b = p.birthday
	if b:
		next_birthday = datetime(now.year, b.month, b.day)
		if next_birthday < now:
			next_birthday = datetime(now.year + 1, b.month, b.day)
		days = (next_birthday - now).days
		days_list.append({'name': p.full_name, 'days': days})

if not days_list:
	print('You don\'t have any birthdays in your address book.')
else:
	days_list.sort(key=operator.itemgetter('days'))
	print('Next Birthdays')
	print('=' * 20)
	for item in days_list:
		print('* %s in %i days' % (item['name'], item['days']))