int_value = 15
float_value = 4.1
text_value = "33"

type_of_float_value = type(float_value)

text_value_as_int = int(text_value)

int_value_as_text = str(int_value)

print("Float value type:", type_of_float_value)

print("Integer addition adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)

print("Text addition adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)