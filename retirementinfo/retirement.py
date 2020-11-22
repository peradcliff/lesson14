"""
Date: 08/20/20
Purpose: To calculate when is the age of retirement and when will that be.
"""

import datetime

print("Social Security Full Retirement Age Calculator")

x = datetime.datetime.now()

while True:
    year_data = input("Enter the year of birth or enter to exit: ")
    if year_data == "":
        break
    else:
        year = int(year_data)

        if 1900 <= year <= x.year:
            month_int = int(input("Enter the month of birth: "))
            # calculate year and months in total months needed for further calculations
            fra = 0
            if year <= 1937:
                fra = 780   # 65 in months
            elif year == 1938:
                fra = 782   # 65 years and 2 months in months
            elif year == 1939:
                fra = 784   # 65 years and 4 months in months
            elif year == 1940:
                fra = 786   # 65 years and 6 months in months
            elif year == 1941:
                fra = 788   # 65 years and 8 months in months
            elif year == 1942:
                fra = 790   # 65 years and 10 months in months
            elif 1943 <= year <= 1954:
                fra = 792   # 66 years in months
            elif year == 1955:
                fra = 794   # 66 years 2 months in months
            elif year == 1956:
                fra = 796   # 66 years and 4 months in months
            elif year == 1957:
                fra = 798    # 66 years and 6 months in months
            elif year == 1958:
                fra = 800   # 66 years and 8 months in months
            elif year == 1959:
                fra = 802   # 66 years and 10 months in months
            else:
                if year >= 1960:
                    fra = 804   # 67 years in months

            # calculate the year to start retirement
            date = (((year * 12) + fra) / 12)
            # calculate month name to start retirement
            month_int = month_int + (fra % 12)
            if month_int > 12:
                date = date + 1
                month_int = month_int % 12
            month = datetime.date(int(date), month_int, 1).strftime('%B')

            print("Your full retirement age is ", int(fra/12), "years and ", fra % 12, "months")
            print("This will be in ", month, "of", int(date))

        else:
            print("Unable to calculate")
