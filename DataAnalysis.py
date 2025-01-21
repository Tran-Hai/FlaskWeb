import pandas as pd

def data_analysis(dataset):

    # Setting name for each column
    columns_name = ['STT','Trạng thái', 'Số chỉ thị', 'Line', 'Tên thiết bị', 'Số quản lí thiết bị', 'Loại công trình',
                    'PP bảo dưỡng', 'Vùng thao tác', 'LK đồng bộ', 'LK không thể tháo rời', 'Mã xử lí', 'Mã hiện tượng',
                    'Mã nguyên nhân', 'Mã nguyên nhân gốc']

    # convert from data from python list into pandas dataframe
    df = pd.DataFrame(dataset, columns=columns_name)
    # Drop the first column which is counting
    df = df.drop(df.columns[0], axis=1)

    return df








