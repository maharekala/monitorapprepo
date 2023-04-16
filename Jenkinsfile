pipeline {
   agent any

    stages {
      
       stage("build"){
         step {
           pip3 install --no-cache-dir -r requirements.txt
           FLASK_RUN_HOST=0.0.0.0:5000
           pyhton3 app.py
            
          }
       }


    }
 }
