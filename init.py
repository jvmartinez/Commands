#! /usr/bin/env python
import sys,os,commands
import config.optionCommand as oc
import config.control as control
command = oc.menuServer()
print "============================"
print oc.titleAction(command)
print "============================"
if command == 1:
    option = oc.menuOption()
    if option == 1:
        commands.getoutput(control.restartMySql())
    if option == 2:
        commands.getoutput(control.stopMySql())
    if option == 3:
        commands.getoutput(control.startMySql())
    print "Process executed...\n"
if command == 2:
    option = oc.menuOption()
    if option == 1:
        commands.getoutput(control.restartMySql())
    if option == 2:
        commands.getoutput(control.stopApache())
    if option == 3:
        commands.getoutput(control.startApache())
    print "Process executed...\n"
