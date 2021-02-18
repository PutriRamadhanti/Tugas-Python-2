#dengan dictionary
vowels = 'aiueo'

ip_str = 'Halo nama saya putri ramadhanti, saya sedang belajar python'

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
    if char in count:
        count[char] += 1

print(count)

#Putri Ramadhanti/29/XI-5
