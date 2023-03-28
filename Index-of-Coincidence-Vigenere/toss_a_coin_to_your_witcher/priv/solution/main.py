alph = "abcdefghijklmnopqrstuvwxyz"
import matplotlib.pyplot as plt

def isLetter(char):
    return (char in alph)


def countLetters(text):
    count = 0
    for i in text:
        if (isLetter(i)):
            count += 1
    return count


def getIOC(text):
    letterCounts = []

    # Loop through each letter in the alphabet - count number of times it appears
    for i in range(len(alph)):
        count = 0
        for j in text:
            if j == alph[i]:
                count += 1
        letterCounts.append(count)

    # Loop through all letter counts, applying the calculation (the sigma part)
    total = 0
    for i in range(len(letterCounts)):
        ni = letterCounts[i]
        total += ni * (ni - 1)

    N = countLetters(text)
    c = 26.0  # Number of letters in the alphabet
    total = float(total) / ((N * (N - 1)))
    return total

cipher = "LSWFWGXYPAELNTWNVPCFJRXMAYMBNPKMFWLYEPRVQLYELSXFVGHERQNICRAHGXRCVAUZCIZDMGEALSMIBRJNOZWZXEJFWUMXNGVKGSGEPGEIAEZDTSWNWQNDUNKITMOUEPMNJCHPTCUFRKLQYRHUCUMFKYCANTRGEVNLDXJXCDNHQEMEHJJOGNTTBKYYTAPYETBMEVTTUMZZCEETMFGHLDLOCGWUCPSEJSEGADSFIAZVIPCIQOHJTJKHXRPEWVRPRXFEWLDLDHEHEWPOWOHFLZZDFEMSCLONYGEIJPCNLIOKEPJJGZFREVMKFWUSHNBLAKMLLSFRVKWSPHICKMFSESGSTIBOLIGFDIUGNXRMEZRGYLDWODLBYOTGTBXVOAYYMIAVLQXJEPFJVKZVNHAIKMPDTOZTYJIAJTXDDYLKPQIOVPKYKUDAIHJIAYWDYFIKVKSDYICUKQWPWTPQKAAZIKPPISUKVENSIUPKUDXRBRBVOCNAXGRGAZTTTTVAVOPMMTWLKAMAMRDLAGNLMBFVWHNTEWOCVFKCEEZDIRLZPSVOJIAGSDPXFEJNNLFKITELNILTYBVIBWNEULTJAKXRODJRTKAHSBNVZURBPSEJSEBJAEKEHKMFOIPDFWJBKUHXMNRBTODPQDXZGRPTXDGVYWODTOIEIFAKMXWPIZCXETAFBGXYANHPGVBVILSPPXYHQNHLOVVVKEDARSEZWYVULICXQTVHHQOSWRAZNNGEFWTNCAINMJMWREMOIRTNIZFUOGYBAMLRJJJBKMPVUTMKHNOIFECKMTOOFASGFGPPNNESVTKMLTQBWLGHVCDESVVVSCEXZQIKASAMIDELKFPRFFHZGGUOPNCFBGXOFGMPPUAPNZSIPTGRZUEFEEPDVMWOLESGZELMJRETILSHAIVIUIMETJRULKVNXRSZVKXRSAXMEWKDEQCJJMJODUYNIIUNLADFPJBOOECQSXRBJAYTNSWCNPTLXFHGKKWRBEIPTGNHAUUIUZAAEBTWVZCBPWAPHVWHPTMLTYMTMZNFSEJMAKUGRTJMTFPDMTQIIWYTBCJCITMZLXFGKBJNIMEKVZADSIZHEJBJKUEGTEKGCPEYTEJDILAGTBVZTINOGMHGNPHGXOAUJGQTNTBHSHUUOBSNKIDVPFDPRKPDVLXGXMMPLCIZHMEZOVSHCXRJNOQEXJGZMUZUIPAZMFWCSQQXVFXLRLUHGQESZNRBVYBIAWHARLBGXPSEQIIYAJTEYRFDGBPDMTEEXTHMBNTJWTORUXBVFYULALTDEQURPDRSMVGZZHBPGVUCBVANMCEHSPNWOLRLOSCEYBXKXNWRTIHVGQEMEPXLVGYLDXLXMMTOOYQTTFKPZMXNOVINYFSXZEIKWUGBNVWZCXVNQTWVLPPMTBAVIUXLYMOCRKPPCEETEIDVPDYVWZVWSSAYCVAUIPTEJBKXAUYXTQCCURPSQOXZKAPTLTWVLKNQISVVVPKUDXRDWN"

key_length = 2
max_key_length = 25

key_length_record = []
key_length_ioc = []


print(len("Lambertwhataprick"))
for l in range(key_length,max_key_length):
    average = []
    for i in range(0,l):
        txt = cipher[i::l]
        total = getIOC(txt.lower())
        average.append(total)

    sum_total = 0
    for i in range(len(average)):
        sum_total+=average[i]
    sum_total = sum_total/len(average)

    print("IOC: " + str(sum_total) ,l)

correct_key_length = 17



alph = "abcdefghijklmnopqrstuvwxyz"
figure, axis = plt.subplots(3,6)

i1 = 0
j1 = 0
for k in range(0,18):
    txt = cipher[k::17]
    print(txt)
    prob = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for letter in txt:
        value = int(ord(letter)-65)
        prob[value]+=1

    for i in range(len(prob)):
        prob[i] = prob[i]/(len(txt))
    print(prob)
    alphBIG = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    axis[i1, j1].bar(alphBIG, prob)
    axis[i1, j1].set_title(f"key letter nr:{k+1}")

    if j1==5:
        j1=0
        i1+=1
    else:
        j1+=1

plt.show()