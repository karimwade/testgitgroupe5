def show(nom,prenom,age):
    if age==0:
        print("veuillez saisir correctement l'age")
    else: 
        print("bonjour "+prenom," "+nom, "vous avez ",age, "ans")

nom= input("saisi le nom : ")
prenom = input("Veuiller saisir votre prenom : ")
age= input("saisi l'age : ")


show(nom,prenom,age)