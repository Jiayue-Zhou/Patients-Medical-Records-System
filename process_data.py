import pandas as pd
from people import People

df = pd.read_csv('C:/Users/zjy/Desktop/Final_dataset_covid19(1).csv')

print(df.shape[0])


def make_people(sl):
    return People(str(sl[0]), sl[1], str(sl[2]), str(sl[3]), str(sl[4]), str(sl[5]), str(sl[6]), str(sl[7]), str(sl[8]),
                  str(sl[9]), str(sl[10]), str(sl[11]), str(sl[12]), str(sl[13]), str(sl[14]), str(sl[15]), sl[16],
                  sl[17], sl[18], sl[19])


def processingData():
    ll = df.values.tolist()
    result = []
    for i in range(df.shape[0]):
        pp = make_people(ll[i])
        result.append(pp)
    return result


# if __name__ == "__main__":
#     #print("Hello World!");
#     result = processingData();
#     print(result[0].MCH)
# print(df.values.tolist())
