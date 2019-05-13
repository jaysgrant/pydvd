pipeline {

    agent any

    stages {

        stage("Run PyLint") {
            steps {
                script {
                    sh 'cd pydvd'
                    sh 'pylint *.py'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}