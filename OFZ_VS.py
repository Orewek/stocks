import pandas as pd
import matplotlib.pyplot as plt

# BLOCK OF INCOMING INFORMATION

first_day = '16.02.22'  # first day of ownership
last_day = '14.08.24'   # last day of ownership
pol_goda = ['1/2', '1', '3/2', '2', '5/2', '3']     # just for graphics
kyponi = [5, 6, 7, 8, 8.5, 8.87]     # Interest on which dividends will be accrued
csena_v_rubliah = 956   # price in rubles
csena_v_kopeikah = 48   # price in pennys (so its rubles + pennys / 100)
kol_vo_ofz = 109        # how many ofz u gonna buy

broker_commission = 0.003   # brokers commission that he takes if u sell/buy securities
personal_income_tax = 13    # tax that u pay if sell securities (to pay gotta earn smth)

debugging = 0
info_showing = '1111'   # DAYS MONEY TAXES PROCENT

# BLOCK OF INCOMING INFORMATION


def info():
    # DAYS-INFO BLOCK

    day_of_placement = first_day
    date_of_maturity = last_day

    years = int(date_of_maturity[6:]) - int(day_of_placement[6:])
    months = int(date_of_maturity[3:5]) - int(day_of_placement[3:5])
    days = int(date_of_maturity[:2]) - int(day_of_placement[:2])

    total_days = years * 365 + months * 30 + days
    total_years = days / 365 + months / 12 + years

    if(days < 0):
        months -= 1
        days += 30
    if(months < 0):
        years -= 1
        months += 12

    string_years = "year"
    string_months = "month"
    string_days = "day"
    if(years != 1):
        string_years += "s"
    if(months != 1):
        string_months += "s"
    if(days != 1):
        string_days += "s"

    if(info_showing[:1] == '1'):
        print("---DAYS_INFO---")

        print(f'day of placement - {day_of_placement} \n'
              f'date of maturity - {date_of_maturity} \n'
              f'whole period - {years} {string_years}, {months} {string_months}, {days} {string_days} \n'
              f'total amount of days - {total_days} or years - {round(total_years, 2)} \n ')

    # MONEY-INFO BLOCK

    rubles_price = csena_v_rubliah
    pennys_price = csena_v_kopeikah

    price_of_bond = rubles_price + pennys_price / 100
    amount_of_bonds = kol_vo_ofz
    total_cost = round(price_of_bond * amount_of_bonds)

    broker_earnings = total_cost / 100 * broker_commission

    earning_per_half_year = []

    total_earnings = 0
    coupons = kyponi

    for coupon in coupons:
        earnings = total_cost / 100 * coupon / 2
        total_earnings += earnings
        earning_per_half_year.append(round(earnings - (earnings / 100 * 13)))

    goverment_earnings = total_earnings / 100 * 13
    total_earnings -= (broker_earnings + goverment_earnings)

    if(info_showing[1:2] == '1'):
        print("---MONEY_INFO---")

        print(f'cost of one bond - {price_of_bond} rubles \n'
              f'amount of bonds - {amount_of_bonds} \n'
              f'total cost - {total_cost} rubles \n'
              f'total earnings - {round(total_earnings)} rubles \n'
              f'earning in half-years - {earning_per_half_year} \n')

    # TAXES-INFO BLOCK

    if(info_showing[2:3] == '1'):
        print("---TAXES_INFO---")

        print(f'brokers earning - {round(broker_earnings, 2)} \n'
              f'goverment earning - {round(goverment_earnings)} \n')

    # PROCENT-INFO BLOCK

    average_annual_profitability = total_earnings / total_cost * 100 / ((len(pol_goda) / 2))
    procent_for_first_year = (earning_per_half_year[0] + earning_per_half_year[1]) / total_cost * 100

    if(info_showing[3:4] == '1'):
        print("---PROCENT_INFO---")

        print(f'average annual profitability - {round(average_annual_profitability, 3)} % \n'
              f'coupons - {coupons} \n'
              f'procent for first year - {round(procent_for_first_year, 3)} % \n')
        if (total_years < 1):
            print(f'THE REAL PROCENT - {round(procent_for_first_year / total_years, 3)} % \n')

    # U CAN TYPE AND CHECK SMTH HERE
    if (debugging == 1):
        print(f'{goverment_earnings} \n'
              f'{total_earnings} \n'
              f'{total_earnings / 100 * 13}')
        goverment_earnings = total_earnings - (total_earnings / 100 * 13)

    # GRAPHICS
    # tables(earning_per_half_year)


def table1(earning_per_half_year):
    ears_elapsed = pol_goda
    x = ears_elapsed
    y = earning_per_half_year
    plt.figure(figsize=(20, 20))
    plt.plot(x, y)

    plt.xlabel('time elapsed (years)', fontsize=30)
    plt.ylabel('earning (rubles)', fontsize=30)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.title('Earning per half-year', fontsize=30)

    plt.show()


def table2(earning_per_half_year):
    ears_elapsed = pol_goda
    x = ears_elapsed
    y = earning_per_half_year

    plt.figure(figsize=(20, 20))
    plt.bar(x, y, color='green')

    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.xlabel('time elapsed (years)', fontsize=30)
    plt.ylabel('earning (rubles)', fontsize=30)

    plt.show()


def table3(earning_per_half_year):
    x = earning_per_half_year
    df = pd.DataFrame(x, columns=['ears_elapsed'])

    df.plot.pie(y='ears_elapsed', figsize=(20, 20))
    plt.show()


def tables(earning_per_half_year):
    table1(earning_per_half_year)
    table2(earning_per_half_year)
    table3(earning_per_half_year)


info()
