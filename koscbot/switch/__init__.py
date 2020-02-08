from .bidirdict import BiDirDict

default_ru_lowercase = "йцукенгшщзхъфывапролджэячсмитьбю."
default_en_lowercase = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
default_ru_uppercase = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"
default_en_uppercase = "QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?"
default_ru_signs = "!\"№;%:?*"
default_en_signs = "!@#$%^&*"

default_en_to_ru_mapping = BiDirDict(
    zip(default_ru_lowercase + default_ru_uppercase + default_ru_signs,
        default_en_lowercase + default_en_uppercase + default_en_signs)
)


def switch(message, mapping=default_en_to_ru_mapping):
    return ''.join([mapping[i] if i in mapping else i for i in message])
