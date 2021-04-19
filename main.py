# quiz app
import random
import matplotlib.pylab
questions = {1: "What is the Full Form of INTERNET ?", 2: "which one is a computer language",
             3: "Ctrl, Shift and Alt are called .......... keys.",
             4: "MS-Word is an example of _____", 5: "A computer cannot boot if it does not have the ___",
             6: "_______ is the process of dividing the disk into tracks and sectors",
             7: "Junk e-mail is also called ______",
             8: "____are attempts by individuals to obtain confidential information from you by falsifying their identity",
             9: "Microsoft Office is an example of a", 10: "By default, your documents print in ________ mode", }

answers = {1: 'a', 2: 'a', 3: 'a', 4: 'c', 5: 'c', 6: 'b', 7: 'a', 8: 'a', 9: 'c', 10: 'b'}
index = []
options = {1: ['A)INTERnational-NETwork which is the interconnected network of all the Web Servers worldwide ',
               'B)International network of science',
               'C) INTERNATIONAL NET WORTH OF INDIA',
               'D) INTERNET WORKS HERE'],
           2: ['A) c++', 'B) mango', 'C) tupple', 'D) rw'],
           3: ['A) modifier	', 'B) function', 'C) alphanumeric', 'D) adjustment'],
           4: ['A) An operating system', '	B) A processing device',
               'C) Application software', '	D) An input device'],
           5: ['A) Compiler', '	B) Loader',
               'C) Operating system', '	D) Assembler'],
           6: ['A) Tracking', '	B) Formatting',
               'C) Crashing', '	D) Allotting'],
           7: ['A) Spam	', 'B) Spoof',
               'C) Sniffer script', '	D) Spool'],
           8: ['A) Phishing trips', '	B) Computer viruses',
               'C) Phishing scams', '	D) Spyware scams'],
           9: ['A) Closed source software', '	B) Open source software',
               'C) Horizontal market software', '	D) vertical market software'],
           10: ['A) Landscape	', 'B) Portrait',
                'C) Page Setup', '	D) Print View'],
           }

def showresult(score):
    if score >=30:
        print('********** PASS **********')
        print('**** Your score is: '+str(score)+' out of 50 ****\n')
        #print('**** Number of correct answers ='+ str(count)+' ****\n\n')


    else:
        print('better luck next time')
        print('**** Your score is: '+str(score)+' out of 50 ****\n\n')


def startquiz(arr):
    global count
    print(arr)
    score = 0
    for i in range(0, 5, 1):
        p = arr[i]
        print('Question ' + str(i + 1) + ': ' + questions[p]+'\n')
        print('**** type a,b,c,d of selected options: ****\n')
        print(options[p])
        ans = input('your answer: ')

        if ans == answers[p]:

            score = score + 10
        else:
            score = score-5
        print("\n \n")

    showresult(score)
check = 1
while check == True:
    choice = int(input('enter choice 1 ,2 or 3\n 1 for start game \n 2 for rules\n 3 for exit \n'))
    if choice == 1:
        print('****** start game ******\n')
        for i in range(10):
            r = random.randint(1, 10)
            if r not in index and len(index) < 5:
                index.append(r)

            elif len(index) == 5:
                break
            else:
                continue
        startquiz(index)


    elif choice==2:
        print(
            'rules: \n 1. you will get 5 questions \n2. if you answer correctly you will get 10 marks if you answered wrong 5 marks will be deducted\n'
            '3. if you score more than 30 you will pass\n ')
    elif choice ==3:
        break
    else:
        exit()
