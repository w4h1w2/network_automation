#!/usr/bin/env python3

from pprint import pprint 

'''
check interface status of switch 
show int status

#kq.txt
Switch#sh int status
                                             Flow Link          Back   Mdix
Port     Type         Duplex  Speed Neg      ctrl State       Pressure Mode
-------- ------------ ------  ----- -------- ---- ----------- -------- -------
gi1      1G-Copper    Full    100   Enabled  Off  Up          Disabled Off
gi2      1G-Copper    Full    100   Enabled  Off  Up          Disabled On
gi3      1G-Copper      --      --     --     --  Down           --     --
gi4      1G-Copper      --      --     --     --  Down           --     --
gi5      1G-Copper      --      --     --     --  Down           --     --
gi6      1G-Copper      --      --     --     --  Down           --     --
gi7      1G-Copper      --      --     --     --  Down           --     --
gi8      1G-Copper    Full    100   Enabled  Off  Up          Disabled Off
gi9      1G-Combo-C     --      --     --     --  Down           --     --
gi10     1G-Combo-C     --      --     --     --  Down           --     --

                                          Flow    Link
Ch       Type    Duplex  Speed  Neg      control  State
-------- ------- ------  -----  -------- -------  -----------
Po1         --     --      --      --       --    Not Present
Po2         --     --      --      --       --    Not Present
Po3         --     --      --      --       --    Not Present
Po4         --     --      --      --       --    Not Present
Po5         --     --      --      --       --    Not Present
Po6         --     --      --      --       --    Not Present
Po7         --     --      --      --       --    Not Present
Po8         --     --      --      --       --    Not Present

'''

def show_port_down():

    f = open("credentials.yml")
    contents = f.read()
    lines = contents.splitlines()
    f.close()

    firstline = lines[0]
    hostname = firstline.split("#")[0]

    list1 = []
    for line in lines:
        if line.startswith("gi"):
            name = line.split()[0]
            state = line.split()[6]
            if state == "Down":
                temp = []
                temp.append(name)
                temp.append(state)
                list1.append(temp)

    print("How many ports are there on {}? Answer: {} ports".format(hostname, len(list1)))
    print()
    print("List of ports in more detail: ")
    pprint(list1)

    return None

def main():
    show_port_down()

    return None

if __name__ == "__main__":
    main()



