import sys
import json


# вывести количество вопросов (questions)
def count_questions(data: dict):
    counter = 0
    if 'game' in data and 'rounds' in data['game']:
        for round_data in data['game']['rounds']:
            if 'questions' in round_data:
                counter += len(round_data['questions'])
    print(f"Total questions: {counter}")

def print_right_answers(data: dict):
    if 'game' in data and 'rounds' in data['game']:
        for round_data in data['game']['rounds']:
            if 'questions' in round_data:
                for question in round_data['questions']:
                    if 'correct_answer' in question:
                        print(f"Right answers: {question['correct_answer']}")



def print_max_answer_time(data: dict):
    max_time = 0
    if 'game' in data and 'rounds' in data['game']:
        for round_data in data['game']['rounds']:
            if 'questions' in round_data:
                for question in round_data['questions']:
                    if 'time_to_answer' in question and question['time_to_answer'] > max_time:
                        max_time = question['time_to_answer']
    print(f"Maximum nswer time : {max_time}")


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)
    #print(data)

if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    #testing
    filename = "./test.json"

    #command line input
    # if len(sys.argv) != 2:
    #     sys.exit(1)
    #
    # filename = sys.argv[1]
    main(filename)