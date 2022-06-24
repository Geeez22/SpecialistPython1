# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = 'fdf....,,,2321'
text_len = len(text)
points = text.count('.')
comma = text.count(',')
if points == comma:
    print('same')
