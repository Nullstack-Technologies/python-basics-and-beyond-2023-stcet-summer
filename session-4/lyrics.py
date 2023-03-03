lyrics = """Chandni raat mein Gori ke saath mein Aasmaan mein Dekhunga nageene  Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Set mera scene hai Scene hai scene hai scene hai Scene hai scene hai scene hai  Gori tu bada sharmati hai Tujhko sharam kyun aati hai Kaatil teri nigaahein hain Tu kaat kaleja le jaati hai Tujh mein nasha hai Tu bilkul afeem hai  Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Set mera scene hai Scene hai scene hai scene hai Scene hai scene hai scene hai  Thought mera chhu ke nikla Badan pe tere phisla Lafz mere honth se chhoo le Main toh tujhe dekh ke pighla Agan mein jali hai jali hai jali Kamsin kali hai kali hai kali Tujhe bas choona hai choona hai choo Misri ki dali hai dali hai dali Tera husn to sabse aala hai Mujhe pagal karne wala hai Aaj nasha tera karke Tera aashiq marne wala hai Sach sach bol haqueeqat Ya ye dream hain  Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Set mera scene hai Scene hai scene hai scene hai Scene hai scene hai scene hai  Gori tu bada sharmati hai Tujhko sharam kyun aati hai Kaatil teri nigaahein hain Tu kaat kaleja le jaati hai Are Tujh mein nasha hai Tu bilkul afeem hai  Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Dheeme dheeme dheeme dheeme Set mera scene hai Scene hai scene hai scene hai Scene hai scene hai scene hai"""
# Lower case everything
lyrics.replace("\n", "")
lyrics = lyrics.lower()
lyrics_dict = {}

print(f"Total Words: {len(lyrics.split())}")
print(f"Total Unique Words: {len(set(lyrics.split()))}")

for word in lyrics.split():
    #word exists ?
    if word in lyrics_dict.keys():
        lyrics_dict[word] += 1
    else:
        lyrics_dict[word] = 1

print(lyrics_dict)
a = []
a = lyrics_dict.values()
a = list(a)
a.sort(reverse=True)
print(f"Lyrics dictionary values in descending order: \n {a}")
b = []
for i in range(20):
    b.append(a[i])
print(f"Lyrics dictionary first 20 values: \n {b}")
c = []
for x in b:
    for y in lyrics_dict.keys():
        if lyrics_dict[y] == x:
            if [y, x] not in c:
                c.append([y, x])
print(f"Lyrics dictionary keys and values in sorted order: \n {c}")

