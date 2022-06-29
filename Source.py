#BAI1
# Monoalphabetic substitution cipher
from collections import Counter
import string
import random
alpha = "abcdefghijklmnopqrstuvwxyz"
text = input("- Plaintext: ").lower()


def encrypt(text, key=None):
  p = ""
  if key is None:
    l = list(alpha)
    random.shuffle(l)
    p = "".join(l)
  else:
    temp = key + alpha
    for char in temp:
      if char not in p:
        p = p + char
  newtext = []
  for letter in text:
    if letter.isalpha():
      newtext.append(p[alpha.index(letter)])
    else:
      newtext.append(letter)
  return ["".join(newtext), p]


result = encrypt(text, "zebraistpdcfghjklmnoquvwxy")
print('- Alphabet: \t', alpha)
print('- Key: \t\t', result[1])
print('- Ciphertext: \t', result[0])
#BAI2
# Giải mã mật mã Caesar
text_1 = input("- Ciphertext: ").lower()


def decryption(text):
  temp = text
# Xóa các ký tự không phải chữ cái khỏi văn bản đầu vào
  for letter in temp:
    if not(letter.isalpha()):
      temp = temp.replace(letter, '')
  # Tìm chữ cái phổ biến nhất và tính toán độ chênh lệch giữa chữ cái đó và 'e'
  # e là nhiều nhất
  jump = ord(Counter(temp).most_common()[0][0]) - ord('e')
  # Decrypting
  alpha = "abcdefghijklmnopqrstuvwxyz"
  decrypt = ''
  for letter in text:
    if letter.isalpha():
      index = alpha.find(letter)  # the index of the letter in Alphabet
      decrypt += alpha[index - jump]
    else:
      decrypt += letter
  return (decrypt, (Counter(temp).most_common()[0][0]), jump)


result_1 = decryption(text_1)
print("- The most common char: ", result_1[1])
print("- Shift by: ", result_1[2])
print("- Decrypted text: ", result_1[0])
