from tqdm import tqdm

with open("lab.csv",encoding="utf8") as fp:

    for i, line in tqdm(enumerate(fp)):
        with open("lab-test.csv", "a+", encoding="utf8") as fp2:
            if (i<200):
                try:
                    fp2.write(line)
                except:
                    continue

            else:
                fp2.close()
                break
