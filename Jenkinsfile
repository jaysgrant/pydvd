pipeline {

    agent any

    stages {

        stage("Run PyLint") {
            steps {
                script {
                    //sh 'pylint --rcfile=pylint.cfg $(find . -maxdepth 2 -name "*.py" -print) MYMODULE/ > pylint.log || exit 0'
                    sh 'pylint pydvd/*.py --disable=W1202 --output-format=parseable --reports=no module > pylint.log || echo "pylint exited with $?"'
                    sh 'cat pylint.log'
                }
            }
        }
    }

    post {
        always {
            recordIssues enabledForFailure: true, tool: pyLint()
            cleanWs()
        }
    }
}