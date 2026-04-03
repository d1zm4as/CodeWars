def next_version(version):
    if version == "9.9":
        return "10.0"
    if version == "9":
        return "10"
    version = version.split('.') 
    for i in range(len(version)-1, -1, -1): #
        if version[i] == '9':
            version[i] = '0'
        else:
            version[i] = str(int(version[i]) + 1)
            break
    else:
        version.insert(0, '1')
    return '.'.join(version)