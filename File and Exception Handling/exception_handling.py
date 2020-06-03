print('Enter numerator and denominator to perform division operation: ')
fail = 1
attempts_no = 0

while ((attempts_no < 5 and fail == 1)):
    attempts_no+=1
    try:
        a = int(input('Numerator : '))
        b = int(input('Denominator : '))
        print ('Quotient : ',(a/b))
        fail = 0
        ## always open resource(db connection, opening file) here
    except ZeroDivisionError as e:
        print('Hi, a denominator can not be 0. Please re-execute the program:::: ')
        fail = 1

    except ValueError:
        print('Hi, Numerators or denominators can be only numbers:::: ')
        fail = 1

    except Exception as e:
        print('Hi, Something went wrong:::: ')
        fail = 1

    else:
        print('Summation of numerator and denominator : ',a+b)

    finally:
        if(fail == 0):
            print('bye')
        ## always close resource(db connection, opening file) here