
def to_lower_case(text):

    text_in_lowercase = text.lower()

    return text_in_lowercase

def text_cleaner(lower_case_text):

    clean_text = lower_case_text.replace(',', '').replace('.','')

    separated_text = clean_text.split()

    return separated_text

def words_counter(separated_text):

    counted_words = {}
    for word in separated_text:
        if word not in counted_words.keys():
            counted_words[word]= separated_text.count(word)

    return counted_words




if __name__ == '__main__':
    text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar."

    text_in_lowercase = to_lower_case(text)
    separated_text = text_cleaner(text_in_lowercase)
    counted_words = words_counter(separated_text)

    print(counted_words)