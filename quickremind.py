# a simple script if you often create the same reminder
# add it to pythonistas today widget for one tap creation

import reminders
r = reminders.Reminder()
r.title = 'Buy coffee' # fill the text to the left with what you want the reminder to say
r.save()
print('Reminder added')