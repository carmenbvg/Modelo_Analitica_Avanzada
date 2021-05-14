def predict_reservation_status(data={}):
    """ Predictor for reservation_status from model/609ea4f6e4279b13ad004583

        Predictive model by BigML - Machine Learning Made Easy
    """
    if (data.get('is_canceled') is None):
        return u'Check-Out'
    if (data['is_canceled'] == u'0'):
        return u'Check-Out'
    if (data['is_canceled'] == u'1'):
        if (data.get('lead_time') is None):
            return u'Canceled'
        if (data['lead_time'] > 13):
            if (data.get('deposit_type') is None):
                return u'Canceled'
            if (data['deposit_type'] == u'Non Refund'):
                if (data.get('reservation_status_date_day_of_week') is None):
                    return u'Canceled'
                if (data['reservation_status_date_day_of_week'] > 6):
                    if (data.get('arrival_date_day_of_month') is None):
                        return u'Canceled'
                    if (data['arrival_date_day_of_month'] == u'28'):
                        return u'No-Show'
                    if (data['arrival_date_day_of_month'] != u'28'):
                        return u'Canceled'
                if (data['reservation_status_date_day_of_week'] <= 6):
                    return u'Canceled'
            if (data['deposit_type'] != u'Non Refund'):
                if (data.get('adults') is None):
                    return u'Canceled'
                if (data['adults'] > 1):
                    if (data.get('market_segment') is None):
                        return u'Canceled'
                    if (data['market_segment'] == u'Direct'):
                        return u'Canceled'
                    if (data['market_segment'] != u'Direct'):
                        if (data.get('previous_cancellations') is None):
                            return u'Canceled'
                        if (data['previous_cancellations'] == u'0'):
                            if (data['market_segment'] == u'Offline TA/TO'):
                                if (data.get('reservation_status_date_day_of_week') is None):
                                    return u'Canceled'
                                if (data['reservation_status_date_day_of_week'] > 6):
                                    return u'No-Show'
                                if (data['reservation_status_date_day_of_week'] <= 6):
                                    if (data.get('customer_type') is None):
                                        return u'Canceled'
                                    if (data['customer_type'] == u'Transient-Party'):
                                        return u'Canceled'
                                    if (data['customer_type'] != u'Transient-Party'):
                                        return u'Canceled'
                            if (data['market_segment'] != u'Offline TA/TO'):
                                if (data.get('total_of_special_requests') is None):
                                    return u'Canceled'
                                if (data['total_of_special_requests'] > 0):
                                    if (data.get('arrival_date_year') is None):
                                        return u'Canceled'
                                    if (data['arrival_date_year'] == u'2017'):
                                        if (data.get('reservation_status_date_year') is None):
                                            return u'Canceled'
                                        if (data['reservation_status_date_year'] > 2016):
                                            if (data['total_of_special_requests'] > 1):
                                                if (data.get('reservation_status_date_day_of_month') is None):
                                                    return u'Canceled'
                                                if (data['reservation_status_date_day_of_month'] > 23):
                                                    if (data.get('arrival_date_day_of_month') is None):
                                                        return u'Canceled'
                                                    if (data['arrival_date_day_of_month'] == u'24'):
                                                        return u'No-Show'
                                                    if (data['arrival_date_day_of_month'] != u'24'):
                                                        if (data.get('reservation_status_date_month') is None):
                                                            return u'Canceled'
                                                        if (data['reservation_status_date_month'] > 7):
                                                            return u'No-Show'
                                                        if (data['reservation_status_date_month'] <= 7):
                                                            return u'Canceled'
                                                if (data['reservation_status_date_day_of_month'] <= 23):
                                                    return u'Canceled'
                                            if (data['total_of_special_requests'] <= 1):
                                                if (data.get('arrival_date_month') is None):
                                                    return u'Canceled'
                                                if (data['arrival_date_month'] == u'August'):
                                                    return u'Canceled'
                                                if (data['arrival_date_month'] != u'August'):
                                                    if (data.get('reservation_status_date_month') is None):
                                                        return u'Canceled'
                                                    if (data['reservation_status_date_month'] > 4):
                                                        return u'Canceled'
                                                    if (data['reservation_status_date_month'] <= 4):
                                                        return u'Canceled'
                                        if (data['reservation_status_date_year'] <= 2016):
                                            return u'Canceled'
                                    if (data['arrival_date_year'] != u'2017'):
                                        if (data.get('hotel') is None):
                                            return u'Canceled'
                                        if (data['hotel'] == u'City Hotel'):
                                            if (data.get('arrival_date_month') is None):
                                                return u'Canceled'
                                            if (data['arrival_date_month'] == u'June'):
                                                return u'Canceled'
                                            if (data['arrival_date_month'] != u'June'):
                                                if (data['arrival_date_month'] == u'July'):
                                                    return u'Canceled'
                                                if (data['arrival_date_month'] != u'July'):
                                                    if (data.get('reservation_status_date_month') is None):
                                                        return u'Canceled'
                                                    if (data['reservation_status_date_month'] > 2):
                                                        if (data.get('stays_in_week_nights') is None):
                                                            return u'Canceled'
                                                        if (data['stays_in_week_nights'] > 4):
                                                            return u'Canceled'
                                                        if (data['stays_in_week_nights'] <= 4):
                                                            if (data.get('reservation_status_date_day_of_week') is None):
                                                                return u'Canceled'
                                                            if (data['reservation_status_date_day_of_week'] > 4):
                                                                return u'Canceled'
                                                            if (data['reservation_status_date_day_of_week'] <= 4):
                                                                return u'Canceled'
                                                    if (data['reservation_status_date_month'] <= 2):
                                                        return u'Canceled'
                                        if (data['hotel'] == u'Resort Hotel'):
                                            if (data.get('reservation_status_date_day_of_week') is None):
                                                return u'Canceled'
                                            if (data['reservation_status_date_day_of_week'] > 4):
                                                return u'Canceled'
                                            if (data['reservation_status_date_day_of_week'] <= 4):
                                                if (data.get('is_repeated_guest') is None):
                                                    return u'Canceled'
                                                if (data['is_repeated_guest'] == u'0'):
                                                    return u'Canceled'
                                                if (data['is_repeated_guest'] == u'1'):
                                                    return u'No-Show'
                                if (data['total_of_special_requests'] <= 0):
                                    if (data['lead_time'] > 90):
                                        if (data['market_segment'] == u'Complementary'):
                                            return u'Canceled'
                                        if (data['market_segment'] != u'Complementary'):
                                            if (data.get('reserved_room_type') is None):
                                                return u'Canceled'
                                            if (data['reserved_room_type'] == u'B'):
                                                return u'Canceled'
                                            if (data['reserved_room_type'] != u'B'):
                                                if (data.get('customer_type') is None):
                                                    return u'Canceled'
                                                if (data['customer_type'] == u'Contract'):
                                                    return u'Canceled'
                                                if (data['customer_type'] != u'Contract'):
                                                    if (data.get('arrival_date_year') is None):
                                                        return u'Canceled'
                                                    if (data['arrival_date_year'] == u'2015'):
                                                        return u'Canceled'
                                                    if (data['arrival_date_year'] != u'2015'):
                                                        if (data.get('booking_changes') is None):
                                                            return u'Canceled'
                                                        if (data['booking_changes'] > 1):
                                                            return u'Canceled'
                                                        if (data['booking_changes'] <= 1):
                                                            if (data.get('reservation_status_date_month') is None):
                                                                return u'Canceled'
                                                            if (data['reservation_status_date_month'] > 3):
                                                                if (data.get('reservation_status_date_day_of_week') is None):
                                                                    return u'Canceled'
                                                                if (data['reservation_status_date_day_of_week'] > 1):
                                                                    if (data['reserved_room_type'] == u'A'):
                                                                        return u'Canceled'
                                                                    if (data['reserved_room_type'] != u'A'):
                                                                        return u'Canceled'
                                                                if (data['reservation_status_date_day_of_week'] <= 1):
                                                                    return u'Canceled'
                                                            if (data['reservation_status_date_month'] <= 3):
                                                                return u'Canceled'
                                    if (data['lead_time'] <= 90):
                                        if (data.get('meal') is None):
                                            return u'Canceled'
                                        if (data['meal'] == u'SC'):
                                            return u'Canceled'
                                        if (data['meal'] != u'SC'):
                                            if (data.get('booking_changes') is None):
                                                return u'Canceled'
                                            if (data['booking_changes'] > 0):
                                                return u'Canceled'
                                            if (data['booking_changes'] <= 0):
                                                if (data.get('arrival_date_day_of_month') is None):
                                                    return u'Canceled'
                                                if (data['arrival_date_day_of_month'] == u'28'):
                                                    return u'Canceled'
                                                if (data['arrival_date_day_of_month'] != u'28'):
                                                    if (data.get('reserved_room_type') is None):
                                                        return u'Canceled'
                                                    if (data['reserved_room_type'] == u'B'):
                                                        return u'Canceled'
                                                    if (data['reserved_room_type'] != u'B'):
                                                        if (data['market_segment'] == u'Complementary'):
                                                            return u'Canceled'
                                                        if (data['market_segment'] != u'Complementary'):
                                                            if (data['meal'] == u'BB'):
                                                                if (data.get('stays_in_week_nights') is None):
                                                                    return u'Canceled'
                                                                if (data['stays_in_week_nights'] > 7):
                                                                    return u'Canceled'
                                                                if (data['stays_in_week_nights'] <= 7):
                                                                    if (data.get('reservation_status_date_month') is None):
                                                                        return u'Canceled'
                                                                    if (data['reservation_status_date_month'] > 1):
                                                                        if (data.get('reservation_status_date_day_of_week') is None):
                                                                            return u'Canceled'
                                                                        if (data['reservation_status_date_day_of_week'] > 6):
                                                                            return u'Canceled'
                                                                        if (data['reservation_status_date_day_of_week'] <= 6):
                                                                            if (data.get('adr') is None):
                                                                                return u'Canceled'
                                                                            if (data['adr'] > 7238):
                                                                                return u'Canceled'
                                                                            if (data['adr'] <= 7238):
                                                                                if (data.get('stays_in_weekend_nights') is None):
                                                                                    return u'Canceled'
                                                                                if (data['stays_in_weekend_nights'] > 1):
                                                                                    return u'Canceled'
                                                                                if (data['stays_in_weekend_nights'] <= 1):
                                                                                    if (data['arrival_date_day_of_month'] == u'29'):
                                                                                        return u'Canceled'
                                                                                    if (data['arrival_date_day_of_month'] != u'29'):
                                                                                        if (data['adr'] > 1132):
                                                                                            return u'Canceled'
                                                                                        if (data['adr'] <= 1132):
                                                                                            return u'Canceled'
                                                                    if (data['reservation_status_date_month'] <= 1):
                                                                        return u'Canceled'
                                                            if (data['meal'] != u'BB'):
                                                                return u'Canceled'
                        if (data['previous_cancellations'] != u'0'):
                            return u'Canceled'
                if (data['adults'] <= 1):
                    if (data.get('arrival_date_month') is None):
                        return u'Canceled'
                    if (data['arrival_date_month'] == u'February'):
                        if (data.get('reservation_status_date_day_of_week') is None):
                            return u'Canceled'
                        if (data['reservation_status_date_day_of_week'] > 5):
                            if (data['lead_time'] > 81):
                                return u'No-Show'
                            if (data['lead_time'] <= 81):
                                return u'Canceled'
                        if (data['reservation_status_date_day_of_week'] <= 5):
                            return u'Canceled'
                    if (data['arrival_date_month'] != u'February'):
                        if (data['lead_time'] > 121):
                            return u'Canceled'
                        if (data['lead_time'] <= 121):
                            if (data.get('booking_changes') is None):
                                return u'Canceled'
                            if (data['booking_changes'] > 1):
                                if (data.get('arrival_date_day_of_month') is None):
                                    return u'Canceled'
                                if (data['arrival_date_day_of_month'] == u'23'):
                                    return u'No-Show'
                                if (data['arrival_date_day_of_month'] != u'23'):
                                    if (data.get('market_segment') is None):
                                        return u'Canceled'
                                    if (data['market_segment'] == u'Offline TA/TO'):
                                        return u'No-Show'
                                    if (data['market_segment'] != u'Offline TA/TO'):
                                        return u'Canceled'
                            if (data['booking_changes'] <= 1):
                                if (data.get('stays_in_weekend_nights') is None):
                                    return u'Canceled'
                                if (data['stays_in_weekend_nights'] > 2):
                                    if (data.get('reservation_status_date_month') is None):
                                        return u'Canceled'
                                    if (data['reservation_status_date_month'] > 6):
                                        return u'Canceled'
                                    if (data['reservation_status_date_month'] <= 6):
                                        if (data['arrival_date_month'] == u'July'):
                                            return u'Canceled'
                                        if (data['arrival_date_month'] != u'July'):
                                            return u'No-Show'
                                if (data['stays_in_weekend_nights'] <= 2):
                                    if (data.get('reservation_status_date_day_of_week') is None):
                                        return u'Canceled'
                                    if (data['reservation_status_date_day_of_week'] > 6):
                                        if (data.get('market_segment') is None):
                                            return u'Canceled'
                                        if (data['market_segment'] == u'Online TA'):
                                            return u'Canceled'
                                        if (data['market_segment'] != u'Online TA'):
                                            return u'No-Show'
                                    if (data['reservation_status_date_day_of_week'] <= 6):
                                        if (data.get('adr') is None):
                                            return u'Canceled'
                                        if (data['adr'] > 1349):
                                            return u'Canceled'
                                        if (data['adr'] <= 1349):
                                            if (data.get('assigned_room_type') is None):
                                                return u'Canceled'
                                            if (data['assigned_room_type'] == u'A'):
                                                if (data['reservation_status_date_day_of_week'] > 1):
                                                    return u'Canceled'
                                                if (data['reservation_status_date_day_of_week'] <= 1):
                                                    return u'Canceled'
                                            if (data['assigned_room_type'] != u'A'):
                                                return u'Canceled'
        if (data['lead_time'] <= 13):
            if (data['lead_time'] > 4):
                if (data.get('stays_in_week_nights') is None):
                    return u'Canceled'
                if (data['stays_in_week_nights'] > 4):
                    return u'Canceled'
                if (data['stays_in_week_nights'] <= 4):
                    if (data.get('adults') is None):
                        return u'Canceled'
                    if (data['adults'] > 1):
                        if (data.get('reservation_status_date_day_of_week') is None):
                            return u'Canceled'
                        if (data['reservation_status_date_day_of_week'] > 5):
                            if (data['stays_in_week_nights'] > 1):
                                return u'Canceled'
                            if (data['stays_in_week_nights'] <= 1):
                                if (data.get('arrival_date_day_of_month') is None):
                                    return u'Canceled'
                                if (data['arrival_date_day_of_month'] == u'7'):
                                    return u'No-Show'
                                if (data['arrival_date_day_of_month'] != u'7'):
                                    return u'Canceled'
                        if (data['reservation_status_date_day_of_week'] <= 5):
                            return u'Canceled'
                    if (data['adults'] <= 1):
                        return u'Canceled'
            if (data['lead_time'] <= 4):
                if (data.get('arrival_date_day_of_month') is None):
                    return u'Canceled'
                if (data['arrival_date_day_of_month'] == u'25'):
                    if (data.get('market_segment') is None):
                        return u'No-Show'
                    if (data['market_segment'] == u'Online TA'):
                        return u'No-Show'
                    if (data['market_segment'] != u'Online TA'):
                        return u'Canceled'
                if (data['arrival_date_day_of_month'] != u'25'):
                    if (data.get('reservation_status_date_day_of_week') is None):
                        return u'Canceled'
                    if (data['reservation_status_date_day_of_week'] > 6):
                        if (data.get('stays_in_weekend_nights') is None):
                            return u'Canceled'
                        if (data['stays_in_weekend_nights'] > 1):
                            return u'No-Show'
                        if (data['stays_in_weekend_nights'] <= 1):
                            return u'Canceled'
                    if (data['reservation_status_date_day_of_week'] <= 6):
                        if (data.get('customer_type') is None):
                            return u'Canceled'
                        if (data['customer_type'] == u'Transient-Party'):
                            return u'Canceled'
                        if (data['customer_type'] != u'Transient-Party'):
                            return u'Canceled'
