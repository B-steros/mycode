import pandas as pd

def main():

    print(pd.to_datetime('2018-01-15 3:45pm'))

    print(pd.to_datetime('1952/07/08'))

    print(pd.to_datetime('7/8/1952', dayfirst=True))


    print(pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995'], format='mixed'))


    print(pd.to_datetime(['2/25/10', '8/6/17', '12/15/12'], format='%m/%d/%y'))

if __name__ == "__main__":
    main()
