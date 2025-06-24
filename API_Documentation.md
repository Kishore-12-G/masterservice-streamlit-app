# VetNet Microservice API Documentation for Testing

This documentation provides detailed information on the VetNet Microservice API endpoints, including input fields, sample inputs, and sample outputs for all operations (GET, POST, PUT, DELETE, DELETE_MANY). It is designed to assist users in testing the API using the Streamlit application located in the `api-tester` directory. Each section covers a specific API category, ensuring you have the necessary data to interact with the endpoints effectively.

## Table of Contents
- [Companies](#companies)
- [Certifications](#certifications)
- [Degrees](#degrees)
- [Universities](#universities)
- [Job Titles](#job-titles)
- [Skills](#skills)
- [Field of Studies](#field-of-studies)

## Companies

**Purpose**: Manage company data, including details like name, logo, industry, website, and location.

**Base Endpoint**: `/companies`

### Operations

#### GET `/companies`
- **Description**: Retrieve a list of all companies.
- **Input**: None
- **Sample Output**:
  ```json
  [
    {
      "id": 1,
      "name": "Acme Corporation",
      "logo": "https://example.com/logo.png",
      "industry": "Technology",
      "website": "https://acme.com",
      "location": "San Francisco, CA",
      "isActive": true,
      "createdAt": "2025-06-23T08:00:00.000Z",
      "updatedAt": "2025-06-23T08:00:00.000Z"
    },
    {
      "id": 2,
      "name": "Beta Inc.",
      "logo": "https://beta.com/logo.jpg",
      "industry": "Finance",
      "website": "https://beta.com",
      "location": "New York, NY",
      "isActive": true,
      "createdAt": "2025-06-23T09:00:00.000Z",
      "updatedAt": "2025-06-23T09:00:00.000Z"
    }
  ]
  ```

#### POST `/companies`
- **Description**: Create a new company.
- **Input Fields**:
  - `name` (Required, Text): The name of the company.
  - `logo` (Optional, Text): URL to the company's logo.
  - `industry` (Optional, Text): Industry the company operates in.
  - `website` (Optional, Text): URL to the company's website.
  - `location` (Optional, Text): Physical location of the company.
  - `isActive` (Optional, Checkbox, Default: True): Whether the company is active.
- **Sample Input**:
  ```json
  {
    "name": "Acme Corporation",
    "logo": "https://example.com/logo.png",
    "industry": "Technology",
    "website": "https://acme.com",
    "location": "San Francisco, CA",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Acme Corporation",
    "logo": "https://example.com/logo.png",
    "industry": "Technology",
    "website": "https://acme.com",
    "location": "San Francisco, CA",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T08:00:00.000Z"
  }
  ```

#### PUT `/companies/{id}`
- **Description**: Update an existing company by ID.
- **Input Fields**: Same as POST.
- **Sample Input** (for ID 1):
  ```json
  {
    "name": "Acme Corporation Updated",
    "logo": "https://example.com/logo-updated.png",
    "industry": "Technology",
    "website": "https://acme-updated.com",
    "location": "San Francisco, CA",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Acme Corporation Updated",
    "logo": "https://example.com/logo-updated.png",
    "industry": "Technology",
    "website": "https://acme-updated.com",
    "location": "San Francisco, CA",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T10:00:00.000Z"
  }
  ```

#### DELETE `/companies/{id}`
- **Description**: Delete a company by ID.
- **Input**: ID of the company to delete (e.g., 1)
- **Sample Output**:
  ```json
  {
    "message": "Company with ID 1 deleted successfully."
  }
  ```

#### DELETE_MANY `/companies/deleteMany`
- **Description**: Delete multiple companies (implementation may vary; often requires a list of IDs in the body depending on API design).
- **Input**: None (or a list of IDs if supported by API)
- **Sample Output**:
  ```json
  {
    "message": "Multiple companies deleted successfully.",
    "count": 2
  }
  ```

## Certifications

**Purpose**: Manage certification data for professional qualifications.

**Base Endpoint**: `/certifications`

### Operations

#### GET `/certifications`
- **Description**: Retrieve a list of all certifications.
- **Input**: None
- **Sample Output**:
  ```json
  [
    {
      "id": 1,
      "name": "AWS Certified Solutions Architect",
      "isActive": true,
      "createdAt": "2025-06-23T08:00:00.000Z",
      "updatedAt": "2025-06-23T08:00:00.000Z"
    },
    {
      "id": 2,
      "name": "Cisco Certified Network Associate",
      "isActive": true,
      "createdAt": "2025-06-23T09:00:00.000Z",
      "updatedAt": "2025-06-23T09:00:00.000Z"
    }
  ]
  ```

#### POST `/certifications`
- **Description**: Create a new certification.
- **Input Fields**:
  - `name` (Required, Text): The name of the certification.
  - `isActive` (Optional, Checkbox, Default: True): Whether the certification is active.
- **Sample Input**:
  ```json
  {
    "name": "AWS Certified Solutions Architect",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "AWS Certified Solutions Architect",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T08:00:00.000Z"
  }
  ```

#### PUT `/certifications/{id}`
- **Description**: Update an existing certification by ID.
- **Input Fields**: Same as POST.
- **Sample Input** (for ID 1):
  ```json
  {
    "name": "AWS Certified Solutions Architect - Professional",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "AWS Certified Solutions Architect - Professional",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T10:00:00.000Z"
  }
  ```

#### DELETE `/certifications/{id}`
- **Description**: Delete a certification by ID.
- **Input**: ID of the certification to delete (e.g., 1)
- **Sample Output**:
  ```json
  {
    "message": "Certification with ID 1 deleted successfully."
  }
  ```

#### DELETE_MANY `/certifications/deleteMany`
- **Description**: Delete multiple certifications.
- **Input**: None (or a list of IDs if supported by API)
- **Sample Output**:
  ```json
  {
    "message": "Multiple certifications deleted successfully.",
    "count": 2
  }
  ```

## Degrees

**Purpose**: Manage academic degree data.

**Base Endpoint**: `/degrees`

### Operations

#### GET `/degrees`
- **Description**: Retrieve a list of all degrees.
- **Input**: None
- **Sample Output**:
  ```json
  [
    {
      "id": 1,
      "name": "Bachelor of Science in Computer Science",
      "isActive": true,
      "createdAt": "2025-06-23T08:00:00.000Z",
      "updatedAt": "2025-06-23T08:00:00.000Z"
    },
    {
      "id": 2,
      "name": "Master of Business Administration",
      "isActive": true,
      "createdAt": "2025-06-23T09:00:00.000Z",
      "updatedAt": "2025-06-23T09:00:00.000Z"
    }
  ]
  ```

#### POST `/degrees`
- **Description**: Create a new degree.
- **Input Fields**:
  - `name` (Required, Text): The name of the degree.
  - `isActive` (Optional, Checkbox, Default: True): Whether the degree is active.
- **Sample Input**:
  ```json
  {
    "name": "Bachelor of Science in Computer Science",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Bachelor of Science in Computer Science",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T08:00:00.000Z"
  }
  ```

#### PUT `/degrees/{id}`
- **Description**: Update an existing degree by ID.
- **Input Fields**: Same as POST.
- **Sample Input** (for ID 1):
  ```json
  {
    "name": "Bachelor of Science in Software Engineering",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Bachelor of Science in Software Engineering",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T10:00:00.000Z"
  }
  ```

#### DELETE `/degrees/{id}`
- **Description**: Delete a degree by ID.
- **Input**: ID of the degree to delete (e.g., 1)
- **Sample Output**:
  ```json
  {
    "message": "Degree with ID 1 deleted successfully."
  }
  ```

#### DELETE_MANY `/degrees/deleteMany`
- **Description**: Delete multiple degrees.
- **Input**: None (or a list of IDs if supported by API)
- **Sample Output**:
  ```json
  {
    "message": "Multiple degrees deleted successfully.",
    "count": 2
  }
  ```

## Universities

**Purpose**: Manage university data, including name, location, and website.

**Base Endpoint**: `/universities`

### Operations

#### GET `/universities`
- **Description**: Retrieve a list of all universities.
- **Input**: None
- **Sample Output**:
  ```json
  [
    {
      "id": 1,
      "name": "Stanford University",
      "location": "Stanford, CA",
      "website": "https://stanford.edu",
      "isActive": true,
      "createdAt": "2025-06-23T08:00:00.000Z",
      "updatedAt": "2025-06-23T08:00:00.000Z"
    },
    {
      "id": 2,
      "name": "MIT",
      "location": "Cambridge, MA",
      "website": "https://mit.edu",
      "isActive": true,
      "createdAt": "2025-06-23T09:00:00.000Z",
      "updatedAt": "2025-06-23T09:00:00.000Z"
    }
  ]
  ```

#### POST `/universities`
- **Description**: Create a new university.
- **Input Fields**:
  - `name` (Required, Text): The name of the university.
  - `location` (Optional, Text): Physical location of the university.
  - `website` (Optional, Text): URL to the university's website.
  - `isActive` (Optional, Checkbox, Default: True): Whether the university is active.
- **Sample Input**:
  ```json
  {
    "name": "Stanford University",
    "location": "Stanford, CA",
    "website": "https://stanford.edu",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Stanford University",
    "location": "Stanford, CA",
    "website": "https://stanford.edu",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T08:00:00.000Z"
  }
  ```

#### PUT `/universities/{id}`
- **Description**: Update an existing university by ID.
- **Input Fields**: Same as POST.
- **Sample Input** (for ID 1):
  ```json
  {
    "name": "Stanford University Updated",
    "location": "Stanford, CA",
    "website": "https://stanford-updated.edu",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Stanford University Updated",
    "location": "Stanford, CA",
    "website": "https://stanford-updated.edu",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T10:00:00.000Z"
  }
  ```

#### DELETE `/universities/{id}`
- **Description**: Delete a university by ID.
- **Input**: ID of the university to delete (e.g., 1)
- **Sample Output**:
  ```json
  {
    "message": "University with ID 1 deleted successfully."
  }
  ```

#### DELETE_MANY `/universities/deleteMany`
- **Description**: Delete multiple universities.
- **Input**: None (or a list of IDs if supported by API)
- **Sample Output**:
  ```json
  {
    "message": "Multiple universities deleted successfully.",
    "count": 2
  }
  ```

## Job Titles

**Purpose**: Manage job title data for professional roles.

**Base Endpoint**: `/jobtitles`

### Operations

#### GET `/jobtitles`
- **Description**: Retrieve a list of all job titles.
- **Input**: None
- **Sample Output**:
  ```json
  [
    {
      "id": 1,
      "name": "Software Engineer",
      "isActive": true,
      "createdAt": "2025-06-23T08:00:00.000Z",
      "updatedAt": "2025-06-23T08:00:00.000Z"
    },
    {
      "id": 2,
      "name": "Product Manager",
      "isActive": true,
      "createdAt": "2025-06-23T09:00:00.000Z",
      "updatedAt": "2025-06-23T09:00:00.000Z"
    }
  ]
  ```

#### POST `/jobtitles`
- **Description**: Create a new job title.
- **Input Fields**:
  - `name` (Required, Text): The name of the job title.
  - `isActive` (Optional, Checkbox, Default: True): Whether the job title is active.
- **Sample Input**:
  ```json
  {
    "name": "Software Engineer",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Software Engineer",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T08:00:00.000Z"
  }
  ```

#### PUT `/jobtitles/{id}`
- **Description**: Update an existing job title by ID.
- **Input Fields**: Same as POST.
- **Sample Input** (for ID 1):
  ```json
  {
    "name": "Senior Software Engineer",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Senior Software Engineer",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T10:00:00.000Z"
  }
  ```

#### DELETE `/jobtitles/{id}`
- **Description**: Delete a job title by ID.
- **Input**: ID of the job title to delete (e.g., 1)
- **Sample Output**:
  ```json
  {
    "message": "Job Title with ID 1 deleted successfully."
  }
  ```

#### DELETE_MANY `/jobtitles/deleteMany`
- **Description**: Delete multiple job titles.
- **Input**: None (or a list of IDs if supported by API)
- **Sample Output**:
  ```json
  {
    "message": "Multiple job titles deleted successfully.",
    "count": 2
  }
  ```

## Skills

**Purpose**: Manage skill data for professional competencies.

**Base Endpoint**: `/skills`

### Operations

#### GET `/skills`
- **Description**: Retrieve a list of all skills.
- **Input**: None
- **Sample Output**:
  ```json
  [
    {
      "id": 1,
      "name": "Python Programming",
      "isActive": true,
      "createdAt": "2025-06-23T08:00:00.000Z",
      "updatedAt": "2025-06-23T08:00:00.000Z"
    },
    {
      "id": 2,
      "name": "Machine Learning",
      "isActive": true,
      "createdAt": "2025-06-23T09:00:00.000Z",
      "updatedAt": "2025-06-23T09:00:00.000Z"
    }
  ]
  ```

#### POST `/skills`
- **Description**: Create a new skill.
- **Input Fields**:
  - `name` (Required, Text): The name of the skill.
  - `isActive` (Optional, Checkbox, Default: True): Whether the skill is active.
- **Sample Input**:
  ```json
  {
    "name": "Python Programming",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Python Programming",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T08:00:00.000Z"
  }
  ```

#### PUT `/skills/{id}`
- **Description**: Update an existing skill by ID.
- **Input Fields**: Same as POST.
- **Sample Input** (for ID 1):
  ```json
  {
    "name": "Advanced Python Programming",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Advanced Python Programming",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T10:00:00.000Z"
  }
  ```

#### DELETE `/skills/{id}`
- **Description**: Delete a skill by ID.
- **Input**: ID of the skill to delete (e.g., 1)
- **Sample Output**:
  ```json
  {
    "message": "Skill with ID 1 deleted successfully."
  }
  ```

#### DELETE_MANY `/skills/deleteMany`
- **Description**: Delete multiple skills.
- **Input**: None (or a list of IDs if supported by API)
- **Sample Output**:
  ```json
  {
    "message": "Multiple skills deleted successfully.",
    "count": 2
  }
  ```

## Field of Studies

**Purpose**: Manage field of study data for academic disciplines.

**Base Endpoint**: `/fieldofstudies`

### Operations

#### GET `/fieldofstudies`
- **Description**: Retrieve a list of all fields of study.
- **Input**: None
- **Sample Output**:
  ```json
  [
    {
      "id": 1,
      "name": "Computer Science",
      "isActive": true,
      "createdAt": "2025-06-23T08:00:00.000Z",
      "updatedAt": "2025-06-23T08:00:00.000Z"
    },
    {
      "id": 2,
      "name": "Electrical Engineering",
      "isActive": true,
      "createdAt": "2025-06-23T09:00:00.000Z",
      "updatedAt": "2025-06-23T09:00:00.000Z"
    }
  ]
  ```

#### POST `/fieldofstudies`
- **Description**: Create a new field of study.
- **Input Fields**:
  - `name` (Required, Text): The name of the field of study.
  - `isActive` (Optional, Checkbox, Default: True): Whether the field of study is active.
- **Sample Input**:
  ```json
  {
    "name": "Computer Science",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Computer Science",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T08:00:00.000Z"
  }
  ```

#### PUT `/fieldofstudies/{id}`
- **Description**: Update an existing field of study by ID.
- **Input Fields**: Same as POST.
- **Sample Input** (for ID 1):
  ```json
  {
    "name": "Computer Science and Engineering",
    "isActive": true
  }
  ```
- **Sample Output**:
  ```json
  {
    "id": 1,
    "name": "Computer Science and Engineering",
    "isActive": true,
    "createdAt": "2025-06-23T08:00:00.000Z",
    "updatedAt": "2025-06-23T10:00:00.000Z"
  }
  ```

#### DELETE `/fieldofstudies/{id}`
- **Description**: Delete a field of study by ID.
- **Input**: ID of the field of study to delete (e.g., 1)
- **Sample Output**:
  ```json
  {
    "message": "Field of Study with ID 1 deleted successfully."
  }
  ```

#### DELETE_MANY `/fieldofstudies/deleteMany`
- **Description**: Delete multiple fields of study.
- **Input**: None (or a list of IDs if supported by API)
- **Sample Output**:
  ```json
  {
    "message": "Multiple fields of study deleted successfully.",
    "count": 2
  }
  ```

## General Notes for Testing
- **API Base URL**: By default, the Streamlit application uses `http://localhost:4000`. Ensure your VetNet Microservice is running at this URL or update the configuration in the Streamlit sidebar.
- **Static Token**: The application uses a default token for authentication. If your API requires a different token, update it via the Streamlit sidebar under "Configuration".
- **Error Handling**: If an API call fails, the response will include an error message, status code, and response text (if available). Use this information to debug issues like missing fields or incorrect data formats.
- **DELETE_MANY**: This operation may vary in implementation. The sample output assumes a successful deletion of multiple items, but your API might require a list of IDs in the request body. Adjust testing accordingly if needed.

This documentation covers all input fields, sample inputs, and expected outputs for each operation across all API categories in the VetNet Microservice. Use this as a reference while testing with the Streamlit application to ensure accurate and effective interaction with the API endpoints.
