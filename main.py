try:
    from calendar import prcal
except:
    print 'Let\'s start out with a select message for those on a incompatible platform getting integer overflows.'

def main(years):
    try:
        print 'Woohoo %s years of Python' % years
    except:
        print '...and how about formatted strings in Python (and type exception!)...'
    try:
        prcal(1991)
    except:
        print '...and we all enjoy having datetime, even with its flaws (and runtime exception)...'
    print '...having some whitespace just for flavor will not break PEP8!'
    for year in range(years):
        print(year)
    print 'Woohoo', years, 'years of Python,'
    try:
        if not all(years):
            print 'is all I wanted to say.'
    except:
        print 'here\'s to', years, 'more!'

try:
    main(years=30)
except:
    print 'Sure is nice being able to set named arguments...'
finally:
    main(30)
