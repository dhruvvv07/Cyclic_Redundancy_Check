def xor_operation(dividend, divisor, length):
    result = []
    for i in range(length):
        result.append('0' if dividend[i] == divisor[i] else '1')
    return ''.join(result)

def crc_generate(data, key):
    data_len = len(data)
    key_len = len(key)
    temp = data + '0' * (key_len - 1)  # Append zeros

    remainder = temp[:key_len]

    for i in range(data_len-1):
        if remainder[0] == '1':
            remainder = xor_operation(remainder, key, key_len) + temp[i + key_len]
        else:
            remainder = xor_operation(remainder, '0' * key_len, key_len) + temp[i + key_len]
        remainder = remainder[1:]  # Shift left by 1 (drop first bit)

    # Drop leading bit to get CRC bits of length key_len - 1
    return remainder[1:]

if __name__ == "__main__":
    data = input("Enter data (binary): ")
    key = input("Enter key (generator polynomial): ")

    crc = crc_generate(data, key)
    print("CRC bits:", crc)
    print("Transmitted data:", data + crc)
