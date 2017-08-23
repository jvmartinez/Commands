def menuServer():
    print "1) Server of mysql-sql"
    print "2) Server of apache"
    print "Action to select:"
    action = input()
    return action

def menuOption():
    print "1) Restart \n"
    print "2) Stop \n"
    print "3) Start \n"
    print "Action to select:"
    action = input()
    return action

def titleAction(option):
    if option == 1:
        return "Server of mysql-sql"
    if option == 2:
        return "Server of apache"