from optparse import OptionParser
parser = OptionParser()
parser.add_option('-d', '--device', dest='Device', help='Device Type')
parser.add_option('-c', '--command', dest='Command', help='Command')
options, arguments = parser.parse_args()

if options.Device == '0': #Electrical Outlet
    if options.Command == 'input.on':print('ON')
    elif options.Command == 'input.off':print('OFF')
