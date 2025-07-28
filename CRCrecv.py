def xor_operation(dividend, divisor, length):
    result = []
    for i in range(length):
        result.append('0' if dividend[i] == divisor[i] else '1')
    return ''.join(result)

def check_crc(received, key):
    data_len = len(received)
    key_len = len(key)
    remainder = received[:key_len]

    for i in range(data_len - key_len):
        if remainder[0] == '1':
            remainder = xor_operation(remainder, key, key_len) + received[i + key_len]
        else:
            remainder = xor_operation(remainder, '0' * key_len, key_len) + received[i + key_len]
        remainder = remainder[1:]

    return '1' not in remainder

if __name__ == "__main__":
    received = input("Enter received data (binary): ")
    key = input("Enter key (generator polynomial): ")

    if check_crc(received, key):
        print("No error detected in received data.")
    else:
        print("Error detected in received data.")
