# Team and Project Plan
Portfolio Task 1

**Unit code:** COS40005  
**Unit name:** Computing Technology Project A  
**Submission date:** 26th of September, 2025

---

### Introduction

This document serves as the comprehensive Team and Project Plan for the development of the "AI-Enabled Digital Health Platform for Chronic Disease Monitoring," undertaken on behalf of BioTective Sdn Bhd. As a formal charter, its purpose is to provide a single source of truth for all project stakeholders, outlining the team structure, communication protocols, project scope, technical architecture, development roadmap, and quality assurance strategy.

The project's vision is to create a functional, high-fidelity prototype that demonstrates the feasibility and value of leveraging advanced AI to transform chronic disease management. This involves moving beyond simple data logging to create an intelligent, proactive system that offers personalised insights and automates timely interventions. This plan is a living document, designed to guide the team from initial setup to the final delivery of a robust and polished prototype, laying the groundwork for a future production-ready system.

| Student Name | Student Id | Description of contribution in team and project planning |
| :--- | :--- | :--- |
| Daniel | 102777801 | Coordinated the overall project planning process, led the definition of the technical and AI architecture by synthesising multiple analysis reports, and drafted the primary sections of the project plan, including the detailed solution approach and risk mitigation register. |
| Alif Harriz | 102782711 | Contributed significantly to the front-end technology selection and UI/UX strategy. Provided critical input on user-centric design principles, accessibility considerations, and helped define the teamwork roadmap and communication plan. |
| Ashley Jong | 102780087 | Assisted in the detailed breakdown of project requirements from the initial proposal, contributing to the system analysis and the creation of a granular product backlog with user stories. Also helped structure the quality assurance plan. |
| Basil Agas | 102778888 | Provided key insights during the AI framework analysis, influencing the decision to adopt a hybrid AI model and the LangChain framework. Contributed to defining the AI-related tasks and deliverables within the project plan. |
| Edison Ho | 102779496 | Led the in-depth analysis of backend, BaaS, and database technologies. Authored the rationale for selecting the Supabase platform and contributed to outlining the document management, security framework, and quality plan sections. |

---

### PART 1: TEAM CHARTER AND CODE OF CONDUCT

This section defines the team's internal operating structure, roles, responsibilities, and the agreed-upon protocols for communication, collaboration, and conflict resolution. It forms the foundation of the team’s professional conduct.

#### 1. Detailed Team Profile

The project team is a well-rounded, multidisciplinary group of computer science students, each bringing a unique specialisation that maps directly to the project's complex requirements. The synergy between their skills in Artificial Intelligence, Software Development, UI/UX Design, and Full-Stack Engineering creates a robust unit capable of tackling this ambitious project.

**Table 1: Team Profile Summary**
| Student name | Technical skills | Soft skills | Communication | Teamwork |
| :--- | :--- | :--- | :--- | :--- |
| **Daniel** | Full-stack development, AI/ML (agentic systems, image classification), multi-platform apps (IoT, games), UI design. | High attention to detail, passion for automation, user-focused design sense. | Proactive, formal written communication, primary client contact point. | Initiative-taker, project coordinator, integrator between front-end, back-end, and AI. |
| **Alif Harriz**| Front-end (HTML, CSS, JS, Vue.js), UI/UX design, prototyping (Figma). | User empathy, focus on accessibility, intuitive design. | Prefers visual communication (prototypes), comfortable with asynchronous chat. | Focuses on translating design into functional product, open to feedback. |
| **Ashley Jong**| Software design, system analysis, AI-driven problem solving, project management, requirement gathering, testing. | Detail-oriented, methodical, adaptable, strong organisational skills. | Comfortable with formal and technical discussion across multiple channels. | Collaborates on frontend and contributes to project management, ensuring requirements are met. |
| **Basil Agas** | AI development (NLP, predictive analytics), AI architecture, infrastructure (Cisco, Windows Server). | Analytical, strategic, focus on practical and ethical AI deployment. | Articulates complex technical concepts clearly. | Focuses on developing, deploying, and optimizing the core AI solutions. |
| **Edison Ho** | Full-stack development (PHP, Python), database management, cybersecurity fundamentals. | Writes clean, maintainable code, strong UI/UX consideration. | Proactive, transparent, presents ideas clearly to ensure team alignment. | Reliable, takes ownership of tasks, ensures smooth integration with other components. |

#### 2. Roles and Responsibilities

To ensure clear ownership and accountability, specific roles have been assigned. These roles are not strictly siloed; collaboration is expected and encouraged. However, the designated role owner holds the primary responsibility for the quality and timely completion of their domain's deliverables.

**Table 2: Team Roles and Primary Responsibilities**
| Role | Assigned To | Justification & Core Responsibilities |
| :--- | :--- | :--- |
| **Project Lead & AI Engineer** | **Daniel** | With a full-stack perspective and a major in AI, Daniel is ideally suited to lead the project, ensuring all parts (frontend, backend, AI) integrate seamlessly. **Responsibilities:** Facilitate team meetings, manage the project backlog in GitHub, act as the primary liaison with Dr. Vong, resolve team blockers, and co-develop the core AI agentic framework. |
| **Frontend Developer (Clinician Dashboard)** | **Alif Harriz** | Alif's focused expertise in front-end development and UX design is perfect for creating the data-rich, intuitive, and responsive clinician dashboard. **Responsibilities:** Translate Figma designs into functional Flutter widgets, ensure the dashboard is performant and visually polished, implement data visualizations for clinician view, and champion accessibility standards. |
| **Frontend Developer (Patient Dashboard)** | **Ashley Jong** | Ashley's double major in Software Development and AI, combined with her user-focused approach, makes her well-suited to build the patient-facing dashboard. **Responsibilities:** Develop the patient dashboard UI in Flutter, integrate the chatbot interface, ensure patient data is displayed clearly and effectively, and collaborate on testing and requirement validation. |
| **Lead AI Engineer** | **Basil Agas** | Basil's specialisation in the architectural and operational aspects of AI systems makes him the ideal candidate to lead the development of the core recommendation engine and automation triggers. **Responsibilities:** Implement the hybrid AI model, train the quantitative predictive model, develop the LangChain tools for the LLM agent, and optimize AI performance and response accuracy. |
| **Backend Developer** | **Edison Ho** | Edison's hands-on experience in building full-stack applications and managing databases is critical for the project's foundation. **Responsibilities:** Develop the Python backend API (FastAPI), design and implement the Supabase database schema, configure Row-Level Security policies, and ensure seamless data flow between the frontend and the database. |

#### 3. Teamwork Roadmap and Collaboration Framework

This framework outlines the processes and tools the team will use to maintain momentum, ensure transparency, and foster a productive working environment.

*   **Meeting Cadence:**
    *   **Class Sync (Twice Weekly):** Mandatory meetings will occur during scheduled class times on Tuesdays and Thursdays. These sessions will be used for formal progress reviews, sprint planning, and supervisor consultations.
    *   **Working Sessions (Twice Weekly):** Additional, less formal working sessions will be scheduled on Fridays and Saturdays. These are hands-on, collaborative sessions dedicated to coding, debugging, and integration.
    *   **Mode of Operation:** The default mode for all meetings will be in-person to facilitate high-bandwidth communication. An online option via Microsoft Teams will be available for members who are unable to attend physically.

*   **Communication Plan:**
    *   **Informal/Daily Communication:** **WhatsApp** will be the primary channel for quick questions, daily updates, and urgent coordination. A maximum response time of 12 hours is expected.
    *   **Formal Communication:** **Email** will be used for all official communication with the project supervisor (Dr. Vong) and for documenting key decisions.
    *   **Technical Discussion:** **GitHub Issues and Pull Requests** will be the venue for all technical discussions, code reviews, and bug tracking to keep conversations linked to the relevant code.

*   **Task Management Workflow:**
    *   **Tool:** The team will exclusively use **GitHub Projects** and **GitHub Issues** for all task management.
    *   **Lifecycle of a Task:** Each task will be created as an Issue and will progress through the following stages on the project board:
        1.  **Backlog:** Awaiting prioritization.
        2.  **To Do:** Prioritized for the current sprint.
        3.  **In Progress:** Actively being worked on by an assigned team member.
        4.  **In Review:** A Pull Request has been opened and is awaiting code review.
        5.  **Done:** The Pull Request has been approved and merged, and the feature meets the Definition of Done.
    *   **Definition of Done (DoD):** A task is considered "Done" only when it meets all the following criteria:
        *   Code is successfully merged into the `main` branch.
        *   Code is formatted and linted according to project standards.
        *   All related acceptance criteria are met.
        *   The feature has been manually tested and verified by someone other than the author.
        *   Relevant documentation (if any) has been updated.

*   **Conflict Resolution:**
    1.  Disagreements should first be discussed directly and respectfully between the involved team members.
    2.  If a resolution cannot be reached, the issue will be brought to the next team meeting for a group discussion, mediated by the Project Lead.
    3.  If the team cannot reach a consensus, the Project Lead will make a final decision after considering all viewpoints.
    4.  For critical issues that impact the project scope or timeline, the matter will be escalated to the Project Supervisor for guidance.

#### 4. Document and Configuration Management

A systematic approach to managing project assets is crucial for consistency and collaboration.

*   **Code Version Control:**
    *   **System:** Git.
    *   **Platform:** GitHub.
    *   **Branching Strategy:** The team will adopt the **GitFlow** branching model.
        *   `main`: Contains production-ready, stable code. Direct commits are forbidden.
        *   `develop`: The primary integration branch for ongoing development.
        *   `feature/<feature-name>`: All new work must be done in a feature branch, created from `develop`.
        *   Pull Requests (PRs) are mandatory for merging feature branches back into `develop`. Each PR must be reviewed and approved by at least one other team member.

*   **Document Management:**
    *   **Platform:** **Microsoft OneDrive** will serve as the central repository for all non-code documents, including this project plan, user guides, meeting minutes, and research materials.
    *   **Collaborative Editing:** Microsoft Office 365 (Word, Excel, PowerPoint) will be used for real-time collaborative editing and commenting.
    *   **Backup Strategy:** In addition to cloud storage, critical documents will be backed up manually on a bi-weekly basis to a separate offline storage device.

#### 5. Risk Management

A proactive approach to risk management is essential. The following register identifies potential risks and outlines a plan to address them. This register will be reviewed and updated at the beginning of each sprint.

**Table 3: Risk Register**
| ID | Risk Description | Impact | Likelihood | Risk Owner | Mitigation and Contingency Plan |
|:---|:---|:---|:---|:---|:---|
| **R1** | **Technical Skill Gap:** A team member may lack the necessary expertise in a required technology (e.g., Flutter state management, advanced RLS policies). | Medium | Medium | Project Lead | **Mitigation:** Promote a culture of knowledge sharing and pair programming. Allocate dedicated time within sprints for learning and experimentation. Encourage the use of online tutorials and documentation. <br> **Contingency:** If a critical gap persists, the team will consult with the project supervisor for expert guidance or an alternative approach. |
| **R2** | **Team Member Unavailability:** A key member becomes unavailable for an extended period due to illness or personal emergency. | High | Low | Project Lead | **Mitigation:** Enforce a strict policy of daily code commits to GitHub and maintain high-quality documentation. Implement a "buddy system" where knowledge for critical components (Backend, AI core) is shared between two members. <br> **Contingency:** The "buddy" will take over the primary responsibilities. The Project Lead will re-allocate tasks across the remaining team members and adjust the sprint scope if necessary. |
| **R3** | **Scope Creep:** The client or team introduces new features or changes that are outside the original project scope. | Medium | Medium | Project Lead | **Mitigation:** All change requests must be formally documented as a GitHub Issue. The team will perform an impact analysis to assess the effect on the timeline and resources. <br> **Contingency:** The Project Lead will present the impact analysis to Dr. Vong to get formal approval before any changes are incorporated into the project backlog. Low-impact changes may be deferred to a "post-prototype" backlog. |
| **R4** | **Integration Issues:** The frontend, backend, and AI modules fail to communicate correctly, causing significant delays late in the project. | High | Medium | All Team | **Mitigation:** Define clear API contracts (e.g., using OpenAPI/Swagger) between services early in the project. Conduct frequent integration testing throughout the development cycle. Implement a shared "mock server" so frontend and backend can develop in parallel. <br> **Contingency:** Allocate a dedicated "integration week" before the final submission to resolve any complex integration bugs. |
| **R5** | **AI Model Underperformance:** The LLM agent hallucinates, provides inaccurate recommendations, or the predictive model has low accuracy. | High | Medium | AI Engineers | **Mitigation:** Employ a Retrieval-Augmented Generation (RAG) pattern to ground the LLM's responses in a trusted knowledge base. Use a high-quality, clean dataset for fine-tuning. Rigorously validate the predictive model's performance using standard metrics (e.g., RMSE, F1-score). <br> **Contingency:** If the LLM is unreliable, implement a stricter rule-based NLP system as a fallback for critical recommendations. If the predictive model is inaccurate, retrain it with more features or a different algorithm. |
| **R6** | **Simulated Data Unrealistic:** The patient data simulator produces data that is too simplistic or does not accurately reflect real-world health patterns, leading to a poorly trained AI model. | Medium | Medium | Backend Developer | **Mitigation:** Research common patterns in chronic disease data (e.g., post-meal glucose spikes, effect of exercise). Incorporate randomness and variability into the simulator to mimic real patient behavior. <br> **Contingency:** Consult with Dr. Vong or external resources to refine the simulation logic. Use a public, anonymized health dataset as a reference to validate the simulator's output distribution. |

---
### PART 2: PROJECT OVERVIEW AND PLAN

This section details the project itself, covering the problem it aims to solve, its boundaries, objectives, technical architecture, and the roadmap for its execution.

#### 1. Project Background and Problem Statement

**Background:** The management of chronic diseases like Type 2 Diabetes is a persistent challenge in modern healthcare. Patients are often overwhelmed by the need to constantly monitor various health metrics (blood glucose, diet, activity, etc.) and struggle to interpret this data effectively. Healthcare providers, in turn, lack the tools for real-time monitoring and are often limited to providing guidance during infrequent appointments, relying on incomplete, patient-recalled information. This results in a reactive, rather than proactive, approach to care.

**Problem Statement:** Chronic disease patients lack a unified platform that integrates their fragmented health data and provides real-time, actionable, and personalised guidance. Existing digital health solutions often act as simple data repositories and do not fully leverage the power of Artificial Intelligence to detect early warning signs, predict adverse events, or provide context-aware recommendations. BioTective seeks to address this gap by developing a prototype solution that serves as an intelligent companion for patients and a powerful monitoring tool for clinicians, ultimately aiming to improve health outcomes through timely, AI-driven interventions.

#### 2. Project Goals and SMART Objectives

*   **Project Goal:** To successfully design, develop, test, and deliver a high-fidelity prototype of an AI-Enabled Digital Health Platform that meets all the functional and non-functional requirements outlined in the project proposal by the end of the semester.

*   **SMART Objectives:**
    1.  **Specific:** Develop a cross-platform application (mobile and web) with distinct patient and clinician dashboards, an AI-powered recommendation engine, an automation layer for alerts, and a patient-facing chatbot.
    2.  **Measurable:** Successfully complete all 20+ user stories defined in the product backlog, achieve a code review approval rate of 100% for all merged PRs, and ensure the final prototype passes all end-to-end testing scenarios without critical bugs.
    3.  **Achievable:** The project scope is defined by six clear milestones and will be developed by a skilled five-person team using a modern, efficient technology stack. The use of a BaaS platform and high-level frameworks makes the timeline feasible.
    4.  **Relevant:** The prototype directly addresses the problem statement provided by BioTective, demonstrating a solution that can enhance patient outcomes and improve the efficiency of chronic disease care, aligning with the company's mission.
    5.  **Time-bound:** The entire project, from planning to final prototype demonstration and documentation, will be completed within the official timeline of the COS40005 Computing Technology Project A unit.

#### 3. Scope, Assumptions, and Constraints

*   **In-Scope:**
    *   Development of all features outlined in the six project milestones.
    *   A functional prototype integrating patient and clinician views.
    *   An AI-powered recommendation engine (hybrid model) and an automation layer (LAM Triggers).
    *   A functional, AI-powered patient-facing chatbot for health data Q&A.
    *   Implementation of robust, database-level role-based access control for security.
    *   Development and use of a custom patient data simulator for all development and testing.

*   **Out-of-Scope:**
    *   Deployment to a live, production environment with real patient data.
    *   Integration with real, physical health monitoring devices (e.g., Bluetooth glucose meters).
    *   The legal and financial process of achieving HIPAA compliance and signing a Business Associate Agreement (BAA).
    *   User onboarding flows, billing/subscription features, and company-level administrative dashboards.

*   **Assumptions:**
    *   The team will have access to all necessary software and development tools (IDEs, Flutter SDK, Python, etc.).
    *   The project requirements as defined in the proposal will remain stable throughout the project lifecycle.
    *   The team has the necessary collective skills to execute the project plan.
    *   The project supervisor will be available for regular consultation and guidance.

*   **Constraints:**
    *   The project must be completed within the fixed semester timeline.
    *   The prototype will be developed using only simulated data due to the ethical and legal constraints of handling Protected Health Information (PHI).
    *   The budget for using third-party APIs (e.g., LLM providers) is limited and must be managed carefully.

#### 4. Stakeholders

| Stakeholder | Role | Interest/Expectations |
| :--- | :--- | :--- |
| **BioTective Sdn Bhd** | Client | Expects a functional, polished prototype that validates their product concept and can be used for future investment pitches or as a foundation for a production build. |
| **Ts. Dr. Vong Wan Tze** | Supervisor | Expects the team to follow a structured project management methodology, demonstrate technical proficiency, and deliver a high-quality project that meets academic standards. |
| **Patients & Clinicians** | End Users | (Represented by personas) Expect an intuitive, reliable, and useful platform that simplifies health management and provides valuable, trustworthy insights. |
| **Development Team** | Executors | Aims to successfully deliver the project, gain practical experience in building a complex AI application, and achieve a high academic grade. |

#### 5. Detailed Solution Approach and System Architecture

The proposed architecture is a modern, decoupled system designed for scalability, security, and rapid development, leveraging best-in-class technologies for each component. This design is the result of a rigorous analysis of the cross-platform, backend, and AI framework landscapes.

*   **Frontend Architecture:**
    *   **Framework:** **Flutter**. Chosen as the definitive cross-platform solution to meet the "code once, deploy anywhere" requirement. Its compiled native performance and declarative UI paradigm (widgets) are ideal for creating the fluid, responsive user experience required for both mobile and desktop platforms.
    *   **State Management:** The team will adopt a standardized state management solution, likely **Provider** or **BLoC**, to manage application state predictably and prevent UI inconsistencies.
    *   **Data Visualization:** The **`fl_chart`** library has been selected for its rich feature set, extensive customization, and strong community support, making it perfect for rendering the required trend charts and weekly summaries.

*   **Backend Architecture:**
    *   **Language/Framework:** **Python 3.11+** with the **FastAPI** framework. This choice is non-negotiable, driven by Python's unrivalled ecosystem for AI and data science. FastAPI provides a high-performance, modern framework for building RESTful APIs with automatic documentation.
    *   **Deployment:** The Python backend will be deployed as serverless functions (e.g., on Google Cloud Functions or Vercel), managed via the chosen BaaS platform to minimize DevOps overhead.

*   **Data and BaaS Architecture:**
    *   **Platform:** **Supabase**. Chosen over Firebase for its open-source nature and powerful PostgreSQL foundation. Supabase provides an integrated suite of essential backend services out-of-the-box.
    *   **Database:** A **PostgreSQL** database managed by Supabase. A relational schema will be designed to store user data, patient health records, diet logs, and clinician-patient relationships.
    *   **Authentication:** **Supabase Auth** will be used for secure user registration and login, handling JWTs for session management.
    *   **Security:** **Row-Level Security (RLS)** is the cornerstone of the security architecture. Fine-grained SQL policies will be written directly in the database to enforce strict data access rules. For example: `CREATE POLICY "Patients can only see their own data." ON health_records FOR SELECT USING (auth.uid() = user_id);`. This ensures that data segregation is enforced at the lowest possible level, preventing accidental data leaks.

*   **Hybrid AI Architecture:**
    The project will implement a sophisticated hybrid AI model, as a single monolithic model is suboptimal for the diverse tasks required. This strategy separates quantitative analysis from qualitative reasoning.
    1.  **The "Quantitative Analyst" (Predictive Model):**
        *   **Model:** An **XGBoost** or **RandomForest** model.
        *   **Function:** This traditional machine learning model will be trained on the simulated data to perform precise, numerical forecasting tasks, such as predicting the peak blood glucose level after a logged meal. Its output is a structured, numerical value.
    2.  **The "Qualitative Strategist" (LLM Agent):**
        *   **Model:** A powerful foundation Large Language Model (e.g., GPT-4, Claude 3) with strong tool-calling capabilities.
        *   **Framework:** **LangChain**. This framework will be used to create an autonomous agent.
        *   **Function:** The agent acts as the system's "brain." It receives context (e.g., patient data, the prediction from the Quantitative Analyst) and uses its reasoning ability to decide on a course of action. It can then use a predefined set of "tools" (custom Python functions) to execute this plan. For instance, it could use a tool to fetch the patient's full diet history from Supabase, another to check for recent activity, and then synthesize all this information into a comprehensive, empathetic recommendation. This is the core of the "Large Action Model" (LAM) system.

  
*(Conceptual Diagram: A flow chart showing patient data entering the system. It splits, with numerical data going to an XGBoost model for prediction. The prediction and qualitative data then go to a LangChain agent (LLM). The agent uses tools to query the Supabase DB, and finally outputs an action/recommendation back to the user via the Flutter app.)*

#### 6. Detailed Product Backlog

This backlog breaks down the project milestones into actionable user stories, which will be managed as GitHub Issues.

| ID | User Story | Priority | Story Points | Acceptance Criteria | Sprint |
|:---|:---|:---|:---|:---|:---|
| **EPIC 1: Project Foundation & Patient View (M1 & M2)** |
| T1.1 | As a developer, I want to set up the project structure with a GitHub repo and CI/CD pipeline so that we have a foundation for collaborative work. | **High** | 3 | Repo created, GitFlow branches configured, basic linting action runs on PR. | 1 |
| T1.2 | As a developer, I want to set up the Supabase project with a complete database schema so that we can store user and health data. | **High** | 5 | All tables (users, patients, clinicians, glucose, diet, activity) are created with correct relationships and constraints. | 1 |
| T1.3 | As a patient/clinician, I want to securely sign up, log in, and log out so that I can access the platform and my data is protected. | **High** | 8 | Users can register. Users can log in with email/password. JWT is issued on login. RLS policies for basic access are in place. | 1 |
| T1.4 | As a developer, I need a Python script to simulate and populate the database with realistic patient data so that we can develop and test features. | **High** | 8 | Script generates data for multiple patients over several weeks. Data includes realistic patterns like meal-related glucose spikes. | 1 |
| T2.1 | As a patient, I want to see a dashboard with visualizations of my key health metrics (glucose, HbA1c, diet, activity) so that I can understand my trends. | **High** | 13 | Dashboard UI is built in Flutter. `fl_chart` widgets display data from Supabase. UI is responsive for mobile/desktop. | 1 |
| **EPIC 2: AI Core & Automation (M3 & M4)** |
| T3.1 | As an AI Engineer, I want to develop and train an XGBoost model to predict glucose spikes based on meal logs so that the system has quantitative predictive power. | **High** | 13 | Model is trained on simulated data. Model achieves an acceptable accuracy metric (e.g., RMSE < 1.0). Model can be called via a FastAPI endpoint. | 2 |
| T3.2 | As an AI Engineer, I want to build a LangChain agent that can reason about patient data and use tools to fetch additional information from the database. | **High** | 21 | Agent is initialized with a base LLM. At least two tools are created (e.g., `get_recent_glucose`, `get_diet_history`). Agent can successfully call tools and use their output. | 2 |
| T3.3 | As a patient, I want to receive personalised recommendations (e.g., meal substitutions, activity suggestions) based on my data patterns. | **High** | 13 | The LangChain agent synthesizes data and predictions to generate a text recommendation. Recommendation is displayed on the patient dashboard. | 2 |
| T4.1 | As a developer, I want to create an automation layer (LAM Triggers) that runs periodically to check for abnormal health patterns in the database. | **High** | 8 | A scheduled serverless function is created that queries the database for trigger conditions (e.g., high glucose, low activity). | 2 |
| T4.2 | As a patient, I want to receive a timely reminder (e.g., push notification) to take a short walk after a high-carb meal is detected. | **Medium**| 5 | A LAM Trigger identifies a high-carb meal and a subsequent glucose spike, triggering a notification event. | 2 |
| **EPIC 3: Clinician View & Finalisation (M5 & M6)** |
| T5.1 | As a clinician, I want to see a dashboard with a list of my assigned patients, highlighting those who need urgent attention. | **High** | 13 | Clinician dashboard UI is built. RLS policies ensure clinicians only see their assigned patients. A risk-scoring system flags high-risk patients. | 3 |
| T5.2 | As a patient, I want to use a chatbot to ask simple questions about my health data (e.g., "What was my average glucose this week?"). | **Medium**| 13 | Chat UI is built in Flutter. The LangChain agent is connected to the chat interface to provide AI-generated responses based on the patient's data. | 3 |
| T6.1 | As a developer, I want to conduct end-to-end system testing using a multi-patient dataset to ensure all components function correctly together. | **High** | 8 | A comprehensive test plan is executed. All critical bugs are logged and resolved. | 3 |
| T6.2 | As a team, we want to finalize all project documentation, including a comprehensive user guide and technical documentation, for final submission. | **High** | 13 | User guide for patients/clinicians is written. Technical documentation covers architecture and setup instructions. | 3 |

#### 7. Quality Assurance Plan

The team is committed to delivering a high-quality prototype. Quality is not just a final check but a continuous process integrated throughout the development lifecycle.

*   **Code Quality Standards:**
    *   **Style Guides:** The team will strictly enforce official style guides: **PEP 8** for Python and **Effective Dart** for Flutter.
    *   **Linters & Formatters:** Automated tools will be integrated into the development environment and CI pipeline. **Black** and **Pylint** for Python, and Dart's built-in `dart format` and linter for Flutter. Commits that do not pass linting will be blocked.

*   **Testing Strategy:**
    *   **Unit Testing:** Developers are responsible for writing unit tests for their code, especially for critical backend logic, utility functions, and AI model inputs/outputs. The target is to achieve a reasonable level of code coverage for business-critical modules. Tools: `pytest` for Python, `flutter_test` for Flutter.
    *   **Integration Testing:** At the end of each week, the team will conduct integration tests to ensure that the frontend can successfully communicate with the backend API and that the API can correctly interact with the Supabase database.
    *   **End-to-End (E2E) System Testing:** During the final sprint, the team will perform comprehensive E2E testing based on the user stories. This involves testing the entire workflow from the user's perspective (e.g., logging a meal, seeing a glucose spike, receiving a recommendation).
    *   **User Acceptance Testing (UAT):** In the final two weeks, team members will engage in peer-UAT, where they test the features developed by others, acting as both a patient and a clinician to identify usability issues and bugs.

*   **Defect Management:**
    *   **Reporting:** All bugs and defects must be reported as a **GitHub Issue** using a standardized bug report template.
    *   **Tracking:** Each bug will be labelled, assigned a priority (Critical, High, Medium, Low), and assigned to a team member.
    *   **Resolution:** A bug is considered resolved only after a fix has been committed, merged, and the fix has been verified by the original reporter or another team member.