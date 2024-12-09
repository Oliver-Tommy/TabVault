# TabVault

TabVault is an online platform designed to help creators organize, store, and manage their guitar tabs. The platform allows users to bookmark tabs for easy access and manage them through a secure dashboard. This project is part of the Code Institute's Full-Stack Developer course and focuses on the Django framework, database management, and CRUD functionality.

## TabVault Homepage

INSERT RESPONSIVITY PIC HERE

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
  - [User View - Registered/Unregistered](#user-view-registeredunregistered)
  - [Role-Based Dashboard Features](#role-based-dashboard-features)
  - [Role-Based Navigation](#role-based-navigation)
  - [Bookmark Feature](#bookmark-feature)
  - [CRUD Functionality](#crud-functionality)
- [Technologies & Languages Used](#technologies-languages-used)
  - [Libraries & Frameworks](#libraries-frameworks)
  - [Tools & Programs](#tools-programs)
- [Testing](#testing)
  - [Validation Testing](#validation-testing)
  - [User Testing](#user-testing)
  - [Bugs](#bugs)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Heroku deployment](#heroku-deployment)
- [Privacy Policy](#privacy-policy)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

## Overview

TabVault is a platform that allows the tab creator to:
- Store their tabs.
- Provide easy access to consumers.
- Provide consumers with a streamlined experience

A significant share of content creators in the guitar sphere create their own tabs. Many of these creators resort to third party websites, or have their own in order to share them. This platform is designed to provide a creator with the means to share their guitar tablature. There is a future potential to also put tabs behind a paywall. 

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
- Provide an intuitive and accessible dashboard.
- Ensure data security for registered users.
- Full responsivity.

### Project Management
This project was primarily managed through use of the GitHub project board, using issues, with MoSCoW prioritisation. There was additional use of a physical to-do list, for smaller issues.


### User Stories

Must haves:

- As a Creator, I can upload tabs so that I can share my work with users.
- As a Creator, I can edit or delete my uploaded tabs so that I can keep my content up to date.
- As a user I can login to access all user privileges.
- As a Site User, I can view detailed information about a tab so that I can decide whether to download it.
- As a Site Admin, I can view and manage all content and users so that I can ensure the platform runs smoothly.
- As a Site User, I can browse and discover tabs so that I can find content relevant to me.

Should haves:

- As a User, I can leave reviews and ratings for a tab so that I can provide feedback to the creator.
- As a User, I can bookmark tabs so that I can save them for later.
- As a User, I can view and edit bookmarks.
- As a User, I can modify or delete my review so that I can correct or remove my feedback.
- As a user I can utilise a search bar so that I can find a tab.

Could haves: 

- As a user I can see the average rating so that I know which tabs are the most highly rated
- As a Creator, I can create and manage my profile so that users can learn about me and my work.
- As a Creator, I can view analytics for my tabs so that I can track their performance.

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
Django's built-in security features handles all data securely:
- Passwords are encrypted.
- Forms are CSRF protected.
- Permission to access data is restricted by role.

## Features

### User View - Unregistered
- When a user is unregistered, they have access to all tabs, with the ability to search, fully navigate and download.

### Reviews
- When a user is logged in, they can submit a review for each tab, with a 1-5 star rating and additional text. This 

### Navigation bar
Logge


### Search bar

### Bookmark Feature

### Review aggregation

### View count

## Technologies & Languages Used

### Libraries & Frameworks
- Django - Backend framework.
- JavaScript - For interactivity and dynamic content.
- HTML5, CSS3, Bootstrap - Markup and styling languages, with bootstrap framework for styling.

### Tools & Programs
- GitHub - Version control.
- Heroku - Deployment.

## Testing

### Validation Testing


### User Testing


### Bugs


## Deployment

### Connecting to GitHub


### Django Project Setup


### Heroku Deployment

## Credits

### Code


### Media


### Additional reading/tutorials/books/blogs


### Acknowledgements


