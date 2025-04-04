docker build -t myjenkins .

docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home --name jenkins myjenkins

docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home --name jenkins myjenkins

Open your browser and navigate to: http://localhost:8080

docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
