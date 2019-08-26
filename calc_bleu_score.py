from nltk.translate.bleu_score import sentence_bleu
from statistics import mean



PAL = True
SYR = False
if __name__ == '__main__':
    real_translation_path =  'data/arabic_data/PADIC/dialects/english_translation/english_msa_translation_test.txt'
    if PAL:
        pred_transaltion_path = 'data/arabic_data/PADIC/results/translation_of_pal_test'
        # pred_transaltion_path = 'data/arabic_data/PADIC/dialects/english_translation/english_msa_translation_test.txt'
    if SYR:
        pred_transaltion_path = 'data/arabic_data/PADIC/results/translation_of_syr_test.txt'
    scores = []
    counter = 0

    with open(real_translation_path) as f:
        real_translation_sents = f.readlines()
    with open(pred_transaltion_path) as f:
        pred_translation_sents = f.readlines()
    for real_trans_sent, pred_trans_sent in zip(real_translation_sents, pred_translation_sents):
        pred_sent_tokens = pred_trans_sent.split()
        # pred_sent_tokens_list = []
        # pred_sent_tokens_list.append(pred_sent_tokens)
        real_trans_sent_tokens = real_trans_sent.split()
        bleu_score = sentence_bleu([pred_sent_tokens], real_trans_sent_tokens)
        if bleu_score != 1.0:
            counter += 1
        #     print(pred_sent_tokens_list, real_trans_sent_tokens)
        #     print("%.2f" % bleu_score)
        #     print('weird!')
        #     print()
        # if bleu_score == 1:
        #     print(pred_sent_tokens_list,real_trans_sent_tokens )
        print("%.2f" % bleu_score)
        scores.append(bleu_score)
    print('counter:')
    print(counter)
    print("mean bleu score over all test sentences: ")
    print("%.2f" % mean(scores))
