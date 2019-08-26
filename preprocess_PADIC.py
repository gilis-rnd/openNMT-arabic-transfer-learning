def write_sentences_to_dialect_files(path, sentences):
    with open(path, 'w+') as f:
        f.write(''.join(sentences))


def split_padic_to_dialects_files(padic_path):
    MSA_path = 'data/arabic_data/PADIC/dialects/MSA/MSA.txt'
    ALG_path = 'data/arabic_data/PADIC/dialects/ALG/ALG.txt'
    ANB_path = 'data/arabic_data/PADIC/dialects/ANB/ANB.txt'
    TUN_path = 'data/arabic_data/PADIC/dialects/TUN/TUN.txt'
    PAL_path = 'data/arabic_data/PADIC/dialects/PAL/PAL.txt'
    SYR_path = 'data/arabic_data/PADIC/dialects/SYR/SYR.txt'
    MAR_path = 'data/arabic_data/PADIC/dialects/MAR/MAR.txt'


    MSA_sentences = []
    ALG_sentences = []
    ANB_sentences = []
    TUN_sentences = []
    PAL_sentences = []
    SYR_sentences = []
    MAR_sentences = []

    with open(padic_path) as f:
        lines = f.readlines()
        for line in lines:
            if '<MSA>' in line:
                MSA_sentences.append(line.split('<MSA>')[1].replace('</MSA>', ''))
            elif '<ALG>' in line:
                ALG_sentences.append(line.split('<ALG>')[1].replace('</ALG>', ''))
            elif '<ANB>' in line:
                ANB_sentences.append(line.split('<ANB>')[1].replace('</ANB>', ''))
            elif '<TUN>' in line:
                TUN_sentences.append(line.split('<TUN>')[1].replace('</TUN>', ''))
            elif '<PAL>' in line:
                PAL_sentences.append(line.split('<PAL>')[1].replace('</PAL>', ''))
            elif '<SYR>' in line:
                SYR_sentences.append(line.split('<SYR>')[1].replace('</SYR>', ''))
            elif '<MAR>' in line:
                MAR_sentences.append(line.split('<MAR>')[1].replace('</MAR>', ''))

    write_sentences_to_dialect_files(MSA_path, MSA_sentences)
    write_sentences_to_dialect_files(ALG_path, ALG_sentences)
    write_sentences_to_dialect_files(ANB_path, ANB_sentences)
    write_sentences_to_dialect_files(TUN_path, TUN_sentences)
    write_sentences_to_dialect_files(PAL_path, PAL_sentences)
    write_sentences_to_dialect_files(SYR_path, SYR_sentences)
    write_sentences_to_dialect_files(MAR_path, MAR_sentences)

    path_list = []
    path_list.append(MSA_path)
    path_list.append(ALG_path)
    path_list.append(ANB_path)
    path_list.append(TUN_path)
    path_list.append(PAL_path)
    path_list.append(SYR_path)
    path_list.append(MAR_path)
    return path_list


def split_padic_dialect_to_train_dev_test(dialect_path):
    with open(dialect_path) as f:
        lines = f.readlines()
    dev_lines = lines[0:1000]
    test_lines = lines[1000:2000]
    train_lines = lines[2000:]
    print(len(dev_lines))
    print(len(train_lines))
    print(len(test_lines))
    return train_lines, dev_lines, test_lines

def write_list_to_file(path, list):
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(''.join(list))

def write_dialect_to_file(dialect_path, train_lines, dev_lines, test_lines):
    train_path = dialect_path.replace('.txt', '_train.txt')
    test_path = dialect_path.replace('.txt', '_test.txt')
    dev_path = dialect_path.replace('.txt', '_dev.txt')
    write_list_to_file(train_path, train_lines)
    write_list_to_file(test_path, test_lines)
    write_list_to_file(dev_path, dev_lines)



if __name__ == '__main__':
    padic_path = 'data/arabic_data/PADIC/PADIC-23-02-2017.xml'
    dialects_paths = split_padic_to_dialects_files(padic_path)
    for dialect_path in dialects_paths:
        train_lines, dev_lines, test_lines = split_padic_dialect_to_train_dev_test(dialect_path)
        write_dialect_to_file(dialect_path, train_lines, dev_lines, test_lines)