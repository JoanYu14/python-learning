import pickle

# 初始化變數
x = 10
y = [1, 2, 3, 4, 5]
z = (2, 3, 4)

# 定義函數以保存資料
def save_data():
    global x, y, z  # 聲明使用全域變數
    # 建立一個字典來保存變數
    dirc = {"x": x, "y": y, "z": z}
    # 以二進制寫入模式開啟文件
    with open("pickle_file", mode="wb") as p_file:
        # 使用 pickle 模組將字典序列化並寫入文件
        pickle.dump(dirc, p_file)

# 呼叫函數以保存資料
save_data()

# 定義函數以讀取資料
def read_data():
    global value_x, value_y, value_z  # 聲明將設置的全域變數
    # 以二進制讀取模式開啟文件
    with open("pickle_file", mode="rb") as p_file:
        # 使用 pickle 模組讀取並反序列化文件中的內容
        deserialize_file = pickle.load(p_file)
        # 遍歷反序列化後的字典
        for key in deserialize_file.keys():
            # 使用 globals() 動態創建全域變數並賦值
            globals()[f"value_{key}"] = deserialize_file[key]



# 呼叫函數以讀取資料並設置全域變數
read_data()
# 檢查全域變數是否已經正確設置
print(f"value_x: {value_x}")
print(f"value_y: {value_y}")
print(f"value_z: {value_z}")