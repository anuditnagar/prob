import re
from tqdm import tqdm

with open("lab.csv",encoding="utf8") as fp:
    for i, line in tqdm(enumerate(fp)):
        with open("lab-q2.csv", "a+") as myfile:
            st = re.sub('question', 'answer', line)
            try:
                myfile.write(st)
            except:
                continue
