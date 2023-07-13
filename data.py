import csv


class ReadData:
    def __init__(self) -> None:
        pass

    def read_file(self, path):
        with open(path, 'r') as fp:
            reader = csv.reader(fp)
            # 跳过表头，读取采集变量
            next(reader)
            g = next(reader)
            # 获取采集变量
            # print(g)
            file = {}
            file['num'] = []
            del g[-1]
            # print(lenth)
            for item in g:
                file[item] = []
            for row in reader:
                if len(row) != len(g) + 1:
                    continue
                i = 0
                for key in file:
                    if i == 0:
                        num = row[0].split(";")[0][1:]
                        file[key].append(num)
                    elif i == 1:
                        file[key].append(float(row[0].split(';')[1]))
                    else:
                        file[key].append(float(row[i-1]))
                    i += 1
        return file


# reader = ReadData()
# file = reader.read_file(path="CA-Sample-cnt40.data")

# for key in file:
#     print(key)
#     print(file[key])