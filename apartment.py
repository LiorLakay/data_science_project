# To reach data:
# json_obj['niobeMinimalClientData'][1][1]['data']['presentation']['stayProductDetailPage']['sections']
#         ['sections][<number>]
# we need to change <number> to the number in the list where the relevant amenities are

# TODO: considering adding one more attribute of 'amenity' as we have for data,
#       then we can iterate easier through all amenities

class Apartment:
    def __init__(self, json_obj):
        self.data = json_obj['niobeMinimalClientData'][1][1]['data']['presentation']['stayProductDetailPage']['sections']
        # self.amenity = json_obj['niobeMinimalClientData'][...]...
    def get_super_host(self):
        return self.data['metadata']['loggingContext']['eventDataLogging']['isSuperhost']

    def get_num_of_rooms(self):
        room_type = self.data['metadata']['loggingContext']['eventDataLogging']['roomType']
        if room_type.find('Private room') != -1:
            return 1
        else:
            # TODO: This is the case where its more than one room.
            #       Implement here the "spot" where we return the # of rooms from the json
            pass

    def get_num_of_guests(self):
        return self.data['metadata']['loggingContext']['eventDataLogging']['personCapacity']

    def get_rate(self):
        return self.data['metadata']['sharingConfig']['starRating']

    def get_review_count(self):
        return self.data['metadata']['sharingConfig']['reviewCount']

    def get_wifi(self):
        pass

    def get_pets_allowed(self):
        pass

    def get_name(self):
        pass