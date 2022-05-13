from transformers import T5Tokenizer, T5ForConditionalGeneration


tokenizer = T5Tokenizer.from_pretrained("/pebble_tmp/models/t5-small")
model = T5ForConditionalGeneration.from_pretrained("/pebble_tmp/models/t5-small")
# tokenizer = T5Tokenizer.from_pretrained("t5-small")
# model = T5ForConditionalGeneration.from_pretrained("t5-small")


def translate(text: str, source: str="English", dest: str="French", max_length=100) -> str:
    """
    Translate text from source to dest
    
    :param text: input text
    :param source: source language
    :param dest: translated language
    """
    input_ids = tokenizer(f"translate {source} to {dest}: {text}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=int(max_length))
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return result 


if __name__ == "__main__":
    text = 'The house is wonderful.'
    print(translate(text))