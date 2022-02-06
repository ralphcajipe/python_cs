def zodiac_sign(month, day):
    """Check month and date within valid range of astrological chart."""

    if month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'

    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'

    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'aries'

    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'taurus'

    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'gemini'

    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'cancer'

    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'leo'

    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'virgo'

    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'libra'

    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'scorpio'

    elif month == 11:
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'

    elif month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'

    print(f"You are a {astro_sign.title()}")


user_month = int(input("Please enter your month of birth as a number:"))
user_day = int(input("Please enter your day of birth as a number:"))

zodiac_sign(user_month, user_day)
