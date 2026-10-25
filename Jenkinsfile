pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'anuragrj24/cloud-cicd-app'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        KUBECONFIG_ID = 'k8s-kubeconfig'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest source code from GitHub...'
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                echo 'Setting up environment and running tests...'
                sh '''
                    python3 -m pip install --upgrade pip --break-system-packages || true
                    pip3 install -r requirements.txt --break-system-packages
                    python3 -m unittest test_app.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}:${BUILD_NUMBER} and ${DOCKER_IMAGE}:latest"
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                    docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Push Image') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE}:latest
                        docker logout
                    '''
                }
            }
        }

        stage('Minikube Deployment') {
            steps {
                echo 'Deploying application to Minikube Kubernetes cluster...'
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl set image deployment/flask-app flask-app=${DOCKER_IMAGE}:${BUILD_NUMBER}
                    kubectl rollout status deployment/flask-app --timeout=90s
                '''
            }
        }

        stage('Verification') {
            steps {
                echo 'Verifying Pods, Deployment, and Service status...'
                sh '''
                    kubectl get pods -l app=flask-app
                    kubectl get deployment flask-app
                    kubectl get svc flask-service
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD Pipeline Build #${BUILD_NUMBER} completed successfully!"
        }
        failure {
            echo "CI/CD Pipeline Build #${BUILD_NUMBER} failed. Please inspect build logs."
        }
    }
}
