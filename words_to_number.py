def words_to_number(text):
    ones = {
        "zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,
        "six":6,"seven":7,"eight":8,"nine":9,"ten":10,
        "eleven":11,"twelve":12,"thirteen":13,"fourteen":14,
        "fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19
    }
    tens = {
        "twenty":20,"thirty":30,"forty":40,"fifty":50,
        "sixty":60,"seventy":70,"eighty":80,"ninety":90
    }
    multipliers = {
        "hundred":100,"thousand":1000,"million":1_000_000,"billion":1_000_000_000
    }

    words = text.lower().split()
    total = 0
    current = 0

    for word in words:
        if word in ones:
            current += ones[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= 100
        elif word in ("thousand", "million", "billion"):
            current *= multipliers[word]
            total += current
            current = 0

    number = total + current
    return f"{number:,}"  # <-- this adds commas to the output


# Test it
print(words_to_number("three"))                          # 3
print(words_to_number("fifty thousand"))                 # 50,000
print(words_to_number("two hundred forty six"))          # 246
print(words_to_number("one million five hundred thousand"))  # 1,500,000
print(words_to_number("one thousand four hundred fifty three"))  #1453
