print('STELLARIS QUIZ')
print('Stellaris is a big game with lots of possibilities. With kind of empire would you be in it?')
QUIZ_STATUS=0
materialist=0
religious=0
egalitarian=0
authoritharian=0
pacifist=0
militarist=0
xenophobe=0
xenophile=0
gestalt=0

while True:
    if QUIZ_STATUS==0:
        print('Q1. Your society unfortunatelly spawned in a world poor of resources. How will you deal with the few you have?')
        print('1. Racioanlly, maximizing happiness where is needed.')
        print('2. Following tradition, sharing accordingly to it. ')
        print('3. We shall share equaly, so all can use it.')
        print('4. Our leaders and specialists need more than others.')
        print('5. We shall share in order to avoid conflict.')
        print('6. Only those able to get it shall have it.')
        print('7. Outsiders shall not be allowed to have them.')
        print('8. Through quotas so there will be no discrimination')
        print('9. Not a problem, everyone does not consume a lot.')
        apc=input('With do you choose?: ')
        apc=int(apc)
        if apc==1:
            materialist+=1
        elif apc==2:
            religious+=1
        elif apc==3:
            egalitarian+=1
        elif apc==4:
            authoritharian+=1
        elif apc==5:
            pacifist+=1
        elif apc==6:
            militarist+=1
        elif apc==7:
            xenophobe+=1
        elif apc==8:
            xenophile+=1
        elif apc==9:
            gestalt+=1
        else:
            print('Invalid Option')

        print('Q2. With way will you share political powers?')
        print('1. We shall reach political equilibrium thorugh scientific models')
        print('2. We shall elect a overseeing body to keep moral standards')
        print('3. All shall have a saying in political process')
        print('4. Sharing?')
        print('5. By any means to maintain internal harmony')
        print('6. Only those who serve shall partake in it')
        print('7. Non-natives shall be banned from community decisions')
        print('8. Outside input may help us in doing such sharing')
        print('9. What is this ''politics'' you talk so much?')
        apc=input('With do you choose?: ')
        apc=int(apc)
        if apc==1:
            materialist+=1
        elif apc==2:
            religious+=1
        elif apc==3:
            egalitarian+=1
        elif apc==4:
            authoritharian+=1
        elif apc==5:
            pacifist+=1
        elif apc==6:
            militarist+=1
        elif apc==7:
            xenophobe+=1
        elif apc==8:
            xenophile+=1
        elif apc==9:
            gestalt+=1
        else:
            print('Invalid Option')

        print('Q3. ')

            

        #print(gestalt)
