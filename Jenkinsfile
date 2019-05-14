pipeline {

    agent any

    stages {

        stage("Run PyLint") {
            steps {
                script {
                    sh 'pylint --rcfile=pylint.cfg $(find . -maxdepth 2 -name "*.py" -print) MYMODULE/ > pylint.log || exit 0'
                }
            }
        }
    }

    post {
        always {
            pylint testResults: 'pylint.log'
            recordIssues enabledForFailure: true, tools: [pylint()]
            cleanWs()
        }
    }
}