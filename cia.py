# -*- coding: utf-8 -*-

with open('dna.txt') as dna_log:
    dna = dna_log.read()


hair_list = [('Black' ,'CCAGCAATCGC'), ('Brown','GCCAGTGCCG'), ('Blonde','TTAGCTATCGC')]
face_list = [('Square' ,'GCCACGG'), ('Round','ACCACAA'), ('Oval','AGGCCTCA')]
eye_list = [('Blue' ,'TTGTGGTGGC'), ('Green','GGGAGGTGGC'), ('Brown','AAGTAGTGAC')]
gender_list = [('Female' ,'TGAAGGACCTTC'), ('Male','TGCAGGAACTTC')]
race_list = [('White' ,'AAAACCTCA'), ('Black','CGACTACAG'), ('Asian','CGCGGGCCG')]

suspects = {'Eva': ['Female', 'White', 'Blonde', 'Blue', 'Oval'],
            'Larisa': ['Female', 'White', 'Brown', 'Brown', 'Oval'],
            'Matej': ['Male', 'White', 'Black', 'Blue', 'Oval'],
            'Miha': ['Male', 'White', 'Brown', 'Green', 'Square']}

unknown_person = []

for hair in hair_list:
    if hair[1] in dna:
        unknown_person.append(hair[0])
for face in face_list:
    if face[1] in dna:
        unknown_person.append(face[0])
for eye in eye_list:
    if eye[1] in dna:
        unknown_person.append(eye[0])
for gender in gender_list:
    if gender[1] in dna:
        unknown_person.append(gender[0])
for race in race_list:
    if race[1] in dna:
        unknown_person.append(race[0])

for suspect, property in suspects.items():
    if len(set(unknown_person) & set(property)) == 5:
        print "Glavni požeruh je: %s" % suspect


