def autocomplete(input_, dictionary):
    input_ = ''.join( [ c for c in list(input_) if c.isalpha() ])
    return [ x for x in dictionary if x.lower().startswith(input_.lower()) ][:5]