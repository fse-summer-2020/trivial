import csv, random, string
from bson import ObjectId

def make_output_json(csvFilePath):
    #strip spaces around commas
    with open(csvFilePath, 'r', encoding='utf-8', errors='ignore') as f:
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
        inputproblem = []
        inputproblemcount = []
        # Convert each row into a dictionary  
        # and add it to data 
       
        #WRITE OUT
        f = open('QuestionList.json', 'w')
        print("Output file started: QuestionList.json")
        f.write('[\n')
        for index, rows in enumerate(csvReader): 
            # Assuming a column named 'No' to 
            # be the primary key 
            key = rows['_id'] 
            data[key] = rows 

            count = count + 1
            #static_lead = "5f399bbc7aef0f2b0c"
            #random_values = get_random_alphanumeric_string(6)
            object_id = str(ObjectId()); #static_lead + random_values

            if (''.join(str(rows['category_id']).lower().split()) == "places"):
                rows['category_id'] = "5f0b7f2a90677a74898769a3"
            elif (''.join(rows['category_id'].lower().split()) == "people"):
                rows['category_id'] = "5f0b7f2a90677a74898769a4"
            elif (''.join(rows['category_id'].lower().split()) == "events"):
                rows['category_id'] = "5f0b7f2a90677a74898769a5"
            elif (''.join(rows['category_id'].lower().split()) == "independencedayholiday" or ''.join(rows['category_id'].lower().split()) == "holiday"):
                rows['category_id'] = "5f0b7f2a90677a74898769a6"
            else:
                raise Exception("Category labeled as: '"+rows['category_id']+"' in the CSV sheet does not exist in the Database, please review CSV category labels")

            #ID START
            if (index != 0):
                f.write(',\n')
            f.write('{\n')
            f.write('  "_id": {')
            f.write('"$oid": "'+object_id+'"')
            f.write('},\n')
            #ID END
            #CAT START
            f.write('  "category_id": {')
            f.write('"$oid": "'+rows['category_id']+'"')
            f.write('},\n')
            #CAT END
            #QUES START
            f.write('  "question": "'+rows['question']+'" ,\n')
            f.write('  "possible_answers": [')
            f.write('"'+rows['possible_answer1']+'",')
            f.write('"'+rows['possible_answer2']+'",')
            f.write('"'+rows['possible_answer3']+'",')
            f.write('"'+rows['possible_answer4']+'"')
            f.write('],\n')
            f.write('  "correct_answer": "'+rows['correct_answer']+'"\n')
            f.write('}\n')
            #QUES END
            if (rows['correct_answer'] == rows['possible_answer1']):
                check = True
            elif (rows['correct_answer'] == rows['possible_answer2']):
                check = True
            elif (rows['correct_answer'] == rows['possible_answer3']):
                check = True
            elif (rows['correct_answer'] == rows['possible_answer4']):
                check = True
            else:
                check = False

            if (check == True):
                print("JSON entry "+str(count-1000)+" created succesfully.")
            else:
                print("JSON entry "+str(count-1000)+" created with an error...")
                inputproblem.append(rows['correct_answer'])
                inputproblemcount.append(str(count-1000))
    
    f.write(']')
    f.close()

    if (len(inputproblem) == 0):
        print("~~~ JSON file created successfully!! ~~~")
    else:
        print("***WARNING: JSON file NOT created successfully!! ***")
        for idx, prob in enumerate(inputproblem):
            print("  ~~~: JSON entry number "+inputproblemcount[idx]+" answer does not have any potential answers that match: "+prob)

#borrowed from https://pynative.com/python-generate-random-string/
def get_random_alphanumeric_string(length):
    return ''.join((random.choice(string.digits) for i in range(length)))

csvFilePath = r'QuestionList.csv'

make_output_json(csvFilePath)