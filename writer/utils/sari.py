# =======================================================
#  SARI -- Text Simplification Tunable Evaluation Metric
# =======================================================
#
# Author: Wei Xu (UPenn xwe@cis.upenn.edu)
#
# A Python implementation of the SARI metric for text simplification
# evaluation in the following paper
#
#     "Optimizing Statistical Machine Translation for Text Simplification"
#     Wei Xu, Courtney Napoles, Ellie Pavlick, Quanze Chen and Chris Callison-Burch
#     In Transactions of the Association for Computational Linguistics (TACL) 2015
#
# There is also a Java implementation of the SARI metric
# that is integrated into the Joshua MT Decoder. It can
# be used for tuning Joshua models for a real end-to-end
# text simplification model.
#

from __future__ import division
from collections import Counter
import sys


def ReadInFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    return lines


def SARIngram(sgrams, cgrams, rgramslist, numref, asreward=False):
    rgramsall = [rgram for rgrams in rgramslist for rgram in rgrams]
    rgramcounter = Counter(rgramsall)
    # if asreward:
    #     for rgram, scount in rgramcounter.items():
    #         rgramcounter[rgram] = 1

    sgramcounter = Counter(sgrams)
    sgramcounter_rep = Counter()
    for sgram, scount in sgramcounter.items():
        sgramcounter_rep[sgram] = scount * numref
        if asreward:
            sgramcounter_rep[sgram] = numref

    cgramcounter = Counter(cgrams)
    cgramcounter_rep = Counter()
    for cgram, ccount in cgramcounter.items():
        cgramcounter_rep[cgram] = ccount * numref
        if asreward:
            cgramcounter_rep[cgram] = numref

    # KEEP
    keepgramcounter_rep = sgramcounter_rep & cgramcounter_rep
    keepgramcountergood_rep = keepgramcounter_rep & rgramcounter
    keepgramcounterall_rep = sgramcounter_rep & rgramcounter

    keeptmpscore1 = 0
    keeptmpscore2 = 0
    for keepgram in keepgramcountergood_rep:
        keeptmpscore1 += keepgramcountergood_rep[keepgram] / keepgramcounter_rep[keepgram]
        keeptmpscore2 += keepgramcountergood_rep[keepgram] / keepgramcounterall_rep[keepgram]
        # print "KEEP", keepgram, keepscore, cgramcounter[keepgram], sgramcounter[keepgram], rgramcounter[keepgram]
    keepscore_precision = 0
    if len(keepgramcounter_rep) > 0:
        keepscore_precision = keeptmpscore1 / len(keepgramcounter_rep)
    keepscore_recall = 0
    if len(keepgramcounterall_rep) > 0:
        keepscore_recall = keeptmpscore2 / len(keepgramcounterall_rep)
    keepscore = 0
    if keepscore_precision > 0 or keepscore_recall > 0:
        keepscore = 2 * keepscore_precision * keepscore_recall / (keepscore_precision + keepscore_recall)

    # DELETION
    delgramcounter_rep = sgramcounter_rep - cgramcounter_rep
    delgramcountergood_rep = delgramcounter_rep - rgramcounter
    delgramcounterall_rep = sgramcounter_rep - rgramcounter

    deltmpscore1 = 0
    deltmpscore2 = 0
    for delgram in delgramcountergood_rep:
        deltmpscore1 += delgramcountergood_rep[delgram] / delgramcounter_rep[delgram]
        deltmpscore2 += delgramcountergood_rep[delgram] / delgramcounterall_rep[delgram]
    delscore_precision = 0
    if len(delgramcounter_rep) > 0:
        delscore_precision = deltmpscore1 / len(delgramcounter_rep)
    delscore_recall = 0
    if len(delgramcounterall_rep) > 0:
        delscore_recall = deltmpscore1 / len(delgramcounterall_rep)
    delscore = 0
    if delscore_precision > 0 or delscore_recall > 0:
        delscore = 2 * delscore_precision * delscore_recall / (delscore_precision + delscore_recall)

    # ADDITION
    addgramcounter = set(cgramcounter) - set(sgramcounter)
    addgramcountergood = set(addgramcounter) & set(rgramcounter)
    addgramcounterall = set(rgramcounter) - set(sgramcounter)

    addtmpscore = 0
    for addgram in addgramcountergood:
        addtmpscore += 1

    addscore_precision = 0
    addscore_recall = 0
    if len(addgramcounter) > 0:
        addscore_precision = addtmpscore / len(addgramcounter)
    if len(addgramcounter) > 0:
        addscore_recall = addtmpscore / len(addgramcounterall)
    addscore = 0
    if addscore_precision > 0 or addscore_recall > 0:
        addscore = 2 * addscore_precision * addscore_recall / (addscore_precision + addscore_recall)

    return (keepscore, delscore_precision, addscore)


def SARIsent(ssent, csent, rsents, asreward=False):
    numref = len(rsents)

    s1grams = ssent.lower().split(" ")
    c1grams = csent.lower().split(" ")
    s2grams = []
    c2grams = []
    s3grams = []
    c3grams = []
    s4grams = []
    c4grams = []

    r1gramslist = []
    r2gramslist = []
    r3gramslist = []
    r4gramslist = []
    for rsent in rsents:
        r1grams = rsent.lower().split(" ")
        r2grams = []
        r3grams = []
        r4grams = []
        r1gramslist.append(r1grams)
        for i in range(0, len(r1grams) - 1):
            if i < len(r1grams) - 1:
                r2gram = r1grams[i] + " " + r1grams[i + 1]
                r2grams.append(r2gram)
            if i < len(r1grams) - 2:
                r3gram = r1grams[i] + " " + r1grams[i + 1] + " " + r1grams[i + 2]
                r3grams.append(r3gram)
            if i < len(r1grams) - 3:
                r4gram = r1grams[i] + " " + r1grams[i + 1] + " " + r1grams[i + 2] + " " + r1grams[i + 3]
                r4grams.append(r4gram)
        r2gramslist.append(r2grams)
        r3gramslist.append(r3grams)
        r4gramslist.append(r4grams)

    for i in range(0, len(s1grams) - 1):
        if i < len(s1grams) - 1:
            s2gram = s1grams[i] + " " + s1grams[i + 1]
            s2grams.append(s2gram)
        if i < len(s1grams) - 2:
            s3gram = s1grams[i] + " " + s1grams[i + 1] + " " + s1grams[i + 2]
            s3grams.append(s3gram)
        if i < len(s1grams) - 3:
            s4gram = s1grams[i] + " " + s1grams[i + 1] + " " + s1grams[i + 2] + " " + s1grams[i + 3]
            s4grams.append(s4gram)

    for i in range(0, len(c1grams) - 1):
        if i < len(c1grams) - 1:
            c2gram = c1grams[i] + " " + c1grams[i + 1]
            c2grams.append(c2gram)
        if i < len(c1grams) - 2:
            c3gram = c1grams[i] + " " + c1grams[i + 1] + " " + c1grams[i + 2]
            c3grams.append(c3gram)
        if i < len(c1grams) - 3:
            c4gram = c1grams[i] + " " + c1grams[i + 1] + " " + c1grams[i + 2] + " " + c1grams[i + 3]
            c4grams.append(c4gram)

    (keep1score, del1score, add1score) = SARIngram(s1grams, c1grams, r1gramslist, numref, asreward)
    (keep2score, del2score, add2score) = SARIngram(s2grams, c2grams, r2gramslist, numref, asreward)
    (keep3score, del3score, add3score) = SARIngram(s3grams, c3grams, r3gramslist, numref, asreward)
    (keep4score, del4score, add4score) = SARIngram(s4grams, c4grams, r4gramslist, numref, asreward)

    avgkeepscore = sum([keep1score, keep2score, keep3score, keep4score]) / 4
    avgdelscore = sum([del1score, del2score, del3score, del4score]) / 4
    avgaddscore = sum([add1score, add2score, add3score, add4score]) / 4
    finalscore = (avgkeepscore + avgdelscore + avgaddscore) / 3

    # avgkeepscore = sum([keep1score]) / 1
    # avgdelscore = sum([del1score]) / 1
    # avgaddscore = sum([add1score]) / 1
    # finalscore = (avgkeepscore + avgdelscore + avgaddscore) / 3

    return finalscore


# Our implementation of corpus-level SARI
# Align with Dress
import os
import re
import subprocess
from util.mteval_bleu import MtEval_BLEU

class CorpusSARI(MtEval_BLEU):

    def get_sari_from_joshua(self, step, path_dst, path_ref, path_src, targets):
        path_tar = self.model_config.resultdir + '/joshua_target_%s.txt' % step
        if not os.path.exists(path_tar):
            f = open(path_tar, 'w', encoding='utf-8')
            # joshua require lower case
            f.write(self.result2txt(targets, lowercase=True))
            f.close()
        if self.model_config.num_refs > 0:
            return self.get_sari_result_joshua(path_ref, path_src, path_tar)
        else:
            return self.get_sari_result_joshua_nonref(path_dst, path_src, path_tar)

    def get_sari_result_joshua(self, path_ref, path_src, path_tar):
        args = ' '.join(['bash', self.model_config.corpus_sari_script,
                         path_tar, path_ref, path_src,
                         self.model_config.joshua_class, str(self.model_config.num_refs)])

        pipe = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        mteval_result = pipe.communicate()

        m = re.search(b'STAR = ([\d+\.]+)', mteval_result[0])

        try:
            result = float(m.group(1))
        except AttributeError:
            result = 0
        return result

    def get_sari_result_joshua_nonref(self, path_ref, path_src, path_tar):
        args = ' '.join(['bash', self.model_config.corpus_sari_script_nonref,
                         path_tar, path_ref, path_src,
                         self.model_config.joshua_class])

        pipe = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        mteval_result = pipe.communicate()

        m = re.search(b'STAR = ([\d+\.]+)', mteval_result[0])

        try:
            result = float(m.group(1))
        except AttributeError:
            result = 0
        return result


if __name__ == '__main__':
    # fnamenorm = "./turkcorpus/test.8turkers.tok.norm"
    # fnamesimp = "./turkcorpus/test.8turkers.tok.simp"
    # fnameturk = "./turkcorpus/test.8turkers.tok.turk."

    ssent = "i am zhao yeah ."
    rsents = ['i am zhao3 .', 'i am zhao2 .', 'i am yeah .']

    csent1 = "i am nn ."
    csent2 = "i am zhao ."
    csent3 = 'i am .'


    # rsents = ["About nnn species are currently known .", "About nnn species are now accepted .",
    #           "nnn species are now accepted ."]

    print(SARIsent(ssent, csent1, rsents, True))
    print(SARIsent(ssent, csent2, rsents, True))
    print(SARIsent(ssent, csent3, rsents, True))

    # print(SARIsent(ssent, csent1, rsents, False))
    # print(SARIsent(ssent, csent2, rsents, False))

    # ssent = 'pittsburg is a city located in camp county , texas .'
    # csent = 'Pittsburg is a city of Camp County in the LOCATION@4 .'
    # rsents = ['pittsburg is a city located in camp county , texas .', 'pittsburg is a city in camp county , texas .', 'pittsburg is a city located in camp county , texas .', 'pittsburg is located in camp county , texas .', 'pittsburg is a city located in camp county , texas .', 'pittsburg is a city located in camp county , texas', 'pittsburg is a city in camp county , texas .', 'pittsburg is a city located in camp county , texas .']
# print(SARIsent(ssent, csent, rsents))