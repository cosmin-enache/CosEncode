import random

rand_list = []
original_str = "Hello" # type a string in here to encode, and see the results

class CosEncode:

  def __init__(self):
    pass

  def encode(self, s, max_no=15, times=0):

    max_no = abs(max_no)

    if times == 0:
      self.reset() # clears past encodings

    if times == max_no:
      self.encoded_string = s
      return

    self.rand_list.append(random.randint(0, len(s) - 1))
    times += 1

    r = list(s)
    random_char = chr(random.randint(97, 122)) # generates a random small cased char

    r.insert(self.rand_list[-1], random_char)

    return self.encode(str.join("", r), max_no, times)

  def decode(self, encoded_string, integer_keys):
    op_list = list(encoded_string)

    for i in reversed(integer_keys):
      op_list.pop(i)

    self.decoded_string = str.join("", op_list)

    return

  def display_meta(self):
    return f"Encoded String: {self.encoded_string}" \
    f"\nInteger Keys: {self.rand_list}" \
    f"\nDecoded String: {self.decoded_string}"

  def reset(self):
    self.rand_list = []
    self.encoded_string = None
    self.decoded_string = None
