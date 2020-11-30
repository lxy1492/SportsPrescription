'''
心率数据类型
value表示心率值
id表示此数据在序列中的顺序
aerobic表示有氧程度，1代表绝对有氧，-1代表无氧,0-1之间是有氧占比程度

'''

class Heart_Rate():
    def __init__(self,value:int,id:int,aerobic=None):
        self.value = value
        self.id = id
        self.aerobic = aerobic

    def __str__(self):
        return "id:"+str(self.id)+"; value:"+str(self.value)+";"

    @ property
    def Dict(self):
        return {
            "id":self.id,
            "value":self.value,
            "aerobic":self.aerobic,
        }