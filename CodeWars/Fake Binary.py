# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
#
# Note: input will never be an empty string

def fake_bin(x):
    result = ""
    stringnum = x
    for digit in stringnum:
        if int(digit) >= 5:
            result += "1"
        if int(digit) < 5:
            result += "0"
    return result
