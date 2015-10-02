from sys import argv


training_file = file(argv[1], 'r')

input_file = file(argv[2], 'r')

output_file = file(argv[3], 'w')




"""
Gets input and returns a dictionary with the counts of how many times each pos tag succeeds another. A 'TOTAL' key
with the total number of times the word/pos tag is succeeded is included as well.
Input:
    trainer: a standard input file provided for this assignment.
Returns:
    A dict of the format:
    {'VB': {'PRP$': 1, 'PRP': 2, 'TOTAL': 3}, 'NN': {'.': 1, 'TOTAL': 2,'IN': 1,}, 'PRP$': {'NN': 1, 'TOTAL': 1}}
    meaning that a VB was followed by a PRP$ once and a PRP twice, NN ws followed by a . once and an IN once, etc...
"""
def get_pos_counts(trainer):

    dict = {}
    selection = None
    prev = None

    for line in trainer:
        if line.strip() != '':
            selection = line.split()[1]
            if selection not in dict:
                dict[selection] = {'TOTAL':0}
            if prev != None:
                if dict[prev].has_key(selection):
                    dict[prev][selection] += 1
                else:
                    dict[prev][selection] = 1
                dict[prev]['TOTAL'] += 1
            prev = selection
        else:
            prev = None

    return dict


"""
Gets input and returns a dictionary with the counts of how many times each word was labeled for each specific tag. A
'TOTAL' key with the total number of times the tag was found is also included with each tag's dictionary.
Input:
    trainer: a standard input file provided for this assignment.
Returns:
    A dict of the format:
    {'VB': {'run': 1, 'hit': 1, 'TOTAL': 2}, 'NN': {'while': 1, 'TOTAL': 4, 'job': 1, 'horse': 2}}
    meaning that there was two words labeled VB one time: run and hit, horse was labeled a NN twice, etc...
"""
def get_word_counts(trainer):

    dict = {}

    for line in trainer:
        if line.strip() != '':
            line = line.split()
            if line[1] not in dict:
                dict[line[1]] = {'TOTAL': 1, line[0]: 1}
            else:
                if line[0] in dict[line[1]]:
                    dict[line[1]][line[0]] += 1
                else:
                    dict[line[1]][line[0]] = 1
                dict[line[1]]['TOTAL'] += 1


    return dict


"""
Input:
    Takes a dictionary with values containing another dictionary that include one 'TOTAL' key.
Functionality:
    Replaces the counts in each value dictionary with probabilities.
e.g.:
    Input:
        {VB:{'run': 2, 'bike': 2, 'TOTAL': 4}, NN:{'duck': 4, 'cow': 2, 'TOTAL': 6}}
    Output:
        {VB:{'run': 0.5, 'bike': 0.5, 'TOTAL': 4}, NN:{'duck': 0.666, 'cow': 0.333, 'TOTAL': 6}}
"""
def get_probabilities(dict):
    for key in dict:
        for key2 in dict[key]:
            if key2 != 'TOTAL':
                dict[key][key2] = float(dict[key][key2]) / dict[key]['TOTAL']

    return dict

"""
Returns a dictionary with keys being the possible parts of speech and their values being the lexical likelihoods
"""
def lexical_probabilities(word, word_probabilities):
    probabilities_dict = {}
    for pos in word_probabilities:
        if word in word_probabilities[pos]:
            probabilities_dict[pos] = word_probabilities[pos][word]

    return probabilities_dict


def tag_words(input, output, pos_probabilities, word_probabilities):
    for line in input:
        word = line[0:-1]

    #TODO compute probabilities



        output.write(line[0:-1] + '\t' +'tag' + '\n')


pos_prob_dict = get_probabilities(get_pos_counts(training_file))
training_file.seek(0)
word_prob_dict = get_probabilities(get_word_counts(training_file))


tag_words(input_file, output_file, pos_prob_dict, word_prob_dict)














