# Book Review Web Application

### Agile Methodology

Elements of Agile and Scrum will be utilised in this project. Since this is an individual project, the Agile role, events and artefacts will be defined as follows:
There will be a Project Owner who will be responsible for planning, creating, managing and deploying the entire software project. The duties of the Scrum Master will not be conducted. The Product Owner’s responsibility of creating and defining the Product Backlog will be conducted by the Project Owner. The Development of the software and the Sprint Backlog will be undertaken by the Project Owner. The Project Owner is also responsible for changing the Sprint Backlog as the Sprint progresses.
The Agile Events will consist of a single Sprint, in which the entire project will be completed. This project will have a Sprint Planning phase, which may involve a simulation with QA as the client. In this meeting the client requirements will be gathered and the user stories will be mutually reviewed and assessed. Artefacts such as the Product Backlog and Sprint Backlog will be created from the client requirements and user stories based on MoSCoW principles. After which the Sprint will be conducted. After the completion and demonstration of the project, a Project Retrospective will be conducted with or without client interaction. This Project Retrospective will detail what could have done better, room for improvements in the software and how the process could be improved. Daily Scrums will not be conducted and there will be no team meetings.

### Program Overview
In the first week Software principles such as Agile and Scrum were introduced. To effectively manage time and create user stories and complete software projects, a technology called Trello was introduced.
In the second week, SQL, Databases, Networks and Network Security were taught. Cloud Computing and its fundamentals were taught, different theoretical benefits of the cloud such as scalability, availability and low latency were introduced. Different cloud models, such as Public, Private, Community and Hybrid Clouds were introduced. Different cloud platforms and their benefits and constraints were discussed. This was followed by exercises involving setting up different virtual machines, how to set firewall configurations and connect a SQL database to a VM.
In the third week python was introduced along with how to push to GitHub and Git. Other aspects of python coding were also introduced such as running tests, setting up virtual environments, using PyMySQL. Python was then used to create a basic banking application. This was followed by an introduced to DevOps, Continuous Integration, Continuous Delivery and Continuous Deployment. A complete Continuous Integration Pipeline was introduced along with the concept of DRY (do not repeat yourself) and the importance of automation. Different features of Git and Jenkins were introduced such as branching, polling and webhooks. This was followed by an introduction to Test Driven Development and basic response codes for the HTTP(S) protocols.
In the fourth week, the concept of using secure socket shells to use other VMs was demonstrated. Libraries such as Flask andSQL Alchemy were introduced, through independent research Bootstrap and WTForms were also discovered. This the fundamentals of how to utilised environment variables was presented. Jinja2 and form validators were taught.
In the fifth week, how to automate the deployment of flask through Systemd and Jenkins was taught. Then unicorn and unit testing in flask was discussed and taught.

### Project Overview
The requirements have been listed below:

| Project requirements |
|  ------ |
| Agile Methodology |
| Trello |
| ERD Diagrams | 
| User Stories | 
| Product Backlog |
| Sprint Backlog  |
| Processes |
| Use Case Scenarios |
| CI Pipeline |
| Risk Assessment |
| Tests Log |


The MoSCoW has been listed below:

|  | MoSCoW |
| ------ | ------ |
| MUST | Have Unit tests for all web pages |
| MUST | Use Test Driven Development methodology |
| MUST | Have automated deployment with a Jenkins CI Server |
| MUST | Have Version Control System (VCS) and a GitHub repository |
| MUST | Be developed on a feature/development branch |
| MUST | Use python |
| MUST | Use Flask |
| MUST | Use a could hosted database and GCP Compute Engine |
| MUST | Have a Trello board(s) with User Stories, User Requirements, Sprint Backlog |
| SHOULD | CSS template |
| SHOULD | Have unique book identifies like ISBN |	
| SHOULD | Basic instance protections |
| SHOULD | Have Login features with hashed/encrypted passwords |
| COULD | Search |
| COULD | Have images |
| WOULD | Defend against security attacks |
### Introduction
The project aims to create a book review application, that allows users to add, delete and update books and reviews to their respective pages.
### Personal Project Goals
This included following the Keep it Simple Stupid (KISS) method. Hence, the entire project was designed to keep the GUI and user experience as simple as possible. It primarily aims to demonstrate that besides CRUD functionality, that all the other CI features had been included.
### Project
Trello was utilised to create a plan. During this phase research was conducted on Agile and Kanban Trello boards and how they have been utilised by different companies such as MicroSoft. After which Trello was used to create User Stories, Sprint Backlog Items and the Backlog items were moved from To Do, Doing to Done as the project progressed. The Trello Board is shown below:

![Trello Planning Board](/Documents/TrelloPlanningBoard.png)

After completing this Initiatives, Themes Epics were researched which resulted in the following epics and user stories:
![First Epic](/Documents/EPICI.jpg)
![Second and Third Epics](/Documents/EPICII&III.jpg)

A user story, its process and use case from the Login Epic has been shown below:
![A User Story and Use Case from the Login Epic](/Documents/LoginEpicUSI.jpg)

A user story, its process and use case from the Reading Reviews epic has been shown below:
![A User Story and Use Case from the second Epic](/Documents/EPICIUSI.jpg)

A user story, its process and use case from the Books epic has been shown below:
![A user story from the third Epic](/Documents/EPICIIUSI.jpg)

An initial Entity Relationship Diagram was created as demonstrated below:

![ERD](/Documents/RealERD.jpg)

The source code was connected to GitHub, which allowed version control and the ability to switch between different versions. It also allowed the project to be pulled onto different machines; and the addition and testing of new features from different machines.

The requirements for the project were traced using Trello. The Trello Sprint Board is shown below:

![Trello Sprint Board](/Documents/TrelloSprintBoard.png)

A SQL database in GCP was spun up along with a VM for Jenkins and another for deployment. An Agile and Test Driven Approach was utilised, hence how to conduct tests was researched. Consideration of HTTP responses and the string responses within the HTML were made. A risk assessment was conducted and is shown below:

![Risk Assessment](/Documents/RiskAssessment.png)

A virtual environment was created, the program was written in a modular form and uploaded to branch on GitHub. This modular form enabled quick troubleshooting throughout the processes. As the software development progressed, the ERD was updated to the following:

![Updated ERD](/Documents/RealERD-2.jpg)

Minor changes were intentionally made to follow the KISS principle (Keep it Simple Stupid). Furthermore, CRUD functionality tests were also taken into account. such as CRUD functionality, login and registration. Front-end development was also considered and was added to the Sprint. During the Sprint phase more more test consideration were taken into account, In total over 30 tests were written and tested:

![Test Log](/Documents/TestLog.png)

This was followed by integration with between the deployment VMs and Jenkins resulting in the following pipeline:

![CI Pipeline](/Documents/CIPipeline.jpg)

There are many improvements that can be made to this application. For example, there could be more stringent policies for who could add a book and less stringent requirements for who can add a reviews. Other features such as search could be added as well. More tests including tests of how the application behaves after a user has logged in could be added. Security could also be enhanced through the addition of dummy data to passwords before hashing and through the randomisation of the dummy data to ensure there are no patterns for the dummy data. The user could also be displayed an image along side each book. Usernames could be attached to each review and improvements to the front end can be made by changing the colours and fonts to fit book genre.

### APPENDIX I

LOGIN EPIC: USER STORY I:

![Login Epic: User Story I](/Documents/LoginEpicUSI.jpg)

LOGIN EPIC: USER STORY II:

![Login Epic: User Story II](/Documents/LoginEpicUSII.jpg)

LOGIN EPIC: USER STORY III:

![Login Epic: User Story III](/Documents/LoginEpicUSIII.jpg)

EPIC I: USER STORY I:

![Epic I: User Story I](/Documents/EPICIUSI.jpg)

EPIC I: USER STORY II:

![Epic I: User Story II](/Documents/EPICIUSII.jpg)

EPIC I: USER STORY III:

![Epic I: User Story III](/Documents/EPICIUSIII.jpg)

EPIC I: USER STORY IV:

![Epic I: User Story IV](/Documents/EPICIUSIV.jpg)

EPIC II: USER STORY I:

![Epic II: User Story I](/Documents/EPICIIUSI.jpg)

EPIC II: USER STORY II:

![Epic II: User Story II](/Documents/EPICIIUSII.jpg)

EPIC III: USER STORY III:

![Epic II: User Story III](/Documents/EPICIIUSIII.jpg)

### APPENDIX II: PRODUCT BACKLOG EXAMPLE

![Product Backlog](/Documents/ProductBacklog.png)


