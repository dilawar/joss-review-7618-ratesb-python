from ratesb_python import check_model

result = check_model("S->P;k1*S")
print(type(result), result)
print(result.get_errors())
print(result.get_warnings())
