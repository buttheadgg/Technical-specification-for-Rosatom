
def compare_versions(version_1: str, version_2: str):
    [a_major, a_minor] = version_1.split('.')
    [b_major, b_minor] = version_2.split('.')
    if a_major == b_major and a_minor == b_minor:
        return 0
    if a_major != b_major:
        if a_major > b_major:
            return 1
        return -1
    if a_minor > b_minor:
        return 1
    return -1



if __name__ == '__main__':
    first = input('Enter first version:')
    second = input('Enter second version:')
    result = compare_versions(first, second)
    print(result)

