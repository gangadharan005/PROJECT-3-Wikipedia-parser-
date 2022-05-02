from bs4 import BeautifulSoup
import requests


print("The Best FIFA Men's Player details:")

while True:
    try:
        user = int(input(
            "\n1.Cristiano Ronaldo\n2.Lionel Messi\n3.Neymar\n4.Virgil van Dijk\n5.N'Golo Kantée\n6.Paul Pogba\n7.Thomas Müller\nEnter the number then view the players information: "))
    except ValueError:
        print("I don't understand")
        continue

    if user != '1' and user != '2' and user != '3' and user != '4' and user != '5' and user != '6' and user != '7':

        if user == 1:
            page1 = requests.get("https://en.wikipedia.org/wiki/Cristiano_Ronaldo")
            # scrape webpage
            soup1 = BeautifulSoup(page1.content, 'html.parser')
            # create object
            object1 = soup1.find(id="mw-content-text")
            # find tags
            items1 = object1.find_all(class_="infobox vcard")
            result1 = items1[0]
            b1 = result1.prettify()
            f1 = open("check.txt", "w")  # for unavailable file it will automatically create file
            f1.write(b1)
            f1.write("\n")
            f1.close()
            file1 = open("check.txt")
            all_lines1 = file1.readlines()
            print('Name: ', all_lines1[2])
            print('country: ', all_lines1[13])
            print('Full name: ', all_lines1[32])
            print('D.O.B: ', all_lines1[52])
            print('Place of Birth: ', all_lines1[69])
            print('Height: ', all_lines1[88])
            print('Position: ', all_lines1[102])
            print('Club: ', all_lines1[119])
            print('Number: ', all_lines1[128])

        elif user == 2:
            page2 = requests.get("https://en.wikipedia.org/wiki/Lionel_Messi")
            soup2 = BeautifulSoup(page2.content, 'html.parser')
            # create object
            object2 = soup2.find(id="mw-content-text")
            # find tags
            items2 = object2.find_all(class_="infobox vcard")
            result2 = items2[0]
            b2 = result2.prettify()
            f2 = open("check.txt", "w")  # for unavailable file it will automatically create file
            f2.write(b2)
            f2.write("\n")
            f2.close()
            file2 = open("check.txt")
            all_lines2 = file2.readlines()
            print('Name: ', all_lines2[2])
            print('country: ', all_lines2[13])
            print('Full name: ', all_lines2[32])
            print('D.O.B: ', all_lines2[52])
            print('Place of Birth: ', all_lines2[69])
            print('Height: ', all_lines2[79])
            print('Position: ', all_lines2[93])
            print('Club: ', all_lines2[110])
            print('Number: ', all_lines2[119])


        elif user == 3:

            page3 = requests.get("https://en.wikipedia.org/wiki/Neymar")
            # scrape webpage
            soup3 = BeautifulSoup(page3.content, 'html.parser')

            # create object
            object3 = soup3.find(id="mw-content-text")

            # find tags
            items3 = object3.find_all(class_="infobox vcard")

            result3 = items3[0]
            b3 = result3.prettify()

            f3 = open("check.txt", "w")  # for unavailable file it will automatically create file
            f3.write(b3)
            f3.write("\n")
            f3.close()
            file3 = open("check.txt")
            all_lines3 = file3.readlines()
            print('Name: ', all_lines3[2])
            print('country: ', all_lines3[13])
            print('Full name: ', all_lines3[32])
            print('D.O.B: ', all_lines3[52])
            print('Place of Birth: ', all_lines3[69])
            print('Height: ', all_lines3[84])
            print('Position: ', all_lines3[108])
            print('Club: ', all_lines3[125])
            print('Number: ', all_lines3[134])

        elif user == 4:
            page4 = requests.get("https://en.wikipedia.org/wiki/Virgil_van_Dijk")
            # scrape webpage
            soup4 = BeautifulSoup(page4.content, 'html.parser')

            # create object
            object4 = soup4.find(id="mw-content-text")

            # find tags
            items4 = object4.find_all(class_="infobox vcard")

            result4 = items4[0]
            b4 = result4.prettify()

            f4 = open("check.txt", "w")  # for unavailable file it will automatically create file
            f4.write(b4)
            f4.write("\n")
            f4.close()
            file4 = open("check.txt")
            all_lines4 = file4.readlines()
            print('Name: ', all_lines4[2])
            print('country: ', all_lines4[13])
            print('Full name: ', all_lines4[29])
            print('D.O.B: ', all_lines4[49])
            print('Place of Birth: ', all_lines4[66])
            print('Height: ', all_lines4[76])
            print('Position: ', all_lines4[90])
            print('Club: ', all_lines4[107])
            print('Number: ', all_lines4[116])

        elif user == 5:
            page5 = requests.get("https://en.wikipedia.org/wiki/N%27Golo_Kant%C3%A9")
            # scrape webpage
            soup5 = BeautifulSoup(page5.content, 'html.parser')

            # create object
            object5 = soup5.find(id="mw-content-text")

            # find tags
            items5 = object5.find_all(class_="infobox vcard")

            result5 = items5[0]
            b5 = result5.prettify()

            f5 = open("check.txt", "w")  # for unavailable file it will automatically create file
            f5.write(b5)
            f5.write("\n")
            f5.close()
            file5 = open("check.txt")
            all_lines5 = file5.readlines()
            print('Name: ', all_lines5[2])
            print('country: ', all_lines5[13])
            print('Full name: ', all_lines5[29])
            print('D.O.B: ', all_lines5[49])
            print('Place of Birth: ', all_lines5[66])
            print('Height: ', all_lines5[76])
            print('Position: ', all_lines5[90])
            print('Club: ', all_lines5[107])
            print('Number: ', all_lines5[116])

        elif user == 6:
            page6 = requests.get("https://en.wikipedia.org/wiki/Paul_Pogba")
            # scrape webpage
            soup6 = BeautifulSoup(page6.content, 'html.parser')

            # create object
            object6 = soup6.find(id="mw-content-text")

            # find tags
            items6 = object6.find_all(class_="infobox vcard")

            result6 = items6[0]
            b6 = result6.prettify()

            f6 = open("check.txt", "w")  # for unavailable file it will automatically create file
            f6.write(b6)
            f6.write("\n")
            f6.close()
            file6 = open("check.txt")
            all_lines6 = file6.readlines()
            print('Name: ', all_lines6[2])
            print('country: ', all_lines6[13])
            print('Full name: ', all_lines6[32])
            print('D.O.B: ', all_lines6[52])
            print('Place of Birth: ', all_lines6[69])
            print('Height: ', all_lines6[79])
            print('Position: ', all_lines6[93])
            print('Club: ', all_lines6[110])
            print('Number: ', all_lines6[119])

        elif user == 7:
            page7 = requests.get("https://en.wikipedia.org/wiki/Thomas_M%C3%BCller")
            # scrape webpage
            soup7 = BeautifulSoup(page7.content, 'html.parser')

            # create object
            object7 = soup7.find(id="mw-content-text")

            # find tags
            items7 = object7.find_all(class_="infobox vcard")

            result7 = items7[0]
            b7 = result7.prettify()

            f7 = open("check.txt", "w")  # for unavailable file it will automatically create file
            f7.write(b7)
            f7.write("\n")
            f7.close()
            file7 = open("check.txt")
            all_lines7 = file7.readlines()
            print('Name: ', all_lines7[2])
            print('country: ', all_lines7[13])
            print('Full name: ', all_lines7[29])
            print('D.O.B: ', all_lines7[49])
            print('Place of Birth: ', all_lines7[68])
            print('Height: ', all_lines7[76])
            print('Position: ', all_lines7[90])
            print('Club: ', all_lines7[111])
            print('Number: ', all_lines7[120])

        user2 = input("Do you want see again player profile (yes/no)?: ").lower()
        if user2 in ['yes', 'y']:
            continue
        else:
            print("************EXIT***********")
            break
