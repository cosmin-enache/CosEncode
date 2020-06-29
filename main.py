from encoder import CosEncode

encoder = CosEncode()

original_str = input("Input string to encode: ")

print()

encoder.encode(original_str, max_no=15) # max_no => number of random chars to add

# LINE BELOW DECODES THE ENCODED STRING IF PRESENT
encoder.decode(encoder.encoded_string, encoder.rand_list)

print(encoder.display_meta())
