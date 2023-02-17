function lecture(texte){
    var string=texte;
    var str =string.split(","); 
    return str;  
} 

function prix_total(l){// utilise une liste de document pour calculer le prix des elements selectionner.
    var montant=0;
    l.forEach(element => {
        montant+=parseFloat(element.prix);
    });
    return montant;
}


function erreur(){
    return "Le nom d'utilisateur et ou le mot de passe est incorrecte."
}


function error(){
    return ["Le nom d'utilisateur n'est pas valide et les mots de passe sont differents","Le nom d'utilisateur est incorrecte , veillez renseigner un nom d'utilisateur valide.",
    "Les mots de passe sont differents."]
}
