import datetime
import random


class QueryGenerator:
    @staticmethod
    def generate_query(query_template, query_number, should_validate, scale_factor, stream_id):
        random.seed()
        return query_template.format(
            **QueryGenerator.query_arguments[query_number](should_validate, scale_factor, stream_id))

    type_syllables_1 = ['STANDARD', 'SMALL', 'MEDIUM', 'LARGE', 'ECONOMY', 'PROMO']
    type_syllables_2 = ['ANODIZED', 'BURNISHED', 'PLATED', 'POLISHED', 'BRUSHED']
    type_syllables_3 = ['TIN', 'NICKEL', 'BRASS', 'STEEL', 'COPPER']
    regions = [(0, 'AFRICA'), (1, 'AMERICA'), (2, 'ASIA'), (3, 'EUROPE'), (4, 'MIDDLE EAST')]
    segments = ['AUTOMOBILE', 'BUILDING', 'FURNITURE', 'MACHINERY', 'HOUSEHOLD']
    dates_03 = [datetime.date(1995, 3, 31) - datetime.timedelta(days=x) for x in range(31)]
    dates_04 = [datetime.date(1993 + month // 12, 1 + month % 12, 1) for month in range(58)]
    dates_05 = [datetime.date(1993 + year, 1, 1) for year in range(5)]
    dates_10 = [datetime.date(1993 + month // 12, 1 + month % 12, 1) for month in range(25)][1:]
    dates_14 = [datetime.date(1993 + month // 12, 1 + month % 12, 1) for month in range(60)]
    nations = [(0, 'ALGERIA', 0), (1, 'ARGENTINA', 1), (2, 'BRAZIL', 1), (3, 'CANADA', 1), (4, 'EGYPT', 4),
               (5, 'ETHIOPIA', 0), (6, 'FRANCE', 3), (7, 'GERMANY', 3), (8, 'INDIA', 2), (9, 'INDONESIA', 2),
               (10, 'IRAN', 4), (11, 'IRAQ', 4), (12, 'JAPAN', 2), (13, 'JORDAN', 4), (14, 'KENYA', 0),
               (15, 'MOROCCO', 0), (16, 'MOZAMBIQUE', 0), (17, 'PERU', 1), (18, 'CHINA', 2), (19, 'ROMANIA', 3),
               (20, 'SAUDI ARABIA', 4), (21, 'VIETNAM', 2), (22, 'RUSSIA', 3), (23, 'UNITED KINGDOM', 3),
               (24, 'UNITED STATES', 1)]
    colors = ['almond', 'antique', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanched', 'blue', 'blush',
              'brown', 'burlywood', 'burnished', 'chartreuse', 'chiffon', 'chocolate', 'coral', 'cornflower',
              'cornsilk', 'cream', 'cyan', 'dark', 'deep', 'dim', 'dodger', 'drab', 'firebrick', 'floral',
              'forest',
              'frosted', 'gainsboro', 'ghost', 'goldenrod', 'green', 'grey', 'honeydew', 'hot', 'indian', 'ivory',
              'khaki', 'lace', 'lavender', 'lawn', 'lemon', 'light', 'lime', 'linen', 'magenta', 'maroon',
              'medium',
              'metallic', 'midnight', 'mint', 'misty', 'moccasin', 'navajo', 'navy', 'olive', 'orange', 'orchid',
              'pale', 'papaya', 'peach', 'peru', 'pink', 'plum', 'powder', 'puff', 'purple', 'red', 'rose', 'rosy',
              'royal', 'saddle', 'salmon', 'sandy', 'seashell', 'sienna', 'sky', 'slate', 'smoke', 'snow',
              'spring',
              'steel', 'tan', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'yellow']
    modes = ['REG AIR', 'AIR', 'RAIL', 'SHIP', 'TRUCK', 'MAIL', 'FOB']
    container_syllables_1 = ['SM', 'LG', 'MED', 'JUMBO', 'WRAP']
    container_syllables_2 = ['CASE', 'BOX', 'BAG', 'JAR', 'PKG', 'PACK', 'CAN', 'DRUM']

    @staticmethod
    def helper_7(should_validate):
        nations = random.sample(QueryGenerator.nations, 2)
        return {'NATION1': 'FRANCE' if should_validate else nations[0][1],
                'NATION2': 'GERMANY' if should_validate else nations[1][1]}

    @staticmethod
    def helper_8(should_validate):
        nation = (2, 'BRAZIL', 1) if should_validate else random.choice(QueryGenerator.nations)
        n_region_key = nation[2]
        return {'NATION': nation[1],
                'REGION': QueryGenerator.regions[n_region_key][1],
                'TYPE': 'ECONOMY ANODIZED STEEL' if should_validate else random.choice(QueryGenerator.type_syllables_3)}

    @staticmethod
    def helper_12(should_validate):
        selected_modes = ['MAIL', 'SHIP'] if should_validate else random.sample(QueryGenerator.modes, 2)
        return {'SHIPMODE1': selected_modes[0],
                'SHIPMODE2': selected_modes[1],
                'DATE': datetime.date(1994, 1, 1) if should_validate else random.choice(QueryGenerator.dates_05)}

    @staticmethod
    def helper15(should_validate, stream_id):
        return {'DATE': datetime.date(1996, 1, 1) if should_validate else random.choice(QueryGenerator.dates_04),
                'STREAM_ID': stream_id if type(stream_id) == int else random.randint(1, 99999)}

    @staticmethod
    def helper_22(should_validate):
        nations = random.sample(QueryGenerator.nations, 7)
        return {'I1': 13 if should_validate else nations[0][0] + 10,
                'I2': 31 if should_validate else nations[1][0] + 10,
                'I3': 23 if should_validate else nations[2][0] + 10,
                'I4': 29 if should_validate else nations[3][0] + 10,
                'I5': 30 if should_validate else nations[4][0] + 10,
                'I6': 18 if should_validate else nations[5][0] + 10,
                'I7': 17 if should_validate else nations[6][0] + 10}

    query_arguments = {
        1: lambda should_validate, _, stream_id: {'DELTA': 90 if should_validate else random.randint(60, 120)},
        2: lambda should_validate, _, stream_id: {'SIZE': 15 if should_validate else random.randint(1, 50),
                                       'TYPE': 'BRASS' if should_validate else random.choice(
                                           QueryGenerator.type_syllables_3),
                                       'REGION': 'EUROPE' if should_validate else
                                       random.choice(QueryGenerator.regions)[1]},
        3: lambda should_validate, _, stream_id: {
            'SEGMENT': 'BUILDING' if should_validate else random.choice(QueryGenerator.segments),
            'DATE': datetime.date(1995, 3, 15) if should_validate else random.choice(QueryGenerator.dates_03)},
        4: lambda should_validate, _, stream_id: {
            'DATE': datetime.date(1993, 7, 1) if should_validate else random.choice(QueryGenerator.dates_04)},
        5: lambda should_validate, _, stream_id: {
            'REGION': 'ASIA' if should_validate else random.choice(QueryGenerator.regions)[1],
            'DATE': datetime.date(1994, 1, 1) if should_validate else random.choice(QueryGenerator.dates_05)},
        6: lambda should_validate, _, stream_id: {
            'DATE': datetime.date(1994, 1, 1) if should_validate else random.choice(QueryGenerator.dates_05),
            'DISCOUNT': 0.06 if should_validate else random.uniform(0.02, 0.09),
            'QUANTITY': 24 if should_validate else random.randint(24, 25)},
        7: lambda should_validate, _, stream_id: QueryGenerator.helper_7(should_validate),
        8: lambda should_validate, _, stream_id: QueryGenerator.helper_8(should_validate),
        9: lambda should_validate, _, stream_id: {
            'COLOR': 'green' if should_validate else random.choice(QueryGenerator.colors)},
        10: lambda should_validate, _, stream_id: {
            'DATE': datetime.date(1993, 10, 1) if should_validate else random.choice(QueryGenerator.dates_10)},
        11: lambda should_validate, scale_factor, stream_id: {
            'NATION': 'GERMANY' if should_validate else random.choice(QueryGenerator.nations)[1],
            'FRACTION': 0.0001 if should_validate else 0.0001 / scale_factor},
        12: lambda should_validate, _, stream_id: QueryGenerator.helper_12(should_validate),
        13: lambda should_validate, _, stream_id: {
            'WORD1': 'special' if should_validate else random.choice(['special', 'pending', 'unusual', 'express']),
            'WORD2': 'requests' if should_validate else random.choice(['packages', 'requests', 'accounts',
                                                                       'deposits'])},
        14: lambda should_validate, _, stream_id: {
            'DATE': datetime.date(1995, 9, 1) if should_validate else random.choice(QueryGenerator.dates_14)},
        15: lambda should_validate, _, stream_id: QueryGenerator.helper15(should_validate, stream_id),
        16: lambda should_validate, _, stream_id: {
            'BRAND': 'Brand#45' if should_validate else 'Brand#{0}{1}'.format(random.randint(1, 5),
                                                                              random.randint(1, 5)),
            'TYPE': 'MEDIUM POLISHED' if should_validate else '{0} {1}'.format(
                random.choice(QueryGenerator.type_syllables_1),
                random.choice(
                    QueryGenerator.type_syllables_2)),
            'SIZE1': 49 if should_validate else random.randint(1, 50),
            'SIZE2': 14 if should_validate else random.randint(1, 50),
            'SIZE3': 23 if should_validate else random.randint(1, 50),
            'SIZE4': 45 if should_validate else random.randint(1, 50),
            'SIZE5': 19 if should_validate else random.randint(1, 50),
            'SIZE6': 3 if should_validate else random.randint(1, 50),
            'SIZE7': 36 if should_validate else random.randint(1, 50),
            'SIZE8': 9 if should_validate else random.randint(1, 50)},
        17: lambda should_validate, _, stream_id: {
            'BRAND': 'Brand#23' if should_validate else 'Brand#{0}{1}'.format(random.randint(1, 5),
                                                                              random.randint(1, 5)),
            'CONTAINER': 'MED BOX' if should_validate else '{0} {1}'.format(
                random.choice(QueryGenerator.container_syllables_1),
                random.choice(QueryGenerator.container_syllables_2))},
        18: lambda should_validate, _, stream_id: {'QUANTITY': 300 if should_validate else random.randint(312, 315)},
        19: lambda should_validate, _, stream_id: {'QUANTITY1': 1 if should_validate else random.randint(1, 10),
                                        'QUANTITY2': 10 if should_validate else random.randint(10, 20),
                                        'QUANTITY3': 20 if should_validate else random.randint(20, 30),
                                        'BRAND1': 'Brand#12' if should_validate else 'Brand#{0}{1}'.format(
                                            random.randint(1, 5),
                                            random.randint(1, 5)),
                                        'BRAND2': 'Brand#23' if should_validate else 'Brand#{0}{1}'.format(
                                            random.randint(1, 5),
                                            random.randint(1, 5)),
                                        'BRAND3': 'Brand#34' if should_validate else 'Brand#{0}{1}'.format(
                                            random.randint(1, 5),
                                            random.randint(1, 5))},
        20: lambda should_validate, _, stream_id: {
            'COLOR': 'forest' if should_validate else random.choice(QueryGenerator.colors),
            'DATE': datetime.date(1994, 1, 1) if should_validate else random.choice(QueryGenerator.dates_05),
            'NATION': 'CANADA' if should_validate else random.choice(QueryGenerator.nations)[1]},
        21: lambda should_validate, _, stream_id: {
            'NATION': 'SAUDI ARABIA' if should_validate else random.choice(QueryGenerator.nations)[1]},
        22: lambda should_validate, _, stream_id: QueryGenerator.helper_22(should_validate)}
