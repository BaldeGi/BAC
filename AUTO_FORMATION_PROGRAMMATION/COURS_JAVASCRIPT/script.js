/* LONGUEUR D'UNE CHAINE */
var name = "John";
var nameLength = name.length;
console.log(nameLength);

console.log("----------------")

/* CONVERTIR EN INT */
var nombre  = 12.5;
var entier = parseInt(nombre);
console.log(entier);

console.log("----------------")

/* CONVERTIR EN FLOAT */
var nombre  = "12.5";
var entier = parseFloat(nombre);
console.log(entier);

console.log("----------------")

/* LA POSITION D'UNE STRING */
var myString = "Hello John";
var position = myString.indexOf("John");
console.log(position)

console.log("----------------")

/* REMPLACER UNE STRING PAR UNE AUTRE */
var myNewString = myString.replace("John","Kim");
console.log(myNewString);

console.log("----------------")

/* ADDITIONNER DEUX STRINGS */
var string1 = "Hello ";
var string2 = "Johny";
var myNewString = string1 + string2;
console.log(myNewString);

console.log("----------------")

/* COMPARAISONS */
var x  = "5";
console.log(x===5);  // False
console.log(x==5); // True

console.log("----------------")

/* LE SWITCH */
var favoriteColor = "blue";
switch(favoriteColor)
{
    case "blue":
        console.log("Yess Bleue")
        break;
    case "red":
        console.log("Yess Red")
        break;
    default:
        console.log("Aucun des deux")
}

console.log("----------------")

/* LES BOUCLES */
var number  = 0;
while(number<3)
{
    console.log(number);
    number++;
}

console.log("----------------")

// le do fait d'abord ce qui est dans le do avant de verifier le while
var numbers  = 3;
do
{
    console.log(numbers);
    numbers++;
}
while(numbers<3)

console.log("----------------")

for(var number = 0; number<5; number++)
{
    console.log(number);
}

console.log("----------------")

/* LES FONCTIONS */
function multiply(number1,number2)
{
    return number1*number2;
}

var a = 5;
var b = 6;
var result = multiply(a,b);
console.log(result);

console.log("----------------")

/* LES TABLEAUX */
var fruits = ["Pomme","Banane","Orange"];
console.log(fruits.length);
console.log(fruits[1]);
console.log(fruits);

for(i=0;i<fruits.length;i++)
{
    console.log(fruits[i])
}

console.log("----------------")

// Ajouter un element
fruits.push("Kiwi");
console.log("Ajouter :",fruits);

// Supprimer le dernier element
fruits.pop()
console.log("Kiwi supprimer :",fruits);

// L'indice
console.log("Indice de Pomme :",fruits.indexOf("Pomme"));

// Le slice
var agrumes = fruits.slice(0,2);
console.log(agrumes);

console.log("----------------")

/* LES OBJETS */
var dog = 
{
    name : "Choupette",
    color: "Blanc",
    age : 4,
};

console.log(dog.name);
console.log(dog["age"]);

for(var property in dog)
{
    console.log(property);
}
 console.log("\n")

 for(var property in dog)
{
    console.log(dog[property]);
}
console.log("\n")

// Autre façon de creer un objet
var dog = new Object();
dog.name = "Choupette";
dog.color = "Noir";
dog.age = 5;
console.log(dog)

console.log("\n")

// Des methodes
dog.aboie = function(){console.log("Wouaf Wouaf")};
dog.aboie();

function numberAboie(number)
{
    while(number>0)
    {
        console.log(number.toString() + " Wouaf");
        number--;
    }
}
numberAboie(5)

console.log("\n")


/* LES FONCTIONS CONSTRUCTEURS */
function Dog(name,color,age)
{
    this.name = name;
    this.color = color;
    this.age = age;
    this.aboie = function() // Methode
    {
        console.log("WOUAF", this.name);
    }
}

var petitCaniche = new Dog("Choupette","White",4);
var grosPitbull = new Dog("Rex", "Black",2);
console.log(petitCaniche);
console.log(grosPitbull);
petitCaniche.aboie();















