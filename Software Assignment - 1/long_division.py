#helper functions

#converts the input strings to an array
def string_to_list(num):
    num_list = []
    for i in num:
        if i == 'a':
            num_list.append(10)
        elif i == 'b':
            num_list.append(11)
        elif i == 'c':
            num_list.append(12)
        elif i == 'd':
            num_list.append(13)
        elif i == 'e':
            num_list.append(14)
        elif i == 'f':
            num_list.append(15)
        elif int(i) < 10:
            num_list.append(int(i))
    return num_list

#converts arrays back to strings for output
def list_to_string(num_list):
    string = ''
    for i in num_list:
        if i < 10:
            string += str(i)
        elif i == 10:
            string += 'a'
        elif i == 11:
            string += 'b'
        elif i == 12:
            string += 'c'
        elif i == 13:
            string += 'd'
        elif i == 14:
            string += 'e'
        elif i == 15:
            string += 'f'
    return string


#Long Division function (Algorithm 1.5)
#
def long_division(x, y, radix):

    #check the sign of the numbers
    sign_x = '+'
    if x[0] == '-':
        x = x[1:]
        sign_x = '-'

    sign_y = '+'
    if y[0] == '-':
        y = y[1:]
        sign_y = '-'

    x = string_to_list(x)
    y = string_to_list(y)

    k = len(x)
    l = len(y)

    #if y>x then output 0 as quotient and x as the remainder
    if k < l:
        return [0, x]

    #quotient and remainder
    q = [] 
    r = [0] + x

    #to avoid division by zero
    if y[0] == 0:
        y_start = 1
    else:
        y_start = y[0] 

    for i in range(0, k-l + 1):
        
        q.append((r[i] * radix + r[i + 1]) // y_start)

        if (q[i] >= radix):
            q[i] = radix - 1

        carry = 0

        for j in range(l - 1, -1, -1):
            temp = r[i+j + 1] - q[i] * y[j] + carry
            carry, r[i+j + 1] = temp // radix, temp % radix

        r[i] = r[i] + carry

        while r[i] < 0:
            carry = 0

            for j in range(l - 1, -1, -1):
                temp = r[i+j + 1] + y[j] + carry
                carry, r[i + j + 1] = temp // radix, temp % radix

            r[i] = r[i] + carry
            q[i] = q[i] - 1
    
    #making the quotient negative if the signs are different
    if sign_x != sign_y:
        q = [-1] + q

    q = list_to_string(q)
    r = list_to_string(r)

    #remove zeroes at the beginning of the numbers
    q = q.lstrip("0")
    r = r.lstrip("0")

    return [q,r]

a = 'd26936c465648ef03a1ade904737b30428155781'
b = '157f77a46f4c796bb774'
print(long_division(a,b,16))