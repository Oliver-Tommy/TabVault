# TabVault

TabVault is an online platform designed to help creators organize, store, and manage their guitar tabs. The platform allows users to bookmark tabs for easy access and manage them through a secure dashboard. This project is part of the Code Institute's Full-Stack Developer course and focuses on the Django framework, database management, and CRUD functionality.

## TabVault Homepage

![Image of the sites responsivity on varying devices](readme/images/responsivity.png)

Live site: [TabVault](https://tab-vault-b662f7e82794.herokuapp.com/)


## Table of Contents
- [Overview](#overview)
- [UX - User Experience](#ux-user-experience)
  - [Colour Scheme](#colour-scheme)
  - [Font](#font)
- [Project Planning](#project-planning)
  - [Site Goals](#site-goals)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
- [Security](#security)
- [Features](#features)
- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Validation Testing](#validation-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [User Testing](#user-testing)
  - [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## Overview

TabVault is a comprehensive platform designed for guitar tab creators and enthusiasts that enables:
- Storage and organization of guitar tabs
- Sharing and distribution to fans and students
- A streamlined, user-friendly experience for both creators and consumers
- Professional presentation of the content

Guitar content creators often struggle with effectively sharing their tablature, either relying on third-party websites with limited features or building costly custom solutions. TabVault bridges this gap by providing a dedicated platform where creators can easily upload, manage and distribute their guitar tabs to their audience. The platform is built with the potential forfuture scalability in mind, with possibilities for a creator-based system, with paid access to tabs.

## UX - User Experience

### Colour Scheme

<b>Linen (#FFF1E6):</b> Clean and warm backgrounds.

<b>Fairy Tale (#FEC8D8):</b> For primary buttons (download link).

<b>Melon (#F8B195):</b> For hover states.

<b>Platinum (#E6E6E6):</b> Borders & dividers.

<b>Space cadet (#2F2E41):</b> Text.

<b>Mint green (#B8E1DD):</b> Secondary buttons

![Image of the colours used](readme/images/colour-scheme.jpg)

### Font
<b>Merriweather (for titles):</b> Was chosen for titles as it is highly readable, with a traditional, formal feel. 

<b>Roboto (for body text):</b> Was chosen for the body text, as it is clean and legible. Also, it's popularity and widespread use provides the user with familiarity. 

The contrast in style between the 'classic' Merriweather and the more 'modern' Roboto helps draw attention to headings and provides a clear visual separation.

![Image of the fonts used](readme/images/fonts.jpg)

## Project Planning

### Site Goals
- Allow users to bookmark and manage tabs.
- Provide an accessible dashboard that displays relevant information clearly.
- Full responsivity across all devices and screen sizes.
- Enable easy tab uploads and downloads.
- Implement a review and rating system.
- Maintain high performance and fast load times.
- Provide comprehensive search capabilities.
- Enable easy content management for creators.

### Project Management
This project was primarily managed through GitHub's project board functionality. Issues were created for all major features and tasks, each categorized using MoSCoW prioritization (Must have, Should have, Could have, Won't have) to ensure proper resource allocation and timely delivery.

The GitHub project board was organized into the following columns:
- To Do: New issues and tasks to be worked on
- In Progress: Currently being developed
- Done: Completed and verified features

For day-to-day task management and smaller items that didn't need issues, I maintained a physical to-do list to track minor bug fixes, small UI improvements, and other quick tasks.



### User Stories

Must haves:


- As a Creator, I can upload tabs so that I can share my work with users.
  - AC1: Given a logged-in creator, they can upload a tab file and metadata (title, artist, genre, difficulty).
  - AC2: Then the file is securely stored.

- As a Creator, I can edit or delete my uploaded tabs so that I can keep my content up to date.
  - AC1: Given a logged-in creator, they can edit metadata (e.g., title, genre, artist) of their uploaded tabs.
  - AC2: Given a logged-in creator, they can delete a tab they uploaded.

- As a user I can login to access all user privileges.
  - AC1: When not logged in, register and login buttons present
  - AC2: When logged in, sign out button present
  - AC3: After login/register, redirect to home page

- As a Site User, I can view detailed information about a tab so that I can decide whether to download it.
  - AC1: Given a tab title is clicked, the user is directed to a detailed view showing its metadata (title, artist, genre, difficulty).
  - AC2: When the tab is viewed, the view count increments.
  - AC3: Then users see reviews and ratings submitted by others.

- As a Site Admin, I can view and manage all content and users so that I can ensure the platform runs smoothly.
  - AC1: Admins can view all uploaded tabs, reviews, and user profiles.
  - AC2: Admins can deactivate or delete inappropriate tabs, reviews, or accounts.

- As a Site User, I can browse and discover tabs so that I can find content relevant to me.
  - AC1: When visiting the homepage, users see tabs.
  - AC2: Then users can search for tabs by genre, difficulty, or artist.
  - AC3: When filtering tabs, the results update dynamically.

Should haves:


- As a User, I can leave reviews and ratings for a tab so that I can provide feedback to the creator.
  - AC1: Given a logged-in user, they can submit a star rating (1–5).
  - AC2: Given a logged-in user, they can add a text comment.
  - AC3: Then the review is associated with the user and the tab.

- As a User, I can bookmark tabs so that I can save them for later.
  - AC1: Given a logged-in user, they can click a "bookmark" button to save a tab.
  - AC2: Then the user can view a list of their bookmarked tabs in their profile/dashboard.
  - AC3: When a bookmarked tab is deleted by the creator, it is automatically removed from the user's list.
  
- As a User, I can view and edit bookmarks.

- As a User, I can modify or delete my review so that I can correct or remove my feedback.
  - AC1: Given a logged-in user, they can edit the text and rating of their submitted review.
  - AC2: Given a logged-in user, they can delete their review.
  - AC3: Then the review updates are reflected immediately.

- As a user I can utilise a search bar so that I can find a tab.
  - AC1: Search bar can be found easily
  - AC2: Upon searching a title, artist or genre, a list of relevant tabs comes up
  - AC3: If there are no relevant results, the user is given a response

Could haves: 


- As a user I can see the average rating so that I know which tabs are the most highly rated.
  - AC1: Reviews average star rating is shown.
  - AC2: You can sort by average rating
  - AC3: Average ratings update as reviews are added or deleted

- As a Creator, I can create and manage my profile so that users can learn about me and my work.
  - AC1: Given a logged-in user, they can add or update their bio.
  - AC2: Given a logged-in user, they can upload or change a profile picture.
  - AC3: Then their profile displays their uploaded tabs.

- As a Creator, I can view analytics for my tabs so that I can track their performance.
  - AC1: When visiting the creator dashboard, creators see views and average ratings for each tab.
  - AC2: Then creators can view aggregated metrics (e.g., total uploads, total reviews).


Image of the project board after sprint completion:

![GitHub Project board](readme/images/Project-board.png)

### Wireframes

Homepage:
<p float="left">
  <img src="readme/images/INDEX.png" width="480" />
  <img src="readme/images/INDEX(PHONE).png" width="170" /> 
</p>

Tab detail page:
<p float="left">
  <img src="readme/images/TAB_DETAIL.png" width="480" />
  <img src="readme/images/TAB_DETAIL(PHONE).png" width="170" /> 
</p>

Bookmarks page:
<p float="left">
  <img src="readme/images/BOOKMARKS.png" width="480" />
  <img src="readme/images/BOOKMARKS(PHONE).png" width="170" /> 
</p>

Search results page:
<p float="left">
  <img src="readme/images/SEARCH_RESULTS.png" width="480" />
  <img src="readme/images/SEARCH_RESULTS(PHONE).png" width="170" /> 
</p>


### Entity Relationship Diagram

![Entity relationship diagram](readme/images/my-project.png)

Dot file generated using <a href ="https://pypi.org/project/pydot/">pydot</a>

Converted to PNG using <a href="https://onlineconvertfree.com/convert-format/dot-to-png/">onlineconvertfree</a>

## Security

Django's built-in security features handle all data securely:

- Passwords are encrypted using Django's default PBKDF2 algorithm with SHA256 hash
- All forms are protected against Cross-Site Request Forgery (CSRF) attacks using Django's middleware
- User authentication and authorization restricts access based on roles:
  - Only authenticated users can access bookmarking features
  - Only authenticated users can submit reviews
  - Admin users have full access to the Django admin interface
- Database queries are protected against SQL injection through Django's ORM
- Cross-Site Scripting (XSS) protection is enabled by default
- Clickjacking protection via X-Frame-Options middleware
- Debug mode is disabled in production
- Secure password validation enforces:
  - Minimum length requirements
  - Common password checking
  - Numeric character requirements

## Features

### User View - Unregistered
- When a user is unregistered, they have access to all tabs, with the ability to search, fully navigate and download.
- However, the user is unable to leave a review, or access the bookmarking page and feature.

### Reviews
- When a user is logged in, they can submit a review for each tab, with a 1-5 star rating and additional text. 
- The star ratings are stored for each tab, and they are aggregated and averaged, then displayed to the user.

### Navigation bar
- When a user isn't logged in, the navigation bar displays options to login and register.
- When a user is logged in, only the logout option appears.
- The navbar is fully responsive, with a dropdown appearing on tablet-sized screens and smaller.
- The users login status is displayed.

### Search bar
- The navigation bar has a search bar present, which allows users to search for the tab title, artist, and genre.

### Bookmark Feature
- When logged in, and viewing a tab_detail page, the user can either add or remove the tab to their 'bookmarks'.
- The user can access their bookmarked tabs, using the bookmarked tabs button on the navigation bar.
- In the bookmarked_tabs page, the user's bookmarked tabs are displayed.

### View count
- When a user visits a particular tab_detail page, the view count increments by 1.

## Future Features

### Many creators
- Currently the site is for the use of only one creator, as many such websites are.
- In the future, many users, apon admin validation, will be able to have a 'creator' account, with the ability to create profiles and add tabs with full CRUD functionality.

### Monetization
- In order to view a tab, the user has to pay to gain access priveleges.
- Creators can set their own prices.

### Social Features
- Add ability for users to follow their favorite creators
- Implement a commenting system on tabs
- Allow users to share tabs on social media platforms
- Create user profile pages with activity feeds

### Enhanced Tab Features
- Add video tutorials linked to specific tabs
- Implement an interactive tab player
- Add difficulty ratings and estimated completion time
- Include practice tips and techniques for each tab

### Advanced Analytics
- Provide detailed analytics for creators including user demographics
- Track user engagement metrics
- Generate revenue reports for monetized content
- Show trending tabs and popular genres

### Mobile App
- Develop native mobile applications for iOS and Android
- Enable offline access to downloaded tabs
- Add push notifications for new tabs from followed creators
- Implement mobile-specific features like metronome and tuner

## Technologies Used

### Languages
- HTML5 & CSS3 - Core web technologies for structure and styling
- JavaScript - Client-side programming for interactive features
- Python - Server-side programming language
- PostgreSQL - Relational database system

### Libraries & Frameworks
- Bootstrap 5 - Frontend CSS framework
- Django 4 - Python web framework
- Cloudinary - Cloud storage service for media files
- WhiteNoise - Static file serving for Python web apps

### Development & Deployment
- Git & GitHub - Version control and code hosting
- Heroku - Cloud platform for deployment

## Testing

### Validation Testing

All HTML pages were validated using the <a href="https://validator.w3.org">W3C Markup Validation Service.</a>

index.html:

![Image of the index.html validation](readme/images/index-validation.png)

tab_detail.html:

![Image of the tab_detail.html validation](readme/images/tab_detail-validation.png)

bookmarked_tabs.html:

![Image of the bookmarked_tabs.html validation](readme/images/bookmarks-validation.png)

search_results.html:

![Image of the search_results.html validation](readme/images/search-results-validation.png)

The CSS was validated using the <a href="https://jigsaw.w3.org/css-validator/">W3C CSS Validation Service.</a>

style.css:

![Image of the style.css validation](readme/images/css-validation.png)

Javascript was validated using <a href="https://jshint.com/">JSHint version 2.13.6:</a>

![Image of the Javascript ](readme/images/JSHint.png)

Python was tested for PEP8 compatibilty using the <a href="https://pep8ci.herokuapp.com/">CI Python Linter</a>, and the python files: models.py, test_form.py, urls.py and views.py were edited for easier readability.


### Lighthouse testing

Mobile testing demonstrated strong results across most metrics:
- High accessibility score
- Strong best practices implementation 
- Good SEO optimization
- Slightly reduced performance due to render-blocking resources

![Image of the mobile lighthouse test](readme/images/mobile-lighthouse.png)

The performance impact was primarily due to render-blocking resources:

![Image of the mobile lighthouse performace warnings](readme/images/mobile-lighthouse-performance.png)

Desktop testing showed optimal performance across all metrics:

![Image of the desktop lighthouse test](readme/images/desktop-lighthouse.png)


### User Testing

The site underwent comprehensive testing by multiple users across different demographics:

Devices tested on included:
- iPhone 11, 13, 13 Pro Max, 15
- iPad Pro
- Various desktop monitors (1080p and 4K)

Each user performed the following testing protocol:
1. Browsed the site as an anonymous user
2. Created an account
3. Logged in and tested authenticated features
4. Tested responsive design by resizing browser window
5. Attempted edge cases like invalid inputs
6. Provided feedback on user experience

All core features were thoroughly tested and verified working:
- Account creation and authentication
- Tab uploading and management
- Review system
- Bookmark functionality
- Search capabilities
- Responsive design elements

<strong>User Story Testing Results:</strong>

| Test Case                 | Expected Behavior | Actual Result | Status  |
| ------------------------- | ---------------- | ------------- | ------- |
| Manage tabs               | Users can create, edit, and delete tabs | Functions as expected | Success |
| Upload tabs              | Users can upload new tabs with metadata | Upload works correctly | Success |
| Leave reviews and ratings | Users can post reviews and star ratings | Rating system works properly | Success |
| Login                    | Users can authenticate securely | Login process smooth | Success |
| View tab details         | Users can see full tab information | All details display correctly | Success |
| Edit reviews             | Users can modify their existing reviews | Edit function works | Success |
| Search bar functions     | Users can search tabs by various criteria | Search returns accurate results | Success |
| Manage content           | Admins can moderate all site content | Admin controls working | Success |
| Bookmark tabs            | Users can save tabs for later | Bookmark system functional | Success |
| View analytics           | Users can see tab statistics | Analytics display correctly | Success |
| Browse Tabs              | Users can view and filter tab listings | Browse feature works smoothly | Success |

### Bugs
During development, several bugs were encountered and resolved:

1. Static Files Loading Issue:
   - Problem: Static files (particularly style.css) weren't loading on index.html and search_results.html pages in the deployed site
   - Solution: Added {% load static %} to the affected templates and verified static file configuration in settings.py
   - Temporary workaround required manual collectstatic commands until fully resolved

2. Search Functionality:
   - Problem: Search results were not displaying correctly when using special characters
   - Solution: Implemented proper URL encoding and input sanitization

3. Mobile Navigation:
   - Problem: Hamburger dropdown menu wasn't responding on some mobile devices
   - Solution: Changed the bootstrap classes to ensure the dropdown menu was working

4. PDF file validation:
   - Problem: PDF files were not being validated
   - Solution: Added a validation function to the model

All identified bugs were documented, tracked, and resolved to ensure optimal site functionality.


## Deployment

Throughout the development process, the site was deployed to Heroku from the main repository branch. The following steps were taken to ensure successful deployment:

1. Environment Setup:
   - Created a requirements.txt file using `pip freeze > requirements.txt` to track all Python dependencies
   - Added a Procfile containing `web: gunicorn tabvault.wsgi` to configure the Gunicorn web server
   - Updated settings.py to include both Heroku app URL and localhost in ALLOWED_HOSTS

2. Database Configuration:
   - Set up a PostgreSQL database instance on ElephantSQL
   - Connected the database to the application using the DATABASE_URL environment variable
   - Ran migrations to set up the database schema

3. Environment Variables:
   The following config vars were set in Heroku:
   - DATABASE_URL: PostgreSQL database connection string
   - SECRET_KEY: Django secret key for security
   - CLOUDINARY_URL: Connection string for Cloudinary media storage
   These replaced the local variables from env.py which was excluded from version control

4. Static Files:
   - Configured Cloudinary for static and media file hosting
   - Ran collectstatic to gather all static files

5. Deployment Steps:
   - Connected GitHub repository to Heroku application
   - Verified build logs and ensured successful deployment
   - Confirmed application was running correctly on Heroku URL

6. Post-Deployment:
   - Tested all functionality on live site
   - Verified database connections and migrations
   - Confirmed static files were being served correctly
   - Checked all environment variables were working as expected

## Credits

### Code

For utilising Django:
- <a href="https://docs.djangoproject.com/">Django documentation</a>
- <a href="https://www.djangoproject.com/start/">Django Getting Started Guide</a>
- <a href="https://docs.djangoproject.com/en/4.2/topics/forms/">Django Forms documentation</a>

For debugging and finding solutions:
- <a href="https://stackoverflow.com/">Stack overflow</a>
- <a href="https://github.com/">GitHub Issues & Discussions</a>

For utilising Bootstrap:
- <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/">Bootstrap documentation</a>
- <a href="https://getbootstrap.com/docs/5.3/examples/">Bootstrap Examples</a>
- <a href="https://getbootstrap.com/docs/5.3/components/">Bootstrap Components</a>

For debugging:
- <a href="https://chatgpt.com/">ChatGPT</a>
- <a href="https://developer.mozilla.org/en-US/">MDN Web Docs</a>

For deployment:
- <a href="https://devcenter.heroku.com/categories/python-support">Heroku Python Support</a>


### Media

Guitar player stock image - <a href="https://pixabay.com/photos/acoustic-guitar-guitarist-1851248/">Link</a>

Favicon - <a href="https://www.flaticon.com/free-icons/vault" title="vault icons">Vault icons created by Smashicons - Flaticon</a>

Converted to favicon using: https://favicon.io/favicon-converter/


### Acknowledgements

I would like to thank my facilitator, Alex, for his guidance and support throughout the project.

I would also like to thank my subject matter expert, Mark, for his great teaching and support.
