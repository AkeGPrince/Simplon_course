from data_company import data


"""def price_filter(data):
    for index in range(len(data)):
        if data[index]["price"] > 500:
            print("Company name : [{}], price : [{}]".format(data[index]["company_name"], data[index]["price"]))
    return None


price_filter(data)"""


"""def find_partners(data_copy):
    result = []
    for enterprise in data_copy:
        for company_partner in enterprise["company_partners"]:
            if company_partner not in result:
                result.append(company_partner)
    result.sort()
    return result


print(find_partners(data))"""


"""def average_price(data_param):
    total_action = 0
    counter = 0
    for company in data_param:
        total_action += company["price"]
        counter += 1
    return round(total_action/counter)


print(average_price(data))"""


def company_stock(data_param):
    value_companies, stocks = build_dico(data_param, init=True)
    value_companies, stocks = build_dico(data_param, value_companies=value_companies, stocks=stocks)
    value_companies = {i: value_companies[i] for i in sorted(value_companies, key=value_companies.get, reverse=True)}
    return value_companies


def build_dico(data_param, init=False, stocks={}, value_companies={}):
    for main_company in data_param:
        for partner_company in main_company["company_partners"]:
            if init:
                stocks[partner_company] = 0
                value_companies[partner_company] = 0
            else:
                value_companies[partner_company] += round(main_company["price"]/(2*len(main_company["company_partners"])))
                stocks[partner_company] += main_company["stock"]/(2*len(main_company["company_partners"]))
    return value_companies, stocks


print(company_stock(data))