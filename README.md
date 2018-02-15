# IrishDeals

Django Milestone project created by Jonathan Bencomo for the Code Institute, Dublin 2018.

[![Build Status](https://travis-ci.org/Bencomo/irishdeals.svg?branch=master)](https://travis-ci.org/Bencomo/irishdeals)

# Demo

A demo version of this project can be found [here] (https://irishdeals.herokuapp.com/)

# Project guidelines

 - Build a web app that fulfills some actual (or imagined) real-world need. This can be of your choosing and may be domain specific.
 - Write a README.md file for your project that explains what the project does and the need that it fulfills. It should also describe the functionality of the project, as well as the technologies used. Detail how the project was deployed and tested and if some of the work was based on other code, explain what was kept and how it was changed to fit your need. A project submitted without a README.md file will FAIL.
 - The project must be a brand new Django project, composed of multiple apps (an app for each reusable component in your project).
 - The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
 - At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, etc.
 - Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
 - The project will need to connect to a database (e.g., sqlite or Postgres) using Django’s ORM
 - The UI should be responsive, use either media queries or a responsive framework such as Bootstrap to make sure that the site looks well on all commonly-used devices.
 - As well as having a responsive UI, the app should have a great user experience.
 - The frontend should contain some JavaScript logic to enhance the user experience.
 - Whenever relevant, the backend should integrate with third-party Python/Django packages, such as Django Rest Framework, etc. Strive to choose the best tool for each purpose and avoid reinventing the wheel, unless your version of the wheel is shinier (and if so, consider also releasing your wheel as a standalone open source project).
 - Make sure to test your project extensively. In particular, make sure that no unhandled exceptions are visible to the users, under any circumstances. Use automated Django tests wherever possible. For your JavaScript code, consider using Jasmine tests.
 - Use Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
 - Deploy the final version of your code to a hosting platform such as Heroku.