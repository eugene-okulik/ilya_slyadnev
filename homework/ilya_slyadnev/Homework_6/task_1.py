txt = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
       'dignissim vitae libero')

words = txt.split()
update_words = []

for word in words:
    word_without_punctuation = word.rstrip('.,')
    add_ing = word_without_punctuation + 'ing' + (word[-1] if word[-1] in '.,' else '')
    update_words.append(add_ing)

modified_text = ' '.join(update_words)
print(modified_text)
