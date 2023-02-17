var express = require('express');
var consolidate = require('consolidate');

MongoClient = require('mongodb').MongoClient,
Server = require('mongodb').Server;
var app = express ()


app.engine ( 'html', consolidate.hogan );
app.set('views', 'priv'); 


MongoClient.connect('mongodb://localhost:27017', (err, db) => {
	dbo = db.db("rapport");
    if (err) throw err;

    app.get('/display',function(req,res){
      if (req.query.mot_de_passe=="user1"){
        res.render('page1.html',{utilisateur:req.query.utilisateur});
      }else{
        res.render('../static/index.html');
      }
    });
    
    app.get('/lien',function(req,res){
      dbo.collection('incidents').findOne({incident:"Voiture mal stationnée"},(err, doc) => {
          if (err) throw err;
          res.render('page2.html', doc);
      });
      //res.render('page2.html',{Lien_pour_ajouter_un_incident: req.query.q="Lien pour ajouter un incident"});
    });
    
    app.get('/ident',function(req,res){
      res.render('nCompte.html',{Nouveau_Compte: req.query.q="Nouveau_Compte"});
    });

    app.get('/des',function(req,res){
      res.render('page1.html',{description:req.query.description,adresse:req.query.adresse})
    })
    

    app.get('*', (req, res) => {
        res.status(404).send('Page Not Found');
    });
    
    app.listen(8080);
    console.log('Express server started on port 8080');
    
});

app.use(express.static('static'));

