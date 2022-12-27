import torch
import nltk
#nltk.download('averaged_perceptron_tagger')
#import os
#os.chdir("/content/drive/MyDrive/Edit_NET")
import writer.editnts as editnts
from .editnts import *
from .main import *
from .data import *
from .evaluator import *
from .label_edits import edit2sent

from .checkpoint import Checkpoint

from .data_preprocess import *

def predict(string):


    str_list = string.split('.')
    simple_str_list = string.split('.')
    str_list.pop()
    simple_str_list.pop()
    print(len(str_list))

    train_df = process_raw_data(str_list, simple_str_list)
    editnet_data_to_editnetID(train_df , r'writer\current_prompt')


    vocab = data.Vocab()
    vocab.add_vocab_from_file(r'writer\vocab_data\vocab_30000', 30000)
    vocab.add_embedding(r'writer\vocab_data\glove.6B.100d.txt')

    eval_dataset = data.Dataset(r'writer\current_prompt')

    def sort_by_lens(seq, seq_lengths):
        seq_lengths_sorted, sort_order = seq_lengths.sort(descending=True)
        seq_sorted = seq.index_select(0, sort_order)
        return seq_sorted, seq_lengths_sorted, sort_order


    ckpt = Checkpoint.load(r'writer\checkpoint')

    edit_net = ckpt.model
    edit_net.cpu()

    model = edit_net

    sys_out = []

    for i, batch_df in eval_dataset.batch_generator(batch_size=1, shuffle=False):
                model.eval()
                prepared_batch, syn_tokens_list = data.prepare_batch(batch_df, vocab, 100)  # comp,scpn,simp

                org_ids = prepared_batch[0]
                org_lens = org_ids.ne(0).sum(1)
                org = sort_by_lens(org_ids, org_lens)  # inp=[inp_sorted, inp_lengths_sorted, inp_sort_order]

                org_pos_ids = prepared_batch[1]
                org_pos_lens = org_pos_ids.ne(0).sum(1)
                org_pos = sort_by_lens(org_pos_ids, org_pos_lens)  # inp=[inp_sorted, inp_lengths_sorted, inp_sort_order]

                out = prepared_batch[2][:, :]
                tar = prepared_batch[2][:, 1:]
                simp_ids = prepared_batch[3]

                # best_seq_list = model.beamsearch(org, out,simp_ids, org_ids, org_pos, 5)
                output_without_teacher_forcing = model(org, out, org_ids, org_pos, simp_ids,0.0) #can't compute loss for this one, can only do teacher forcing
                output_teacher_forcing = model(org, out, org_ids, org_pos,simp_ids, 1.0)

                for j in range(output_without_teacher_forcing.size()[0]):
                    ## write beam search here
                    # try:
                    if True:
                        example = batch_df.iloc[j]
                        example_out = output_without_teacher_forcing[j, :, :]

                        ##GREEDY
                        pred_action = torch.argmax(example_out, dim=1).view(-1).data.cpu().numpy()
                        edit_list_in_tokens = data.id2edits(pred_action, vocab)
                        # ###BEST BEAM
                        # edit_list_in_tokens = vocab_data.id2edits(best_seq_list[0][1:], vocab)
                        print(edit_list_in_tokens)

                        greedy_decoded_tokens = ' '.join(edit2sent(example['comp_tokens'], edit_list_in_tokens))
                        greedy_decoded_tokens = greedy_decoded_tokens.split('STOP')[0].split(' ')


                        # tgt_tokens_translated = [vocab.i2w[i] for i in example['simp_ids']]
                        sys_out.append(' '.join(greedy_decoded_tokens))



    result_str = ""

    for strings in sys_out:
        temp_str = strings + ". "
        temp_str = temp_str.capitalize()
        result_str = result_str + temp_str
    
    return result_str