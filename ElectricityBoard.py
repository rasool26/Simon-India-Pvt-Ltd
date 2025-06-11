class ElectricityBoardMain:
    def __init__(self):
        self.__electricityMap = {}

    def getElectricityMap(self):
        return self.__electricityMap

    def setElectricityMap(self, electricityMap):
        self.__electricityMap = electricityMap

    def findCountOfConnectionsBasedOnTheConnectionType(self, connectionType):
        count = 0
        for value in self.__electricityMap.values():
            if value.lower() == connectionType.lower():
                count += 1
        return count if count > 0 else -1

    def findConnectionIdsBasedOnTheConnectionType(self, connectionType):
        result = []
        for key, value in self.__electricityMap.items():
            if value.lower() == connectionType.lower():
                result.append(key)
        return result


if __name__ == "__main__":
    eb = ElectricityBoardMain()
    electricity_map = {}

    print("Enter the number of connection records to be added")
    n = int(input())
    print("Enter the connection records (ConnectionId:Connectiontype)")
    
   
    records = input().strip().split()
    
    if len(records) != n:
        print(f"Expected {n} records but got {len(records)}. Please check input.")
        exit()
    
    for record in records:
        if ":" in record:
            parts = record.split(":", 1)
            if len(parts) == 2:
                connection_id = parts[0].strip()
                connection_type = parts[1].strip()
                electricity_map[connection_id] = connection_type

    eb.setElectricityMap(electricity_map)

    print("Enter the Connection type to be searched")
    search_type = input().strip()
    count = eb.findCountOfConnectionsBasedOnTheConnectionType(search_type)
    if count == -1:
        print(f"No Connection Ids were found for {search_type}")
    else:
        print(f"The count of connection Ids based on {search_type.upper()} are {count}")

    print("Enter the Connection type to identify the Connection Ids")
    filter_type = input().strip()
    ids = eb.findConnectionIdsBasedOnTheConnectionType(filter_type)
    if not ids:
        print(f"No Connection Ids were found for the {filter_type}")
    else:
        print(f"Connection Ids based on the {filter_type.upper()} are")
        for cid in ids:
            print(cid)
