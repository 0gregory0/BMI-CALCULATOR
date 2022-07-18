def bmi_calculator():

    while True:
        print('''
        DISCLAIMER !!!
        Information obtained from here is
        NOT medical advice or a diagnosis!
        Only use if you are an adult.
        Results may be inaccurate if you
        are a body builder or expectant
        ''')

        weight = float(input('Enter your weight (kg) here: '))
        height = float(input('Enter your height (cm) here: '))

        height_in_m = height/100
        height_squared = height_in_m ** 2

        bmi = weight/height_squared

        if bmi <= 18.5:
            print(
                f'your bmi is {bmi}kg/m2. A bmi less than 18.5 is underweight. Normal bmi ranges between 18.5 to 24.9.')

        elif bmi <= 24.9:
            print(
                f'your bmi is {bmi}kg/m2. This is considered healthy as it lies within the normal range of 18.5 to 24.9.')

        elif bmi <= 29.9:
            print(
                f'your bmi is {bmi}kg/m2. A bmi between 25 and 29.9 is overweight. Normal bmi ranges between 18.5 to 24.9.')

        elif bmi <= 39.9:
            print(
                f'your bmi is {bmi}kg/m2. A bmi between 30 and 39.9 is obese. Normal bmi ranges between 18.5 to 24.9.')

        elif bmi >= 40:
            print(
                f'your bmi is {bmi}kg/m2. A bmi of 40 or greater is extreme obesity. Normal bmi ranges between 18.5 to 24.9.')

        prompt_again = input('Try again? Y/N ')

        if (prompt_again == 'Y') or (prompt_again == 'y'):
            pass

        elif (prompt_again == 'N') or (prompt_again == 'n'):
            break


bmi_calculator()
