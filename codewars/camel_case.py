def to_camel_case(text: str) -> str:

    arr_text = text.split("_")
    out_str = ""

    for word in arr_text:
        first_char = word[0].capitalize()
        word = first_char + word[1: len(word)]
        out_str += word
    
    return out_str

print(to_camel_case("hello_shangwa"))