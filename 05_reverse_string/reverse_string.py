def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    list_1 = list(phrase.strip(" "))
    list_1.reverse()
    return ''.join(list_1)


    #ezpz way:
    # return phrase[::-1]
    