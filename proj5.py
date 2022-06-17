def gen_quiz(qpool, *args, altcodes, quiz = None):
    if altcodes is None:
        altcodes = []
    if len(altcodes) == 0:
        altcodes = ['A', 'B', 'C', 'D', 'E', 'F']
    if not quiz:
        quiz = []
    for i in args:
        try:
            adding = qpool[i]
        except IndexError as exception_text:
            print('Ignoring index ' + str(i) + ' - ' + str(exception_text))
        else:
            list_of_answers = []
            alt_strings = [str(processing) for processing in altcodes]
            for answer in zip(alt_strings, adding[1]):
                string = answer[0] + ': ' + answer[1]
                list_of_answers.append(string)
            add = (adding[0], list_of_answers)
            quiz.append(add)
    return quiz
    
