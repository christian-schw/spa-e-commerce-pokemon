<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
# E-Commerce Shop Pokemon - Catch 'em All!

<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li>
      <a href="#general">General</a>
      <ul>
        <li><a href="#general-information-about-the-project">General Information about the Project</a></li>
        <li><a href="#important-notes">Important Notes</a></li>
        <li><a href="#roadmap">Roadmap</a></li>
        <li><a href="#project-folder-layout">Project Folder Layout</a></li>
        <li><a href="#general---tech-stack">General - Tech Stack</a></li>
        <li><a href="#general---reasons-for-the-tech-stack-selection">General - Reasons for the Tech Stack Selection</a></li>
        <li><a href="#complete-overview-of-the-system">Complete Overview of the System</a></li>
        <li><a href="#contributors">Contributors</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#acknowledgements">Acknowledgements</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </li>
    <li>
      <a href="#frontend">Frontend</a>
      <ul>
        <li><a href="#frontend---tech-stack">Frontend - Tech Stack</a>
        <li><a href="#frontend---reasons-for-the-tech-stack-selection">Frontend - Reasons for the Tech Stack Selection</a></li>
        <li><a href="#frontend---development-process">Frontend - Development Process</a></li>
      </ul>
    </li>
    <li>
      <a href="#backend">Backend</a>
      <ul>
        <li><a href="#backend---tech-stack">Backend - Tech Stack</a>
        <li><a href="#backend---reasons-for-the-tech-stack-selection">Backend - Reasons for the Tech Stack Selection</a></li>
        <li><a href="#backend---development-process">Backend - Development Process</a></li>
      </ul>
    </li>
  </ol>
</details>
<br>


## Introduction
E-Commerce Shop where you can browse, buy and collect Pokemon.<br>
The shop is built as a single page application (SPA) to ensure a better user experience!<br>
<br>
Teaser pictures of the initial design mockups during the planning phase for a first impression of the project:<br>

![teaser1-picture-description-stats](https://github.com/user-attachments/assets/8b405cd1-f58a-4137-8f58-5f288e1e44ef)

![teaser2-facts](https://github.com/user-attachments/assets/fcaf1bab-6073-47e9-85d2-3bf911d52574)

![teaser3-evolution](https://github.com/user-attachments/assets/90dd1c76-bd3f-4404-8e10-d9dd1e7abddf)

![teaser4-tablet-view](https://github.com/user-attachments/assets/34698781-0235-4ab9-9f9b-e2ce4c0d366c)

![teaser5-mobile-view](https://github.com/user-attachments/assets/5e347520-f5d5-4c5a-afa5-75dcd2ce5835)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


## General
### General Information about the Project
- Client: Myself
- Project Goal: Improving my software development skills in both frontend and backend as well as Cloud and DevOps. At the same time creating a fun project for a bit of nostalgia (childhood) ;-)
- Number of Project Participants: 2
- Time Period: October, 2024 - Present
- Industry / Area: E-Commerce, Pokemon
- Role: Developer
- Languages: German, English
- Result: TODO
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Important Notes
The project uses the [PokéAPI](https://pokeapi.co/) to obtain the Pokémon data.<br>
Although the project is an e-commerce shop, it does <ins>not</ins> make any commercial profit.<br>
Any commercial transaction is purely exemplary and involves imaginary currency.
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Roadmap
- [ ] Analyze current status
- [ ] Document progress
- [ ] Prepare for the next implementation steps
- [ ] Backend
    - [ ] Setting up development environment
    - [ ] Setting up CI/CD pipeline
    - [ ] TODO: Insert further steps
- [ ] Frontend
    - [ ] Setting up development environment
    - [ ] Setting up CI/CD pipeline
    - [ ] TODO: Insert further steps

As I have suddenly stopped working on the project for a while for certain reasons and unfortunately have not documented the progress in detail, I first need to determine the current status of the project.<br>
Then document it and prepare for the next steps.<br>
<br>
The general plan is that the backend is roughly completed first, before the frontend comes next.<br>
For each step in the roadmap, there is an extra project (see tab `Projects` in GitHub repository) with a Kanban board in the repository, in which the roadmap steps are broken down further.<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Project Folder Layout
The project is a full-stack application.<br>
Accordingly, there is both a `backend` and a `frontend` folder.<br>
<br>
TODO: Implement further details<br>

<!-- Change the content of comment and uncomment it at the end when everything fits.
The code for the microservice is contained in the `service` package. All of the test are in the `tests` folder.<br>
The code follows the **Model-View-Controller** pattern with all of the database code and business logic in the model (`models.py`), and all of the RESTful routing on the controller (`routes.py`).<br>

```text
├── service         <- microservice package
│   ├── common/     <- common log and error handlers
│   ├── config.py   <- Flask configuration object
│   ├── models.py   <- code for the persistent model
│   └── routes.py   <- code for the REST API routes
├── setup.cfg       <- tools setup config
└── tests                       <- folder for all of the tests
    ├── factories.py            <- test factories
    ├── test_cli_commands.py    <- CLI tests
    ├── test_models.py          <- model unit tests
    └── test_routes.py          <- route unit tests
```
-->
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### General - Tech Stack
This tech stack refers to things that are used in the frontend as well as the backend or neither.<br>
For backend or frontend specific tech stack please read the corresponding section in the `README.md`.<br>
Help is provided in the table of contents at the beginning of the `README.md`.<br>
<br>
The tech stack - `General`:<br>
- Mind Mapping Tool: XMind
- IDE: Microsoft Visual Studio
- GitHub (Version Control, Kanban Board, ...)
- Identity and Access Management: AWS IAM
- Identity and Access Management: Microsoft Authenticator
- Hosting (Security): AWS Certificate Manager
- Monitoring: AWS CloudWatch
- Monitoring: AWS Billing and Cost Management
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### General - Reasons for the Tech Stack Selection
TODO: Implement<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Complete Overview of the System
TODO: Create and insert diagramm (e. g. AWS)<br>
<!-- Help: AWS Diagramme Visio: https://www.microsoft365.com/template/Visio/?culture=de-de&country=de&categoryId=TemplateCategory_AWSDiagrams -->
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Contributors
Contributors:
- Designer: [combine visual - Christine Biendl](http://www.combine-visual.com)

If you have a suggestion that would make this better, please fork the repo and create a pull request.<br>
You can also simply open an issue with the tag `enhancement`.<br>
Don't forget to give the project a star! Thanks again!<br>

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### License
TODO: Implement. Not sure if I need this.<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Getting Started
TODO: Implement (individually for backend and frontend as well as together)<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


## Acknowledgements
* [combine visual - Christine Biendl](http://www.combine-visual.com): Thanks to the designer for her active support! The design isn't finished yet and I can't work on the project all the time due to work and other commitments. I really appreciate the fact that I can ask her for help at any time, that she responds to my questions and conjures up great designs for me.
* [othneildrew](https://github.com/othneildrew/Best-README-Template/tree/main): Thank you and the contributors of the `Best-README-template`-repository for providing the `README.md` template! I have already been able to conjure up some beautiful texts for my repositories with it.
* [PokéAPI](https://pokeapi.co/): Thanks for providing the Pokemon data! It saves a lot of work to create the data (Pokemon values, Pokedex, ...) yourself
* Creators of the Pokémon Franchise: I was able to build up many great childhood experiences and friendships with it! I still enjoy playing Pokemon today, for example on the Nintendo Switch.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Contact
If you have any questions, please feel free to reach out via email: christian-schwanse (at) gmx.net<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>



## Frontend
### Frontend - Tech Stack
- Markup Language: HTML
- Markup Language: CSS
- Programming Language: JavaScript / TypeScript
- UI Design Tool: Figma
- Library: React
- Library: Redux
- Build Tool: Vite
- Linting: ESLint
- TDD Framework: Jest
- Hosting (Storage): AWS S3
- Hosting (DNS): AWS Route 53
- Hosting (CDN): AWS CloudFront
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>

### Frontend - Reasons for the Tech Stack Selection
TODO: Implement<br>
TODO: Implement choice details in XMind Mindmap about S3, Route 53 and CloudFront (e. g. why CDN if the project is mainly aimed at Germany / the country of origin of repo owner)?<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Frontend - Development Process
The frontend is developed according to the `mobile-first` approach.<br>
A mobile-first approach prioritizes designing for mobile devices before scaling up to larger screens, ensuring a seamless user experience across all devices.<br>
<br>
The reason is that, from my point of view, it is easier to develop the desktop view retrospectively than the mobile view retrospectively.<br>
Starting mobile-first ensures a working and simpler design at small screens, and lets the door open to implement more elements, space, features, progressively as the screen size increases.<br>
<br>
Other reasons are:
- It forces you to think about the site's bare bones requirements
- You can generally get something up and running faster
- Mobile is the larger share of visitors for many / most sites

The frontend is also being developed as a `single-page application` (`SPA`).<br>
A single-page application is a website or web application that dynamically rewrites a current web page with new data from the web server, instead of the default method of a web browser loading entire new pages.<br>
This can result in performance gains and a more dynamic and better user experience (with some tradeoff disadvantages like search engine optimization).<br>
<br>
TODO: Mention GitHub Kanban Board and XMind Mindmap. Also TDD and CI/CD.<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>



## Backend
### Backend - Tech Stack
- Programming Language: Python
- Linting: PyLint
- Web Framework: Flask
- TDD Framework: unittest / nose
- Hosting: AWS Elastic Beanstalk
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Backend - Reasons for the Tech Stack Selection
TODO: Implement<br>
TODO: Explain further -> Originally planned AWS Elastic Beanstalk, but due to running costs and because this is a hobby project, another payment model (pay-as-you-go) with Amazon Lambda or similar would be good.<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Backend - Development Process
TODO: Implement<br>
TODO: Mention GitHub Kanban Board and XMind Mindmap. Also TDD and CI/CD.<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
