import csv, random, string

def make_output_json(csvFilePath):
    #strip spaces around commas
    with open(csvFilePath, 'r') as f:
        lines = f.readlines()
    f.close()
    print("File successfully opened: "+csvFilePath)
    print("Stripping white spaces around commas")
    lines = [line.replace(', ', ',') for line in lines]
    lines = [line.replace(' ,', ',') for line in lines]
    lines = [line.replace(',  ', ',') for line in lines]
    lines = [line.replace('  ,', ',') for line in lines]
    lines = [line.replace(' , ', ',') for line in lines]
    lines = [line.replace('  ,  ', ',') for line in lines]
    with open(csvFilePath, 'w') as f:
        f.writelines(lines)
    f.close()

    data = {} 
    # Open a csv reader called DictReader 
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        count = 1000
        # Convert each row into a dictionary  
        # and add it to data 
       
        #WRITE OUT
        f = open('QuestionList.json', 'w')
        print("Output file started: QuestionList.json")
        f.write('[')
        for rows in csvReader: 
            # Assuming a column named 'No' to 
            # be the primary key 
            key = rows['_id'] 
            data[key] = rows 

            count = count + 1
            random_values = get_random_alphanumeric_string(24)

            #ID START
            f.write('{\n')
            f.write('  "_id": {\n')
            f.write('    "$oid": "'+random_values+'"\n')
            f.write('  },\n')
            #ID END
            #CAT START
            f.write('  "category_id": {\n')
            f.write('    "$oid": "'+rows['category_id']+'"\n')
            f.write('  },\n')
            #CAT END
            #QUES START
            f.write('  "question": "'+rows['question']+'",\n')
            f.write('  "possible_answers": [\n')
            f.write('    "'+rows['possible_answer1']+'",\n')
            f.write('    "'+rows['possible_answer2']+'",\n')
            f.write('    "'+rows['possible_answer3']+'",\n')
            f.write('    "'+rows['possible_answer4']+'"\n')
            f.write('  ],\n')
            f.write('  "correct_answer": "'+rows['correct_answer']+'"\n')
            f.write('},')
            #QUES END
            print("JSON entry "+str(count-1000)+" created succesfully.")
    f.write(']')
    f.close()
    print("JSON file created successfully!!")

#borrowed from https://pynative.com/python-generate-random-string/
def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(length)))

csvFilePath = r'QuestionList.csv'

make_output_json(csvFilePath)