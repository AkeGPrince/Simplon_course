# ## Votre restaurant propose désormais des pizzas à la carte
# ## Pour simplifier et optimiser le traitement des données relative à ce chargement
# ## Nous décidons d'utiliser la programmation orienté-objet :

# """Créer une classe pizza sans argument, et instancier cette classe en créant une première pizza"""

# # Nous souhaitons ajouter 3 pizzas à la carte du restaurant :
# # Une Reine, composée de tomate, de fromage de jambon, de champignon
# # Une Nordique, composée de creme fraiche, de fromage et de saumon
# # et Une Napolitaine composée de tomate, de fromage, d'anchois et d'olive
# """2) Ajouter à notre classe pizza 2 variable d'instance : name(string) et ingredient(liste) et crée les 3 pizza de la carte"""

# # Les pizzas sont toute cuite au "feu de bois"
# """3) Ajouter un une variable de classe "cuisson" à la classe pizza"""

# #On souhaite affiché sur l'écran du restaurant le nom de la pizza, ces ingrédients sa technique de cuisson:
# """4) Créer une fonction "display_pizza" qui permet d'afficher le nom, les ingrédients
# et le mode de cuisson puis utilisé cette méthode sur les 3 pizzas."""

# #La pizzeria veut étendre sa carte, et rajouter la Calzone au menu. Contrairement à la pizza, la calzone peut prendre des formes différentes, et la pizzeria veut proposer cette option à ces clients.
# """5) Créer une Class fille de la Class parent 'Pizza' nommée 'Calzone'. Rajouter un argument 'forme' à cette nouvelle Class.


class Pizza:


    def __init__(self, name, ingredients = []):
        self.name = name
        self.ingredients = ingredients









reine = Pizza("Reine", ["Tomate", "Jambon", "Fromage", "Champignons"])

print(reine.ingredients.name)
