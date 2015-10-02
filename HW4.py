

#{'POS1': {'POS2': 3, 'POS4': 2}, 'POS2': {'POS1': 9, 'POS5': 3}}
#dict['POS1']['POS2']

dict = {}
prev = None
pos = None

pos_trainer = file('training.pos', 'r')

#pos_trainer = file('training2.pos', 'r')


"""
Gets input and returns a dictionary with the counts of how many times each word/pos tag succeeds another. A 'TOTAL' key
with the total number of times the word/pos tag is succeeded is included as well.
Input:
    trainer: a standard input file provided for this assignment.
    pos_or_word: 0 to get counts of words, 1 to get counts of pos tags
Returns:
    A dict of the format:
    {'VB': {'PRP$': 1, 'PRP': 2, 'TOTAL': 3}, 'NN': {'.': 1, 'TOTAL': 2,'IN': 1,}, 'PRP$': {'NN': 1, 'TOTAL': 1}}
    meaning that a VB was followed by a PRP$ once and a PRP twice, NN ws followed by a . once and an IN once, etc...
"""
def get_counts(trainer, pos_or_word):

    dict = {}
    selection = None
    prev = None

    for line in trainer:
        if line.strip() != '':
            selection = line.split()[pos_or_word]
            if selection not in dict:
                dict[selection] = {'TOTAL':0}
            if prev != None:
                if dict[prev].has_key(selection):
                    dict[prev][selection] += 1
                else:
                    dict[prev][selection] = 1.0
                dict[prev]['TOTAL'] += 1
            prev = selection
        else:
            prev = None

    return dict


"""
Input:
    Takes a dictionary in the format returned by get_counts().
Functionality:
    Replaces the counts of how many times a word/pos tag succeeds another with probabilities of succeeding
    its predecessor.
"""
def get_probabilities(dict):
    for key in dict:
        for key2 in dict[key]:
            if key2 != 'TOTAL':
                dict[key][key2] = dict[key][key2] / dict[key]['TOTAL']

    return dict


dict = get_probabilities(get_counts(pos_trainer, 1))

print dict['JJ']['DT']















