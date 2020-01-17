# Description: This example connects to a previous set-up XRVR router,
#              executes some show commands and parses via cAAs/TCL and
#              parsergen/Python, with differences in the parse results
#              shown.  

import os
from pyats.easypy import run

def main():
    # Find the examples/tests directory where the test script exists
    test_path = (os.path.dirname(os.path.abspath(__file__)))
    # Do some logic here to determine which devices to use
    # and pass these device names as script arguments
    # ...
    chosen_uut_device = 'VM-1'
    stdby_device = 'notreallyadevice'
    if_name = 'GigabitEthernet0/0'
    mtu = 1500

    #
    # NOTE: The tabular parse will fail on vIOS platform, because
    #       one of the colums is right-justified while the rest are
    #       left-justified.  The tabular parser only supports a 
    #       consistent justification setting for all columns in the table.
    #
    show_arp_header_fields= [ "Protocol",
                              "Address",
                              "Age \(min\)",
                              "Hardware Addr",
                              "Type",
                              "Interface" ]
    show_arp_table_parse_index = [1, 5]
    show_arp_table_title_pattern = None


    run(testscript=test_path + '/parsergen_demo.py',
        uut_name=chosen_uut_device,
        stdby_name=stdby_device, if_name=if_name, mtu=mtu, 
        show_arp_header_fields=show_arp_header_fields, 
        show_arp_table_parse_index=show_arp_table_parse_index,
        show_arp_table_title_pattern=show_arp_table_title_pattern)
