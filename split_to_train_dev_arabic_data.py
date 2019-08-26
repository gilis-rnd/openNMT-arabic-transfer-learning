import os


def get_train_dev_lists(sents_path):
    with open(sents_path) as f:
        lines = f.readlines()
    dev_lines = lines[0:4000]
    test_lines = lines[4000:8000]
    train_lines = lines[8000:]
    print(len(dev_lines))
    print(len(train_lines))
    print(len(test_lines))
    return train_lines, dev_lines, test_lines

def write_list_to_file(path, list):
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(''.join(list))


if __name__ == '__main__':
    data_path = '/home/gilis/PycharmProjects/OpenNMT-py-master/data/arabic_data'
    arabic_sents_path =  os.path.join(data_path, 'arabic_sents')
    english_sents_path = os.path.join(data_path, 'english_sents')

    arabic_train, arabic_dev, arabic_test = get_train_dev_lists(arabic_sents_path)
    english_train, english_dev, english_test = get_train_dev_lists(english_sents_path)
    arabic_train_path = os.path.join(data_path, 'src_train.txt')
    arabic_dev_path = os.path.join(data_path, 'src_dev.txt')
    arabic_test_path = os.path.join(data_path,'src_test.txt')
    english_train_path = os.path.join(data_path, 'tgt_train.txt')
    english_dev_path = os.path.join(data_path, 'tgt_dev.txt')
    english_test_path = os.path.join(data_path,'tgt_test.txt')

    write_list_to_file(arabic_train_path, arabic_train)
    write_list_to_file(arabic_dev_path, arabic_dev)
    write_list_to_file(arabic_test_path, arabic_test)

    write_list_to_file(english_train_path, english_train)
    write_list_to_file(english_dev_path, english_dev)
    write_list_to_file(english_test_path, english_test)


