class Service:

    __common_attrs = {"data": 123}
    def __init__(self):
        self.__dict__ = Service.__common_attrs


    def Handler(self, data):
        print("Data:", self.data)
        print('Writing new data:',data)
        self.data = data
        print("Data:",self.data)

    def GetData(self):
        return self.data

if __name__ == "__main__":
    service1 = Service()
    service2 = Service()
    service3 = Service()

    service1.Handler("Hi")
    service3.Handler(12312)
    service2.Handler(True)

    print("________________")
    print("new data:", service1.GetData())