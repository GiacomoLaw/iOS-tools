# a simple script if you often create the same reminder

import reminders
r = reminders.Reminder()
r.title = 'Buy coffee' # fill the text to the left with what you want the reminder to say
r.save()
print('Reminder added')