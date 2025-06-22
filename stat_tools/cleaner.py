import re

def clean_source(source_item):
    replace_prime = re.sub("′", "&prime;", source_item)
    replace_section = re.sub("§ ", "&sect;&nbsp;", replace_prime)
    replace_dollar = re.sub("\$", "&dollar;", replace_section)
    replace_lb = re.sub("LB ", "LB&nbsp;", replace_dollar)
    cleaned_source = re.sub("\n", " ", replace_lb)
    return cleaned_source
    