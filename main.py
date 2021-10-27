from collections import Counter


def max_occ(lst, x):
    count = 0
    for i in lst:
        if (i == x):
            count = count + 1
    return count

lst = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg', 'ccg', 'cca', 'ata', 'cca', 'tat', 'ata', 'cac', 'gcg', 'cca', 'gta', 'gtg', 'gac', 'taa', 'ata',
'gtc', 'aat', 'gct', 'gta', 'ggc', 'tgc', 'tca', 'ctt', 'tgt', 'ata', 'acc', 'tgc', 'gac', 'cgc', 'atc', 'cgt', 'tac', 'agg', 'ctt', 'cgc', 'cgc', 'tgg',
'gcg', 'tgg', 'taa', 'cta', 'aaa', 'tgc', 'cgt', 'tgc', 'gac', 'tta', 'aag', 'taa', 'act', 'cca', 'tac', 'agg', 'cgc', 'gtg', 'cca', 'gcg', 'gtt', 'gag',
'tca', 'aca', 'tct', 'gta', 'ata', 'ctt', 'gat', 'tcg', 'tcg', 'cac', 'cgt', 'tac', 'caa', 'aac', 'ctg', 'tgt', 'aag', 'ttc', 'ccc', 'tcc', 'ctc', 'cct',
'aga', 'gtt', 'tga', 'gaa', 'cct', 'ctc', 'tct', 'ggt', 'gcc', 'tct', 'ccc', 'agt', 'caa', 'gac', 'ccc', 'cgc']

c = Counter(lst)
maximums = [x for x in c if c[x] == c.most_common(1)[0][1]]
x = max(lst, key=lst.count)

print(maximums, max_occ(lst, x),)

