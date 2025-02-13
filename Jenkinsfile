pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'World-of-Games'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'DanielRivni'
        APP_PORT = '8777'
        SCORES_FILE = 'Scores.txt'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DanielRivni/wog.git'
            }
        }


        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh """
                    docker run -d -p ${APP_PORT}:${APP_PORT} --name ${DOCKER_IMAGE}-container \
                    --mount type=bind,source=${WORKSPACE}/${SCORES_FILE},target=/app/Scores.txt \
                    ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def testResult = sh(script: "python3 e2e.py http://localhost:${APP_PORT}", returnStatus: true)

                    if (testResult != 0) {
                        error "Tests failed, aborting pipeline."
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh "docker stop ${DOCKER_IMAGE}-container"
                    sh "docker rm ${DOCKER_IMAGE}-container"

                    sh "docker tag ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                    sh "docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        always {
            script {
                sh "docker system prune -f"
            }
        }
    }
}
