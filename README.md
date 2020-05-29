**P.S. STILL TO BE UPDATED!**
--

Home automation testing project based on the Weave Socks project - https://microservices-demo.github.io/. Both API and UI domains are included.

**Brief summary**:

1. Get testable projects (like microservices-demo).
2. Create GitHub account to keep the project up.
3. Create automation framework.
4. Create Amazon Web Service (Google Cloud, DigitalOcean etc.) for the project.
5. Create AWS for Jenkins via Docker.
6. Create AWS for Jenkins' slave(s)/node(s).
7. Create pipeline.
8. Add Selenoid.

**General CI scheme**: 
* merge branch to master branch in Github --> 
* that triggers Jenkins on AWS --> 
* master Jenkins triggers its slaves --> 
* Selenoid?

Below is an almost step-by-step process that I followed to make this work:)
--
**1. GET THE PROJECT:**

* Clone or download it from - https://microservices-demo.github.io/.

* Upload it to the Amazon Web Services: 

  _Comments: necessary, should you be willing to work with it along with Selenoid, Jenkins etc._

  * Register on the Amazon Web Service - https://aws.amazon.com/.
  * Create EC2 (Elastic Computer Cloud), which provides scalable computing capacity in the Amazon Web Services (AWS) cloud.
  * Publish project to the EC2 - https://qiita.com/phanithken/items/34d1a81395f8c0b78132 (regarding EC2) and https://microservices-demo.github.io/deployment/docker-compose.html (regarding the way to run project in Docker. Yeap, you have to install Docker as well).

* Install Jenkins via Docker on the AWS:
  * Install Jenkins within Docker - https://jenkins.io/doc/book/installing/#setup-wizard
  * Run Jenkins in Docker - https://hub.docker.com/_/jenkins/
  * Make your first Job, which is hooked to the Github repository and is triggered by every commit - https://www.youtube.com/watch?v=Z3S2gMBUkBo
* Create slave(s)/node(s) - 



**POSSIBLE ISSUES:**
--
* Currently known issues with "microservices-demo" project:
  * by default has total 4 user addresses being added;
  * doesn't add new addresses;
  * by default has total 4 user cards being added;
  * doesn't add new cards; 

* Possible issues with running Jenkins in browser

  * Run Jenkins within Docker in a correct manner - sudo docker run -p 8080:8080 -p 50000:50000 -v /your/home:/var/jenkins_home jenkins - https://hub.docker.com/_/jenkins/
  * Closed port 8080 - https://stackoverflow.com/questions/26338301/ec2-how-to-add-port-8080-in-security-group
  * Sometime firewalls should be disabled.

* Other possible issues

   * Terminal freezes after short inactivity while SSH connection - sudo vi /etc/ssh/sshd_config - https://unix.stackexchange.com/questions/200239/how-can-i-keep-my-ssh-sessions-from-freezing or https://superuser.com/questions/98562/way-to-avoid-ssh-connection-timeout-freezing-of-gnome-terminal
