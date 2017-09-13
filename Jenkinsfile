//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'ls -lah'
            }
        }

	stage('Deploy') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS' 
              }
            }
            steps {
                //sh 'make publish'
		echo "RESULT: ${currentBuild.result}"
            }
        }
    }

    post {
        always {
		echo "ENV : ${env}"
		echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
        }
        failure {
            //mail to: sunny.k@shieldsquare.com, subject: 'The Pipeline failed :('
          	step([$class: 'Mailer',
            	notifyEveryUnstableBuild: true,
            	recipients: "sunny.k@shieldsquare.com",
            	sendToIndividuals: true])
        }
    }
}
