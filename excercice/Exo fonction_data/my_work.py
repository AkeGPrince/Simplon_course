from data_company import data

def filter_price(data):
    result = ""
    for company in data:
        if company["price"] > 500:
            result += f'Company name : {company["company_name"]}, price : {company["price"]}'
    print(result)


def find_partners(data):
    lst = []
    for entreprise in data:
        for company_partner in entreprise["company_partners"]:
            if company_partner not in lst:
                lst.append(company_partner)
    return sorted(lst)

print(find_partners(data))

def average_price(data):
    counter = 0
    total = 0
    for stock_price in data:
        counter += 1
        total += stock_price["price"]
    return round(total/counter)

print(average_price(data))

def companies_stock(data):
    total = 0
    for stocks in data:
        total += stocks["stock"]
        total = round(total / 2)
    return total

print(companies_stock(data))


### **Exercice 4 :**
#company_partners` représente comment sont divisées les actions
#de chaque entreprise pour les partenaires.

# *exemple*:
# ```
# {
#     'company_name': 'Nunc PC',
#     'price': 102,
#     'company_partners': ['Sibelius', 'Adobe', 'Chami'],
#     'stock': 12
# }
# ```
# Dans ce cas :
# - **Nunc PC** possède 50% des actions (**12** / 2 = **6**)
# - **Sibelius, Adobe et Chami** se divisent équitablement les 50%restant
# (**6** / 3 = 2 actions par entreprise)

# soit :
# - **Nunc PC** : 6 actions
# - **Sibelius** : 2 actions
# - **Adobe** : 2 actions
# - **Chami** : 2 actions



# **Avec ces indications, créez la fonction ``companies_stock``
# qui retourne le nombre d'actions que chaque ``company_partners`` possèdent.**
