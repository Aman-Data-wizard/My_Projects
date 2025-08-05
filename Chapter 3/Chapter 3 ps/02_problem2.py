letter = '''Dear <|Name|>, 
you are selected 
<|Date|>'''

print(letter.replace("|Name|>", "Aman").replace("<|Date|", "24 December 2025"))