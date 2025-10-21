def get_hidden_card(cc_number, length=4):
    censored = ("*" * length) + str(cc_number[-4:])
    print(censored)
    return

get_hidden_card('1234567812345678', 2)
get_hidden_card('1234567812345678', 3)