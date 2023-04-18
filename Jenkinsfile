pipeline {
    agent  any

    stages {
      stage('Clone repository') {
        steps {
             script{
              checkout scm
             }
          }
      }
      
      stage ('Build') {
        steps {
            script {
            app = docker.build("flaskapp")
          } 
        }
      }
     
      stage ('Deploy') {
        steps {
          script {
               docker.withRegistry('026720147938.dkr.ecr.us-east-1.amazonaws.com', 'aws-creds') {
                   app.push("${env.BUILD_NUMBER}")
                   app.push("latest")
                   }
               }
          }
        }

   }   
}
