pipeline {
    agent {
        label 'ubuntu_node'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/vlad9976/WorldOfGames.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t world_of_games_image .'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker run -d -p 8777:5000 --name world_of_games_container world_of_games_image:latest'
                    sh 'docker ps'
                }
            }
        }

        stage('Test') {
            steps {
                sh 'python3 tests/e2e.py'
            }
        }
    }

    post {
        always {
            script {
                sh 'docker stop world_of_games_container'
                sh 'docker rm world_of_games_container'
            }
        }
    }
}