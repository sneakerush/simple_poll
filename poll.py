# long-ish poll using while loops, if statement, and for loop

responses = {}
polling = True

while polling:
    # ask polling questions
    name = input('What is your name? ')
    response_1 = input('If you could live anywhere in the United States, where would that be? ')
    # store responses in the dictionary 'responses'
    responses[name] = response_1
    # ask if the person would like someone else to take the poll
    continue_poll = input('Would you like someone else to do this poll? (yes/no) ')
    # create if statement for 'no' response to stop the while loop
    if continue_poll == 'no':
        polling = False

# print a results title
print('----The Polling Results----')
# for statement to print the results
for name, response_1 in responses.items():
# print the responses with corresponding name
    print(f"{name.title()} would live in {response_1.title()} if he had the choice!")