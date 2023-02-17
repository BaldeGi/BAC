const { ObjectId } = require ( "bson" )

function object(str){
    return ObjectId(str);
};

var express = require('express');
var consolidate = require('consolidate');
var session = require('express-session');

MongoClient = require('mongodb').MongoClient;
Server = require('mongodb').Server;

var app = express ()

var bodyParser = require("body-parser");
var https = require('https');
var fs = require('fs'); 

// ajout

var vm = require('vm');
const { scriptName } = require("yargs");
var fonc = fs.readFileSync('test.js')
vm.runInThisContext(fonc)





app.engine ( 'html', consolidate.hogan );
app.set('views', 'content');

app.use(bodyParser.urlencoded({ extended: true })); 
app.use(session({
  secret: "propre123",
  resave: false,
  saveUninitialized: true,
  cookie: { 
    path: '/', 
    httpOnly: true, 
    maxAge: 3600000
  }
}));





const date=new Date();
const mois=date.getMonth()+1;
const d=date.getDate()+'/'+mois+'/'+date.getFullYear();


var acheter=[];
var vendu=[];



MongoClient.connect("mongodb://localhost:27017",function(err,db){
    dbm=db.db("database");
    if(err) throw err;
    //page d'identification
    app.post("/display",(req,res)=>{
        dbm.collection("utilisateurs").findOne({"utilisateur":req.body.utilisateur,"mot_de_passe":req.body.mot_de_passe},(err,cle)=>{
            if(err) throw err;
            else if(cle==null){
                res.render("identification.html",{"erreur":erreur});
            }
            else{
                req.session.utilisateur=req.body.utilisateur;
                dbm.collection("depot").find({}).toArray((err,doc)=>{
                    if(err) throw err;
                    res.render("page_principale.html",{livre: doc,utilisateur:req.session.utilisateur,date:d})
                });
            }
        })
    });

    //identification
    app.get("/connect",(req,res)=>{
        res.render("identification.html")
    });

    

    // Vers la page principale
    app.get("/acceuil",(req,res)=>{
        dbm.collection("depot").find({}).toArray((err,doc)=>{
            if(err) throw err;
            else if (req.session.utilisateur){
                res.render("page_principale.html",{livre:doc,utilisateur:req.session.utilisateur});
            }
            else res.render("index.html",{livre:doc})
        });
    });

    // Le profil
    app.get("/profile",(req,res)=>{
        dbm.collection("utilisateurs").find({"utilisateur":req.session.utilisateur}).toArray((err,doc)=>{
            if(err) throw err;
            res.render("profile.html",{profile:doc,utilisateur:req.session.utilisateur});
        })
    });


    // Livres achetes

    // Livres Vendus
    app.get("/vendu",(req,res)=>{
        dbm.collection("depot").find({utilisateur:req.session.utilisateur}).toArray((err,doc)=>{
            if(err) throw err;
            res.render("vendu.html",{livre: doc,utilisateur:req.session.utilisateur})
        });
    });

     //pour aller a la page de selectionne
     app.get("/achete",(req,res)=>{
        dbm.collection("depot").find({}).toArray((err,doc)=>{
            if(err) throw err;
            res.render("achete.html",{livre: doc,utilisateur:req.session.utilisateur})
        })
    });

    // Deconnection
    app.get('/deconnect',function(req,res){
        req.session.destroy();
        res.redirect('/');

    });

    // accès au nouveau Compte
    app.get("/ident",(req,res)=>{
        res.render("creation_compte.html")
    });
    // Creer un nouveau compte

    app.post("/enregistrement",(req,res)=>{
        if(req.body.utilisateur=="" || req.body.mot_de_passe=="" || req.body.nom=="" || req.body.prenom=="" || req.body.mail==""){
            res.render("creation_compte.html")
        }else{
            dbm.collection("utilisateurs").findOne({"utilisateur":req.body.utilisateur},(err,doc)=>{
                if(err) throw err;
                else if(doc!=null){
                    res.render("creation_compte.html")
                }else{
                    dbm.collection("utilisateurs").insertOne({"utilisateur":req.body.utilisateur,"mot_de_passe":req.body.mot_de_passe,"nom":req.body.nom,"prenom":req.body.prenom,"mail":req.body.mail},(err,doc)=>{
                        if(err) throw err;
                        req.session.utilisateur=req.body.utilisateur;
                        dbm.collection("depot").find({}).toArray((err,doc)=>{
                            if(err) throw err;
                            res.render("page_principale.html",{livre: doc,utilisateur:req.session.utilisateur})
                        })
                    })
                }
            });
        };
    });


    // bouton acheter un livre
     app.get("/achat",(req,res)=>{

        dbm.collection("depot").find({}).toArray((err,doc)=>{
            if(err) throw err;
            res.render("select.html",{livre: doc,utilisateur:req.session.utilisateur,date:d})
            vendu=[];
            acheter=[];

        })

    });

    // dans la page vente

    app.get("/confirmer",(req,res)=>{
        res.render("carte_banque.html",{utilisateur:req.session.utilisateur})
    });


    // bouton Vendre

    app.get("/vente",(req,res)=>{
        res.render("depot.html",{utilisateur:req.session.utilisateur,date:d})
    });


    // Deposer un livre
    app.post("/depot",(req,res)=>{
        dbm.collection("depot").insertOne({"utilisateur":req.session.utilisateur,"titre":req.body.titre,"auteur":req.body.auteur,"edition":req.body.edition,"prix":req.body.prix,"date":d},(err,doc)=>{
            if(err) throw err;
            dbm.collection("depot").find({}).toArray((err,doc)=>{
                if(err) throw err;
                res.render("page_principale.html",{livre: doc,utilisateur:req.session.utilisateur})
            })
        });
    });


    // Select 

    app.post("/select",(req,res)=>{
        if(req.body.ecrie){
           var texte= lecture(req.body.ecrie);
            var l=[];
            texte.forEach(element=>{
                l.push(object(element))
            })
            dbm.collection("depot").find({"_id":{"$in":l}}).toArray((err,doc)=>{
                m_total=prix_total(doc);
                var variable =doc;
                doc.forEach(element=>{
                    vendu.push(element);
                });
                variable.forEach(i=>{
                    acheter.push(i);
                })
                if(err) throw err;
                res.render("vente.html",{livre: doc,montant:m_total,utilisateur:req.session.utilisateur,date:d});
            });
        }else{
            res.redirect("/achat");
        };
    });


    // La recherche
    app.post("/search",(req,res)=>{
        let mot = req.body.search;  
        dbm.collection("depot").find(
            { $search: mot },
         ).toArray((err,doc)=>{
           
            res.render("page_principale.html",{livre:doc,utilisateur:req.session.utilisateur})
         });
    })


    app.get("/oublier",(req,res)=>{
        res.render("nouveau_mot_passe.html")
    })

    app.post("/nouveau_pswd",(req,res)=>{
        dbm.collection("utilisateurs").findOne({"utilisateur":req.body.utilisateur},(err,doc)=>{
            if (err) throw err
            else if(doc==null&&req.body.mot_de_passe!=req.body.conf_mot_de_passe){
                res.render("nouveau_mot_passe.html",{"error":error()[0]})
            }

            else if(doc==null){
                res.render("nouveau_mot_passe.html",{"error":error()[1]})
            }
            else{
                if(req.body.mot_de_passe==req.body.conf_mot_de_passe){
                    req.session.utilisateur=req.body.utilisateur
                    dbm.collection("utilisateurs").updateOne({"utilisateur":req.body.utilisateur},{$set:{mot_de_passe:req.body.mot_de_passe}},(err,doc)=>{
                        if (err) throw err
                        dbm.collection("depot").find({}).toArray((err,doc)=>{
                            if(err) throw err;
                            res.render("page_principale.html",{livre: doc,utilisateur:req.session.utilisateur,date:d})
                           
                        })
                    });
                }
                else{
                    res.render("nouveau_mot_passe.html",{"error":error()[2]})
                }
            }
        })
    })
  

    //affiche la page index
    app.get("/",(req,res)=>{
        req.session.utilisateur=null;
        dbm.collection("depot").find({}).toArray((err,doc)=>{
            if(err) throw err;
            res.render("index.html",{livre: doc,date:d})
        })
    })
});

app.use(express.static('static'));
app.listen(10);