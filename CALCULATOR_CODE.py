def q():
    qu = input('what do you want to do. Type space followed by facts, calculator or type')
    if qu == ' calculator':
        c()
    if qu == ' type':
        t()
    if qu == ' facts':
        f()
def f():
    print('the most venemous animal in the world is the geography cone snail.')
    print('if you are in space without a space suit you pass out after 30 seconds and die after 90 seconds.')
    print('150 apple seeds can kill you if they are crushed and of a certain apple type. However, in other types of apples, a few thousand may be needed to kill you.')
    print('pianos were originaly called "clavicembalo col piano e forte me" meaning a harpsicord that can play loud and soft notes.')
    print('roblox was coded using python')
    print('minecraft was coded using java')
    print('Elizibath 1st owned the first ever toilet')
    g = input('do you want to see more facts? type space followed by yes or no.').lower()
    if g == ' no':
        q()
    print('Bessie Smith was known as "the Empress of the blues.')
    print('the queen bee has an unlimited number of stings')
    print('Magnus Carlson was the chess world champion 2020.')
    Go_Home = input('No more facts. Type space followed by home to go home').lower
    if Go_Home == ' home':
        q()
def t():
    ty = input('type here:')
def c():
    what = input('what do you want to do? type space followed by x, /, + or -.')
    if what == ' x':
        x = int(input('please enter a number'))
        table = int(input('please enter a number'))
        print(x, 'x', table, '=', x*table)
        qwerty = input('type space followed by calculator, type, facts or home.').lower
        if qwerty ==  ' home':
            q()
        if qwerty == ' calculator':
            c()
        if qwerty == ' type':
            t()
        if qwerty == ' facts':
            f()
    if what == ' /':
        x = int(input('please enter a number'))
        divide = int(input('please enter a number'))
        print(x,'÷', divide, '=', x/divide)
        asd = input('type space followed by calculator, type, facts or home.').lower
        if asd ==  ' home':
            q()
        if asd == ' calculator':
            c()
        if asd == ' type':
            t()
        if asd == ' facts':
            f()
    if what == ' +':
        x = int(input('please enter a number'))
        addition = int(input('please enter a number'))
        print(x, '+', addition, '=', x + addition)
        zxc = input('type space followed by calculator, type, facts or home.').lower
        if zxc ==  ' home':
            q()
        if zxc == ' calculator':
            c()
        if zxc == ' type':
            t()
        if zxc == ' facts':
            f()
    if what == ' -':
        x = int(input('please type a number'))
        sub = int(input('please enter a number'))
        print(x, '-', sub, '=', x - sub)
        qwerty = input('type space followed by calculator, type, facts or home.').lower
        if jkl ==  ' home':
            q()
        if jkl == ' calclator':
            c()
        if jkl == ' type':
            t()
        if jkl == ' facts':
            f()


q()
